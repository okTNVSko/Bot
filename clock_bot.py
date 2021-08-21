import json
import time
import asyncio
import datetime
from discord.ext import commands
from classes.classes import Cog_Extension

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
def jsfile():
    with open('setting.json', mode='r', encoding='utf8') as jfile:
        jdata = json.load(jfile)
    return int(jdata['Clock_Channel'])

class Clock(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.counter = 0
        self.txt = ''
        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(jsfile())
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%m%d%H%M')
                with open('setting.json', mode='r', encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if now_time == jdata['time'] and self.counter == 0:
                    self.counter = 1
                    await self.channel.send(self.txt)
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def now(self,ctx):
        await ctx.send(f"Now is {datetime.datetime.now().strftime('%Y %m %d %A %H:%M:%S')}")

    @commands.command()
    async def Alarm(self, ctx, time:str, txt=''):
        self.counter = 0
        if txt=='':
            self.txt = 'Time\'s up'
        else:
            self.txt = txt
        with open('setting.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        sum = len(time)
        if sum == 4:
            jdata['time'] = datetime.datetime.now().strftime('%m%d')+time
        elif sum==6:
            jdata['time'] = datetime.datetime.now().strftime('%m') + time
        with open('setting.json', 'w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=8)
def setup(clock_bot):
    clock_bot.add_cog(Clock(clock_bot))

    #f(x) = 8-strlong