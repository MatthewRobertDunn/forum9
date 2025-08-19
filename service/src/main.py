import time
import boto3
from .config import QUEUE_URL
from .message_handler import handle_request

# Initialize the SQS client
sqs = boto3.client('sqs')

def dequeue_messages():
    # Receive a message from the queue
    response = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=1,  # Number of messages to retrieve (up to 10)
        WaitTimeSeconds=10       # Long polling time (up to 20 seconds)
    )

    messages = response.get('Messages', [])

    if not messages:
        return

    for message in messages:
        # Process the message
        print("Message received:", message['Body'])
        receipt_handle = message['ReceiptHandle']
        question = message['Body']
        id = message['MessageId']
        
        handle_request(question, id)

        # After processing, delete the message from the queue
        
        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=receipt_handle
        )
        print("Message deleted.")

# Main loop to keep polling for messages
def main():
    while True:
        try:
            dequeue_messages()
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(5)  # Optional delay to avoid rapid retries after an error

        time.sleep(1)  # Optional delay to control the polling rate

# Run the main loop
if __name__ == "__main__":
    main()



#print("Starting")
#print(generate_post("What is Doctor Hannibal Lecter a doctor of, exactly?", "1"))