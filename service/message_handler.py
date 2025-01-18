from datetime import datetime, timezone
from post_generator import generate_post
from dyanmodb_repo import insert_post
def handle_request(question: str, id: str):
    post = generate_post(question, id)
    created_date = datetime.now(timezone.utc).replace(microsecond=0)
    post = {
            "year": created_date.year,
            "created_date": created_date.isoformat(),
            "id": id,
            "question": question,
            "post": post
           }
    insert_post(post)