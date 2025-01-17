import json
import sys

class MethodNotAllowed(Exception):
    pass

def handle_request(service_function):
    print("Content-Type: application/json\n")  
    try:
        # Check if the request method is POST
        if 'REQUEST_METHOD' not in sys.stdin.environ or sys.stdin.environ['REQUEST_METHOD'] != 'POST':
            raise MethodNotAllowed("Request method must be POST")
        raw_post_data = sys.stdin.read(int(sys.stdin.environ.get('CONTENT_LENGTH', 0)))
        message = json.loads(raw_post_data)
        response = service_function(message)
        print("Status: 200 OK")
    except MethodNotAllowed as e:
        response = {"status": "error", "message": str(e)}
        print("Status: 405 Method Not Allowed")
    except Exception as e:
        response = {"status": "error", "message": str(e)}
        print("Status: 500 Internal Server Error")
    
    print()  # Blank line separating headers from body
    print(json.dumps(response))