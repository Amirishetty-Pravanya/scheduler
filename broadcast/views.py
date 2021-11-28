from django.conf import settings                                                                                                                                                       
from django.http import HttpResponse
from twilio.rest import Client


def broadcast_sms(request):
    message_to_broadcast = ("Have you played the incredible TwilioQuest "
                                                "yet? Grab it here: https://www.twilio.com/quest")
    client = Client("AC781a6124e645245f10e146457d688b63","c0bcb7a7fc55e2c80f089d055e256f72")
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to='+919398595860',
                                   from_='+17175239533',
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!", 200)
