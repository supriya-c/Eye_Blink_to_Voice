'''from twilio.rest import Client

### Find these values at https://twilio.com/user/account
account_sid = "AC0c7e826cedb7edf4aaa8a7ef56fa501d"
auth_token = "e0989ce732ceabe95e75647eaff97353"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+91-7899391634",
    from_="+12067410072" ,
    body=" hi" )'''



from twilio.rest import Client

account_sid = 'AC0c7e826cedb7edf4aaa8a7ef56fa501d'
auth_token = 'e0989ce732ceabe95e75647eaff97353'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>i need to pee!</Say></Response>',
                        to='+91-7899391634',
                        from_='+12067410072'
                    )

print(call.sid)

