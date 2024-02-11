from twilio.rest import Client
import config
import sys

number = sys.argv[1]

def reg(num = number):
    client = Client(config.account_sid, config.auth_token)

    validation_request = client.validation_requests \
        .create(
            # friendly_name='Third Party VOIP Number',
            # status_callback='https://somefunction.twil.io/caller-id-validation-callback',
            phone_number=num
        )

    print(validation_request.validation_code)


if __name__ == "__main__":
    reg(number)
