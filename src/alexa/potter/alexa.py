from __future__ import absolute_import
from random import randint
from collections import OrderedDict
from rest_framework.serializers import CharField
from django_alexa.api import fields, intent, ResponseBuilder


HOUSES = ("gryffindor", "hufflepuff", "ravenclaw", "slytherin")
# Ordered
CURSES = OrderedDict()
CURSES["The Cruciatus Curse"] = "Crucio"
CURSES["The Imperius Curse"] =  "Imperio"
CURSES["The Killing Curse"] = "Avada Kedavra"


@intent(app="hogworts")
def LaunchRequest(session):
    """
    ---
    launch
    """
    message = "Welcome to Hog warts school of witchcraft and wizardry!"
    reprompt = "What house would you like to give points to?"
    return ResponseBuilder.create_response(message=message,
                                           reprompt=reprompt,
                                           end_session=False,
                                           launched=True)


class PointsForHouseSlots(fields.AmazonSlots):
    points = fields.AmazonNumber()
    house = fields.AmazonCustom(label="HOUSE_LIST", choices=HOUSES)


@intent(app="hogworts", slots=PointsForHouseSlots)
def PointsForHouse(session, points, house):
    """
    Direct response to add points to a house
    ---
    {house}
    {points}
    {points} {house}
    {points} points {house}
    add {points} points to {house}
    give {points} points to {house}
    """
    kwargs = {}
    kwargs['launched'] = launched = session.get('launched')
    kwargs['marauder'] = marauder = session.get('marauder')
    kwargs['points'] = points = points or session.get('points')
    kwargs['house'] = house = house or session.get('house')
    if points is None:
        kwargs['message'] = "How many points?".format(house)
        kwargs["end_session"] = False
        return ResponseBuilder.create_response(**kwargs)
    if house is None:
        kwargs['message'] = "Which house?".format(points)
        kwargs["end_session"] = False
        return ResponseBuilder.create_response(**kwargs)
    if marauder:
        kwargs['message'] = "messers can not give points to houses, we lose them in the name of mischief!"
        kwargs['message'] += " {0} points removed from house {1}.".format(randint(1,10), house or HOUSES[randint(0, 3)])
        kwargs['reprompt'] = "What mischief brings you here?"
        kwargs['end_session'] = False
    else:
        if launched:
            kwargs['reprompt'] = "What house would you like to give points to?"
            kwargs['end_session'] = False
        kwargs['message'] = "{0} points added to house {1}.".format(points, house)
        kwargs.pop("house")
        kwargs.pop("points")
    return ResponseBuilder.create_response(**kwargs)


@intent(app="hogworts")
def UnforgivableCurses(session):
    """
    The 3 unforgivable curses
    ---
    What are the unforgivable curses
    """
    message = "The Unforgivable Curses are three of the most powerful and sinister spells known to the wizarding world. "
    count = 0
    for curse_name, curse_word in CURSES.items():
        count += 1
        message += " {0}. {1}. Cast by saying, {2}. ".format(str(count), curse_name, curse_word)
    return ResponseBuilder.create_response(message=message)


@intent(app="hogworts")
def MaraudersLaunchRequest(session):
    """
    ---
    i solemnly swear i am up to no good
    """
    message = "Messers Moony, Wormtail, Padfoot and Prongs are proud to present the Marauders Map!"
    reprompt = "What mischief brings you here?"
    return ResponseBuilder.create_response(message=message,
                                           reprompt=reprompt,
                                           end_session=False,
                                           marauder=True)


@intent(app="hogworts")
def MaraudersSessionEndedRequest(session):
    """
    Default End Session Intent
    ---
    mischief managed
    """
    return ResponseBuilder.create_response()
