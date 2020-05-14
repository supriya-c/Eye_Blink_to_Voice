#Text and Voice Message

from twilio.rest import Client
account_sid = "TWILIO_ACOOUNT_SID"
auth_token = "TWILIO_AUTH_TOKEN"
client = Client(account_sid, auth_token)

#Text Message
client.api.account.messages.create(
    to="CONTACT_NO",
    from_="TWILIO_NO" ,
    body=" Text Message" )

#Voice Message
call = client.calls.create(
                        twiml='<Response><Say>Selected message for voice call</Say></Response>',
                        to='CONTACT_NO',
                        from_='TWILIO_NO'
                    )

print(call.sid)

