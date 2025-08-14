from datetime import datetime, timezone
from thread_generator import generate_posts
from dyanmodb_repo import insert_thread, get_thread
def handle_request(question: str, id: str):

    #Fetch any existing discussion
    discussion = get_thread(id)
    if(not discussion):
        created_date = datetime.now(timezone.utc).replace(microsecond=0)
        discussion = {
            "year": created_date.year,
            "created_date": created_date.isoformat(),
            "id": id,
            "question": question
        }
        

    posts = generate_posts(question)
    if(not posts):
        return
    discussion = {
            "year": created_date.year,
            "created_date": created_date.isoformat(),
            "id": id,
            "question": question,
            "post": posts
           }
    insert_thread(discussion)