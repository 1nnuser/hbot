import discord
from discord.ext import commands
import asyncio
from discord.ext.commands import MissingRequiredArgument, BadArgument
from config import PREFIX



class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx):
        emb = discord.Embed (title = ':clipboard: Навигация по командам.', color = 0x000000)
        emb.add_field(name ='Хентай 18+', value = '`bdsm`, `anal`, `leg`, `ahageo`, `bigass`, `bigtits`, `bikini`, `demon`, `elves`, `furry`, `stocking`, `angel`, `hmaid`, `mastur`, `monster`, `neko`, `police`, `pussy`, `smalltits`, `sport`, `tentacles`, `titsjob`, `yaoy`, `uri`', inline= False)
        emb.add_field(name ='Автопубликация.', value = '`auto`', inline= False)
        emb.add_field(name ='Прочее', value = '`invite`, `support`, `about`, `bag`', inline= False)
        emb.description ='**Бот находится в тест режиме! Мы стараемся постепенно улучшать его!**'
        emb.set_footer(text= 'Пригласи меня к себе! h!invite')
        await ctx.send(embed = emb)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def invite(self, ctx):
        emb = discord.Embed (title='📢 Пригласи бота к себе на сервер!', color = 0x000000)
        emb.add_field(name ='Инвайт ссылка на бота:', value = '[Пригласить бота (клик)](https://discord.com/oauth2/authorize?client_id=772542142986846288&permissions=359642&scope=bot)', inline= False)
        await ctx.send(embed = emb)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def support(self, ctx):
        emb = discord.Embed (title='📢 Тех. сервер!', color = 0x000000)
        emb.add_field(name ='Инвайт ссылка на тех. сервер:', value = '[Сервер (клик)](https://discord.gg/tD2QYkUs8N)', inline= False)
        await ctx.send(embed = emb)


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def piar(self, ctx):
        emb = discord.Embed (color = 0xFFFAFA)
        emb.description = f'**Закажи рекламу своего контента!**\n `Более 1000+ серверов`\nДля заказа рекламы перейдите на наш тех. сервер. [Тех. сервер (кликабельно)](https://discord.gg/tD2QYkUs8N)'
        await ctx.send(embed = emb)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def about(self, ctx):
        guild_count = len(self.client.guilds)

        embed = discord.Embed(title="**Hbot Info**", color= 0x000000)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(name="Создатель:", value="`Fmeme#0120`", inline=False)
        embed.add_field(name="Сервера:", value= '`{}`'.format(guild_count), inline=False)
        embed.add_field(name="Каналов:", value= '`{}`'.format(len(list(self.client.get_all_channels()))), inline=False)
        embed.add_field(name="Бот создан:", value='`1 нояб. 2020 г.`', inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def bag(self, ctx, *, arg):
        channel = self.client.get_channel(int(789401803942002718))
        embed2 = discord.Embed(title="Новый баг!", color = 0x000000)
        embed2.add_field(name="О баге:", value= arg, inline=False)
        await channel.send(embed = embed2)


    @support.error
    async def support_error(self, ctx, error):
        embed = discord.Embed(title = '🔔 Ошибка.', color = 0xDC143C)
        embed.description = 'Бот имеет **задержку**, пожалуйста, подождите {} сек.'.format(int(error.retry_after))
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed = embed)

    @help.error
    async def help_error(self, ctx, error):
        embed = discord.Embed(title = '🔔 Ошибка.', color = 0xDC143C)
        embed.description = 'Бот имеет **задержку**, пожалуйста, подождите {} сек.'.format(int(error.retry_after))
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed = embed)

    @invite.error
    async def invite_error(self, ctx, error):
        embed = discord.Embed(title = '🔔 Ошибка.', color = 0xDC143C)
        embed.description = 'Бот имеет **задержку**, пожалуйста, подождите {} сек.'.format(int(error.retry_after))
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed = embed)

    @bag.error
    async def bag_error(self, ctx, error):
        embed0 = discord.Embed(title = '🔔 Ошибка.', color = 0xDC143C)
        embed0.description = 'Бот имеет **задержку**, пожалуйста, подождите **несколько** сек.'

        embed1= discord.Embed(title = '🔔 Ошибка.', color = 0xDC143C)
        embed1.description = 'Вы не описали **баг!**'

        if isinstance(error, MissingRequiredArgument):
            await ctx.send(embed = embed1)
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed = embed0)
   




def setup(client):
    client.add_cog(Help(client))
