import json

class Rollcall(object):
    def __init__(self, channelid, name, users):
        self.channelid = channelid
        self.name = name
        self.users = users

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class User(object):
    def __init__(self, name, username, status, reason):
        self.name = name
        self.username = username
        self.status = status
        self.reason = reason

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
