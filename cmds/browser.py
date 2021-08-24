from discord.ext import commands
from classes.classes import Cog_Extension
import googletrans as GS
import webbrowser as wb
import json

class Browser(Cog_Extension):

    @commands.command()
    async def google(self, ctx,*,search_value=""):
        if len(search_value):
            wb.get("windows-default").open("https://www.google.com/search?q=" + search_value)
        else:
            wb.get("windows-default").open("https://www.google.com")

    @commands.command()
    async def 翻譯(self,ctx,txt="",lang="zh-tw"):
        self.translator = GS.Translator()
        self.result = self.translator.translate(txt,dest=lang)
        await ctx.send(self.result.text)

    @commands.command()
    async def 翻譯使用教學(self,ctx):
        self.translate_txt = open('translate.txt', 'r')
        await ctx.send(self.translate_txt.read())
        self.translate_txt.close()

    @commands.command()
    async def add_url(self,ctx,name:str,url):
        with open('save_url.json', mode='r', encoding='utf8') as url_file:
            url_data = json.load(url_file)
        url_data[name] = url
        with open('save_url.json', 'w',encoding='utf8') as url_file:
            json.dump(url_data,url_file,ensure_ascii=False)

    @commands.command()
    async def 我的最愛(self,ctx,name:str):

        with open('save_url.json', mode='r', encoding='utf8') as url_file:
            url_data = json.load(url_file)
        if (name in url_data):
            wb.get("windows-default").open(url_data[name])
        else:
            await ctx.send(f"{name} 不在我的最愛裡面 ")

    @commands.command()
    async def pop_url(self,ctx,name:str):
        with open('save_url.json', mode='r', encoding='utf8') as url_file:
            url_data = json.load(url_file)
            if (name in url_data):
                del url_data[name]
                await ctx.send(f"移除成功")
            else:
                await ctx.send(f"移除失敗")
        with open('save_url.json', 'w',encoding='utf8') as url_file:
            json.dump(url_data,url_file,ensure_ascii=False)
def setup(browser):
    browser.add_cog(Browser(browser))