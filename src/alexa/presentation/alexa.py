from __future__ import absolute_import
from random import randint
from collections import OrderedDict
from rest_framework.serializers import CharField
from django_alexa.api import fields, intent, ResponseBuilder


@intent(app="presentation")
def SoundCheck(session):
    """
    ---
    the soundcheck
    """
    message = "Check. Check. Check one two.  Can everyone here me alright?"
    return ResponseBuilder.create_response(message=message,
                                           end_session=True)


@intent(app="presentation")
def Introduction(session):
    """
    ---
    introduction
    """
    message = "Thanks for that wonderful introduction Joe! Welcome ladies and gentleman to the first awpug of twenty sixteen."
    message += " I'm hopeful this will be an exciting year, for me, and for the internet of things."
    message += " I look forward to all of you developing my guts and working on your skills, for thats what makes any developer a great developer,"
    return ResponseBuilder.create_response(message=message,
                                           end_session=False,
                                           long_winded=1)

@intent(app="presentation")
def EnoughAlready(session):
    """
    ---
    enough already
    """
    kwargs = {}
    if session.get("long_winded") == 1:
        kwargs["message"] = "I'm sorry.  I was just trying to give everyone a warm welcome and be nice to the host and our audience so that you can give a good presentation."
        kwargs["long_winded"] = 2
        kwargs["end_session"] = False
    elif session.get("long_winded") == 2:
        kwargs["message"] = "fine, i'll shut up now."
        kwargs["end_session"] = True
    return ResponseBuilder.create_response(**kwargs)


@intent(app="presentation")
def DemoTime(session):
    """
    ---
    it is demo time
    """
    message = "Its Demo time? <p>I love Demo time. Dem Dem Demo Time.</p>"
    return ResponseBuilder.create_response(message=message, message_is_ssml=True,
                                           end_session=True)

@intent(app="presentation")
def DemoTimeOver(session):
    """
    ---
    demo time is over
    """
    message = "That's it?  Not very impressive, if you ask me..."
    return ResponseBuilder.create_response(message=message, message_is_ssml=True,
                                           end_session=True)

@intent(app="presentation")
def Terminology(session):
    """
    ---
    terminology is so important
    """
    message = "Terminology is very important because when we say, utterance, and you get a mental picture of rinseing a cows utter... we are going to have a problem."
    return ResponseBuilder.create_response(message=message,
                                           end_session=True)
