class MsgUtilException(Exception):
    pass


class DiscordpyNotFound(MsgUtilException):
    ...

class SlackNotFound(MsgUtilException):
    ...