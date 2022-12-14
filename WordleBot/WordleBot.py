import os
from dotenv import load_dotenv

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

load_dotenv()

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=',', intents=intents)

slash = SlashCommand(bot)

@slash.slash(name = "wordle")
async def _test(ctx: SlashContext):
    embed = discord.Embed(title="embed test")
    await ctx.send(content="test", embeds=[embed])

bot.run(TOKEN)