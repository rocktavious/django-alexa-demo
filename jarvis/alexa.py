from __future__ import absolute_import
from random import randint
from collections import OrderedDict
from rest_framework.serializers import CharField
from django_alexa.api import fields, intent, ResponseBuilder


@intent(app="jarvis")
def LaunchRequest(session):
    message = 'Loading Jarvis. <audio src="https://alexa.rocktavious.com/static/jarvis/voice/calibrating.mp3" />'
    message += '<audio src="https://alexa.rocktavious.com/static/jarvis/voice/utilization.mp3" />'
    message += '<audio src="https://alexa.rocktavious.com/static/jarvis/voice/uploaded.mp3" />'
    reprompt = '<audio src="https://alexa.rocktavious.com/static/jarvis/voice/what_to_do.mp3" />'
    return ResponseBuilder.create_response(message=message, message_is_ssml=True,
                                           reprompt=reprompt, reprompt_is_ssml=True,
                                           end_session=False)


@intent(app="jarvis")
def HousePartyProtocol(session):
    """
    ---
    you know what to do
    """
    message = '<audio src="https://alexa.rocktavious.com/static/jarvis/voice/house_party_protocol.mp3" />'
    return ResponseBuilder.create_response(message=message, message_is_ssml=True,
                                           end_session=False,
                                           house_party=1)

@intent(app="jarvis")
def StopRequest(session):
    """
    ---
    yes
    """
    kwargs = {}
    house_party = session.get('house_party')
    if house_party:
        kwargs["message"] = '<audio src="https://alexa.rocktavious.com/static/jarvis/voice/house_party_song.mp3" />'
        kwargs["message_is_ssml"] = True
    return ResponseBuilder.create_response(**kwargs)