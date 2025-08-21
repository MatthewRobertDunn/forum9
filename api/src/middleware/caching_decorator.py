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


def cache_json_response(etag_func, key_func=get_cache_key):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            cache_key = key_func(request)
            if cache_key in _cache:
                cached_response, cached_etag = _cache[cache_key]
                if etag_func and request.headers.get('If-None-Match') == cached_etag:
                    return "", 304
                return (cached_response, 200, {'ETag': cached_etag})

            response = f(*args, **kwargs)
            generated_etag = etag_func(response)
            _cache[cache_key] = (response, generated_etag)
            return (response, 200, {'ETag': generated_etag})
        return wrapped
    return decorator
