# This does refer to the library and its respective forks
from .exceptions import *

try:
    import discord
except:
    raise DiscordpyNotFound


class _DiscordEmbed(discord.Embed):
    """
    An parsed Embed having message attributes. Used for sending message data along with embed.
    """

    def __init__(self, data: dict, message: discord.Message):
        super().__init__(
            colour=data["colour"],
            color=data["color"],
            title=data["title"],
            type=data["type"],
            url=data["url"],
            description=data["description"],
            timestamp=data["timestamp"],
        )
        self.message = message


class DiscordIPC:
    ...
