from datetime import datetime, timezone
from .thread_generator import generate_posts
from .dyanmodb_repo import insert_thread, get_thread, append_post, remove_is_processing


def handle_request(question: str, id: str):

    # Fetch any existing discussion
    thread = get_thread(id)
    if (not thread):
        created_date = datetime.now(timezone.utc).replace(microsecond=0)
        thread = {
            "year": created_date.year,
            "created_date": created_date.isoformat(),
            "id": id,
            "question": question,
            "is_processing": True,
            "post": []
        }

    # We insert the thread into dynamodb right away
    insert_thread(thread)

    # todo Make this a generator and insert the posts as they come
    for post in generate_posts(question, thread["post"]):
        thread["post"].append(post)
        # update dynamodb with each post as they're created
        append_post(id, post)

    # Mark that the thread is complete in dynamodb
    remove_is_processing(id)
