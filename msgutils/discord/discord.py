# This does refer to the library
from ..global_exception import *
try: 
    import discord
except:
    raise DiscordpyNotFound

class ParsedDiscordEmbed(discord.Embed):
    ...