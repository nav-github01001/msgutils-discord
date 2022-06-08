from typing import Union
from .discord import *
from .slack import *

HAS_DISCORD: bool = None
HAS_SLACK: bool = None
try:
    from discord import Embed

    HAS_DISCORD = True
except:
    HAS_DISCORD = False

try:
    import slacksdk

    HAS_SLACK = True
except:
    HAS_SLACK = False


class MsgIPC:
    def __init__(self, ipcclass: Union[DiscordIPC, SlackIPC]):
        if HAS_DISCORD == False and isinstance(ipcclass, DiscordIPC):
            pass
