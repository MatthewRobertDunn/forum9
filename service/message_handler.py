from datetime import datetime, timezone
from post_generator import generate_post
from dyanmodb_repo import insert_post
def handle_request(question: str, id: str):
    post = generate_post(question, id)
    created_date = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    post = {
            "id": id,
            "created_date": created_date,
            "post": post
           }
    insert_post(post)