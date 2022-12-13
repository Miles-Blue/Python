import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

from discord_slash import SlashContext, SlashCommand

import random_word

load_dotenv()

TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix = commands.when_mentioned_or('!'))

slash = SlashCommand(client)

@slash.slash(
    name="wordle",
    description="Starts a game of wordle"
)

async def _wordle(ctx: SlashContext):
    r = randomword.RandomWords()
    new_word = r.get_random_word(
        minLength=5,
        maxLength=5
    ).lower()
    
    await ctx.send("Thanks for starting a game of wordle! Make a guess!")
    
    def check(m):
        return m.channel == ctx.channel and m.author == ctx.author

client.run(TOKEN)