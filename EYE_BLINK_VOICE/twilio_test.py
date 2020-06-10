#Text and Voice Message

from twilio.rest import Client
account_sid = os.environ['TWILIO_ACOOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

#Text Message
client.api.account.messages.create(
    to=os.environ['CONTACT_NO'],
    from_=os.environ['TWILIO_NO'],
    body=" Text Message" )

#Voice Message
call = client.calls.create(
                        twiml='<Response><Say>Selected message for voice call</Say></Response>',
                        to=os.environ['CONTACT_NO'],
                        from_=os.environ['TWILIO_NO']
                    )

print(call.sid)

