from twilio.rest import Client
from time import sleep

accountSid = None
authToken = None
myPhoneNumber = None
toPhoneNumbers = None

client = None

def setup():
    global accountSid, authToken, client, myPhoneNumber, toPhoneNumbers

    with open('.twilio.tokens', 'r') as f:
        accountSid = f.readline().strip()
        authToken = f.readline().strip()
        myPhoneNumber = f.readline().strip()

    with open('.phone.numbers', 'r') as f:
        toPhoneNumbers = [i.split() for i in f.readlines()]

    client = Client(accountSid, authToken)

def alert(text):
    if client is None:
        setup()

    for number in toPhoneNumbers:
        alert_one(text, number)

def alert_one(text, number):
    if client is None:
        setup()

    try:
        client.api.account.messages.create(
                to=number,
                from_=myPhoneNumber,
                body=text)
    except:
        sleep(30)
        alert_one(text, number)



if __name__ == '__main__':
    alert("test")
