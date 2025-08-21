from datetime import datetime, timezone
import random

from .notifications import topics
from .notifications.notifications import NewPostNotification
from .notifications import bus
from .scopes.thread_scope import thread_scope
from .thread_generator import generate_posts
from .dyanmodb_repo import insert_thread, get_thread, append_post, remove_is_processing


def handle_request(question: str, id: str):
    """
    Handle a single request from the SQS queue.

    This function will generate a thread of posts in response to a given question and
    insert them into the dynamodb table. It will also mark the thread as complete when
    finished.

    :param question: The question to be answered
    :type question: str
    :param id: The id of the thread
    :type id: str
    """
    with thread_scope(id):
        _handle_request(question, id)


def _handle_request(question: str, id: str):
    # Fetch any existing discussion
    thread = get_thread(id)
    if (not thread):
        created_date = datetime.now(timezone.utc).replace(microsecond=0)
        thread = {
            "year": created_date.year,
            "created_date": created_date.isoformat(),
            "id": id,
            "count": random.randint(1, 30) + 2,
            "question": question,
            "is_processing": True,
            "posts": []
        }

        # We insert the thread into dynamodb right away
        insert_thread(thread)

    # todo Make this a generator and insert the posts as they come
    for post in generate_posts(question, thread["posts"], thread["count"]):
        thread["posts"].append(post)
        # update dynamodb with each post as they're created
        append_post(id, post)
        # notify any subscribers that a new post has been added
        bus.publish(topics.new_post,
                    NewPostNotification(
                        id,
                        post["id"],
                        persona=post["persona"],
                        post=post["content"]
                    ))

    # Mark that the thread is complete in dynamodb
    remove_is_processing(id)
