from datetime import datetime, timezone
from post_generator import generate_discussion
from dyanmodb_repo import insert_discussion
def handle_request(question: str, id: str):

    #Fetch any existing discussion

    discussion = generate_discussion(question, id)
    if(not discussion):
        return
    created_date = datetime.now(timezone.utc).replace(microsecond=0)
    discussion = {
            "year": created_date.year,
            "created_date": created_date.isoformat(),
            "id": id,
            "question": question,
            "post": discussion
           }
    insert_discussion(discussion)