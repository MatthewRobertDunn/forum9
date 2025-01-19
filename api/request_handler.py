import simplejson
import sys
import os
from urllib.parse import parse_qs
import traceback
class MethodNotAllowed(Exception):
    pass

def handle_request(service_function, request_method):
    try:
        # Check if the request method is POST
        if 'REQUEST_METHOD' not in os.environ or os.environ['REQUEST_METHOD'] != request_method:
            raise MethodNotAllowed(f"Request method must be {request_method}")
        
        request = {}
        if 'QUERY_STRING' in os.environ:
            query_string = os.environ.get("QUERY_STRING", "")
            # Parse the query string into a dictionary
            parsed_params = parse_qs(query_string)
            request = {key: value[0] for key, value in parsed_params.items()}
        
        if 'CONTENT_LENGTH' in os.environ and os.environ['CONTENT_LENGTH'].isnumeric() and int(os.environ['CONTENT_LENGTH']) > 0:
            raw_post_data = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
            body = simplejson.loads(raw_post_data)
            request['body'] = body

        request['method'] = request_method
        response = service_function(**request)
        response_json = simplejson.dumps(response)
        print("Status: 200 OK")
    except MethodNotAllowed as e:
        response_json = simplejson.dumps({"status": "error", "message": str(e)})
        print("Status: 405 Method Not Allowed")
    except Exception as e:
        response_json = simplejson.dumps({"status": "error", "message": str(e), "traceback": traceback.format_exc()})
        print("Status: 500 Internal Server Error")
    print("Content-Type: application/json\n")      
    print()  # Blank line separating headers from body
    print(response_json)