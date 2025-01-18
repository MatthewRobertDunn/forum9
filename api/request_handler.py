import json
import sys
import os
from urllib.parse import parse_qs

class MethodNotAllowed(Exception):
    pass

def handle_request(service_function, request_method):
    try:
        # Check if the request method is POST
        if 'REQUEST_METHOD' not in os.environ or os.environ['REQUEST_METHOD'] != request_method:
            raise MethodNotAllowed(f"Request method must be {request_method}")
        query_string = os.environ.get("QUERY_STRING", "")
        # Parse the query string into a dictionary
        request = parse_qs(query_string)
        raw_post_data = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
        body = json.loads(raw_post_data)
        request['body'] = body
        request['method'] = request_method
        response = service_function(**request)
        print("Status: 200 OK")
    except MethodNotAllowed as e:
        response = {"status": "error", "message": str(e)}
        print("Status: 405 Method Not Allowed")
    except Exception as e:
        response = {"status": "error", "message": str(e)}
        print("Status: 500 Internal Server Error")
    print("Content-Type: application/json\n")      
    print()  # Blank line separating headers from body
    print(json.dumps(response))