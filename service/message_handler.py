from datetime import datetime, timezone
from thread_generator import generate_posts
from dyanmodb_repo import insert_thread, get_thread
def handle_request(question: str, id: str):

    #Fetch any existing discussion
    thread = get_thread(id)
    if(not thread):
        created_date = datetime.now(timezone.utc).replace(microsecond=0)
        thread = {
            "year": created_date.year,
            "created_date": created_date.isoformat(),
            "id": id,
            "question": question,
            "is_complete": False
        }
        

    posts = generate_posts(question)
    if(not posts):
        return
    thread = {
            "year": created_date.year,
            "created_date": created_date.isoformat(),
            "id": id,
            "question": question,
            "post": posts,
            "is_complete": True
           }
    insert_thread(thread)