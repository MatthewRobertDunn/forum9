import json
from typing import Dict, List
from ..middleware.bus import register_handler
from ..middleware.cache import get_cached_response


def post_exists(posts: List[Dict[str, str]], post_id: int) -> bool:
    for post in posts:
        if post["id"] == post_id:
            return True
    return False


def on_new_post(content):
    np = json.loads(content)
    thread_id = np["thread_id"]
    new_post = np["post"]
    new_post_id = new_post["id"]
    print(f"New post in thread {thread_id}: {new_post_id}")
    thread = get_cached_response(f"thread-{thread_id}")

    if (not thread):
        print(f"Thread {thread_id} not found in cache, skipping")
        return

    posts = thread.get("posts")
    if (not posts):
        return

    if (post_exists(posts, new_post_id)):
        return
    
    print(f"Appended new post to thread {thread_id}")
    posts.append(new_post)
    
    # sort posts by id ascending
    posts.sort(key=lambda x: x["id"])

def register():
    print("Registering new_post handler")
    register_handler("new_post", on_new_post)
