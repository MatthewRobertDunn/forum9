from cachetools import TTLCache
from functools import wraps
from flask import request, Request, make_response
import hashlib
import json

# Cache with max 1024 items, TTL 60 seconds
_cache = TTLCache(maxsize=1024, ttl=3600)


def get_cache_key(request: Request) -> str:
    key_data = {
        "path": request.path,
        "args": request.args,
        "json": request.get_json(silent=True)
    }
    cache_key = hashlib.blake2b(json.dumps(
        key_data, sort_keys=True).encode(), digest_size=16).hexdigest()
    return cache_key


def _weak_etag(etag: str) -> str:
    return f'W/"{etag}"'


def cache_json_response(etag_func, key_func=get_cache_key):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            cache_key = key_func(
                **kwargs) if key_func else get_cache_key(request)
            if cache_key in _cache:
                cached_response = _cache[cache_key]
                cached_etag = _weak_etag(etag_func(cached_response))
                if request.headers.get('If-None-Match') == cached_etag:
                    return "", 304
                print(
                    f"Returning cached response for {cache_key} with ETag {cached_etag}")
                return (cached_response, 200, {'ETag': cached_etag})

            response = f(*args, **kwargs)
            generated_etag = _weak_etag(etag_func(response))
            print(
                f"Caching response for {cache_key} with ETag {generated_etag}")
            _cache[cache_key] = response
            return (response, 200, {'ETag': generated_etag})
        return wrapped
    return decorator


def get_cached_response(cache_key: str):
    return _cache.get(cache_key, None)
