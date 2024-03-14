from telethon.sync import TelegramClient
from telethon.tl.types import Message
import time

api_id = 'YOUR_API_ID'  # Replace with your actual API ID
api_hash = 'YOUR_API_HASH'  # Replace with your actual API hash
phone_number = 'YOUR_PHONE_NUMBER'  # Replace with your phone number in international format

def print_received_messages(event):
    if isinstance(event, Message):
        print(f"Received message from {event.sender_id}: {event.text}")
        reply_message = f"Hello! You said: {event.text}"
        client.send_message(event.sender_id, reply_message)

with TelegramClient('session_name', api_id, api_hash) as client:
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        client.sign_in(phone_number, input('Enter the code: '))

    client.add_event_handler(print_received_messages)

    while True:
        try:
            client.run_until_disconnected()
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(5)  # Wait for 5 seconds before reconnecting
