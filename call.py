from twilio.rest import Client
import sys
import config

from_number = sys.argv[1]
to_number = sys.argv[2]
text_to_say = sys.argv[3]

def say(fromNo=from_number, toNumber = to_number, textToSay = text_to_say):
    client = Client(config.account_sid, config.auth_token)
    call = client.calls.create(
                        twiml=f'<Response><Pause length="3"/><Say voice="Polly.Kajal-Neural">{textToSay}</Say></Response>',
                        to=toNumber,
                        from_=fromNo
                    )
    print("Call initiated:", call.sid)

if __name__ == "__main__":
    say(from_number, to_number, text_to_say)
