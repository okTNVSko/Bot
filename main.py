import discord
import json
from discord.ext import commands
import os

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

jdata['time'] = " "
with open('setting.json','w',encoding='utf8') as jfile:
    json.dump(jdata,jfile,indent=4)

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = "-", intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")
    channel = bot.get_channel(int(jdata['Clock_Channel']))
    await channel.send(f'This\'s commands is \"-\"')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'Loaded{extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'Re-Loaded{extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'Un-loaded{extension} done.')

@bot.command()
async def close_bot(ctx):
    await ctx.send(">>The bot is offline<<")
    os._exit(0)
for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(F'cmds.{Filename[:-3]}')

if __name__ == "--main__":
    pass

bot.run(jdata['Bot_IP'])