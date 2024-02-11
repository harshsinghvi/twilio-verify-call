from dotenv import load_dotenv
import os

load_dotenv()

# Your Twilio Account SID and Auth Token
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']