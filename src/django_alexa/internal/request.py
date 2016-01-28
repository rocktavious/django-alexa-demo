

class Request(object):
    """
    Wrapper for the request data to allow for easy access of attributes
    """
    def __init__(self, request_dict):
        self.request = request_dict

    def request_type(self):
        return self.request["request"]["type"]

    def intent_name(self):
        if not "intent" in self.request["request"]:
            return None
        return self.request["request"]["intent"]["name"]

    def user_id(self):
        return self.request["session"]["user"]["userId"]

    def access_token(self):
        try:
            return self.request['session']['user']['accessToken']
        except:
            return None

    def session_id(self):
        return self.request["session"]["sessionId"]

    def get_slot_value(self, slot_name):
        try:
            return self.request["request"]["intent"]["slots"][slot_name]["value"]
        except:
            """Value not found"""
            return None

    def get_slot_names(self):
        try:
            return self.request['request']['intent']['slots'].keys()
        except:
            return []

    def get_slot_map(self):
        return {slot_name : self.get_slot_value(slot_name) for slot_name in self.get_slot_names()}