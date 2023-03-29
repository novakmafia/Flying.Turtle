import nextcord
import requests
import sys
sys.path.insert(1, "C:\\Users\\posei\\OneDrive\\Документы\\BOT")
from nextcord.ext import commands
from config import settings
from config import links
from config import image
from PIL import Image
import os
from select_role import SelectSTRP
from samp_client.client import SampClient

class StartBot(commands.Bot):
    def __init__(self):
        intents = nextcord.Intents.all()
        intents.message_content = True
        super().__init__(command_prefix=commands.when_mentioned_or(settings['prefix']), intents=intents)

    async def on_ready(self):
        h1 = requests.head(url='http://check.santrope-rp.com')
        h2 = requests.head(url='http://80.66.71.48')
        h3 = requests.head(url='http://80.66.71.49')
        self.add_view(view=SelectSTRP(), message_id=1076398513665097788)
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=settings['drp']), status=nextcord.Status.idle)

bot = StartBot()
bot.remove_command('help')

@bot.event
async def on_message(message):
    if message.channel.name == "「📢」новости":
        channel = bot.get_channel(int("959930633939984434"))
        thread = await channel.create_thread(name='Комментарии', message=message, auto_archive_duration=1440, type=nextcord.ChannelType.public_thread, reason="Added a thread to people can write comments")
        await thread.send("Обратите внимание, что в данной ветке действуют такие же правила, как и на обычные каналы!")
        await message.add_reaction(emoji="<:santrope_bs_like:994679420054949889>")
        await message.add_reaction(emoji="<:santrope_bs_dislike:994679418192662578>")
    elif message.channel.name == "「📻」мастерская":
        channel = bot.get_channel(int("906633755874189322"))
        thread = await channel.create_thread(name='Комментарии', message=message, auto_archive_duration=1440, type=nextcord.ChannelType.public_thread, reason="Added a thread to people can write comments")
        await thread.send("Обратите внимание, что в данной ветке действуют такие же правила, как и на обычные каналы!")
        await message.add_reaction(emoji="<:santrope_bs_like:994679420054949889>")
        await message.add_reaction(emoji="<:santrope_bs_dislike:994679418192662578>")
    else:
        await bot.process_commands(message)

@bot.command()
async def ку(ctx):
    await ctx.reply(file=nextcord.File(r"C:\Users\posei\OneDrive\Документы\BOT\1676705615678.png"))

@bot.command(pass_context=True)
async def addrole(ctx, role: nextcord.Role, member: nextcord.Member=None):
    if ctx.message.author.id == 788044062614749190:
        member = member or ctx.message.author
        assert isinstance(role, nextcord.Role)
        await member.add_roles(role)
        await ctx.reply('+')

@bot.command(name='say')
async def say(ctx, *, msg=None):
    if ctx.message.author.guild_permissions.administrator or ctx.message.author.id == 788044062614749190:
        if msg is not None or len(ctx.message.attachments) > 0:
            await ctx.message.delete()
            if len(ctx.message.attachments) > 0:
                img = Image.open(requests.get(ctx.message.attachments[0].url, stream=True).raw)
                img.save('example.png')
                await ctx.send(msg, file=nextcord.File('example.png'))
                os.remove('example.png')
            else:
                await ctx.send(msg)
        else:
            await ctx.reply("[Error]: Невозможно отправить пустоту!")
    else:
        await ctx.reply("[Error]: У Вас отсутствует доступ администратора этого Discord сервера для выполнения данного действия.")


@bot.command()
@commands.has_permissions(administrator=True)
async def reaction(ctx):
    embed = nextcord.Embed(
        description = '> - Для получения роли вашего сервера Вам нужно выбрать его в интерактивном меню, которое находится ниже.',
        colour = nextcord.Colour.from_rgb(251, 206, 177)
    )
    embed.set_author(
        name = '・Система выдачи авто-ролей:',
        icon_url = image['logo']
    )
    embed.set_thumbnail(
        url=image['p_logo']
    )
    await ctx.send(embed=embed, view=SelectSTRP())
    await ctx.message.delete()

@bot.slash_command(description='Понг!')
async def ping(interaction: nextcord.Interaction):
    embed = nextcord.Embed(
        description=f'Discord Bot ⇒ `{bot.latency * 1000:.2f}ms`',
        colour = nextcord.Colour.from_rgb(251, 206, 177)
    )
    embed.set_author(
        name='・pong!🏓',
        icon_url = image['logo']
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.slash_command(description='Ссылка на этот сервер')
async def link(interaction: nextcord.Interaction):
    await interaction.response.send_message(links['discord_short'])

@bot.slash_command(description="Узнать онлайн проекта")
async def online(interaction: nextcord.Interaction):
    all_players = 0
    max_players = 0
    embed = nextcord.Embed(
        colour = nextcord.Colour.from_rgb(251, 206, 177)
    )
    embed.set_author(
        name = '・Онлайн серверов проекта:',
        icon_url = image['p_logo']
    )
    for i in range(4, 10):
        with SampClient(address=f'80.66.71.4{str(i)}', port=5125) as client:
            info = client.get_server_info()
        embed.add_field(name=f'**{info.hostname}**', value=f'Онлайн: {info.players}/{info.max_players}')
        all_players += int(info.players)
        max_players += int(info.max_players)
    embed.set_footer(text=f'・Общий онлайн всех серверов: {all_players}/{max_players}')
    await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.slash_command(description="Ссылки на ресурсы проекта")
async def invite(interaction: nextcord.Interaction):
    embed = nextcord.Embed(
        colour = nextcord.Colour.from_rgb(251, 206, 177)
    )
    embed.add_field(name='**`DISCORD`**', value=links['discord'], inline=True)
    embed.add_field(name='**`FORUM`**', value=links['forum'], inline=True)
    embed.add_field(name='**`Telegram`**', value=links['tg'], inline=True)
    embed.add_field(name='**`Support`**', value=links['tp'], inline=True)
    embed.add_field(name='**`VK`**', value=links['vk'], inline=True)
    embed.add_field(name='**`Partner`**', value=links['partner'], inline=True)

    embed.set_author(
        name = '・Официальные ресурсы проекта:',
        icon_url = image['logo']
    )
    embed.set_thumbnail(
        url = image['p_logo']
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.command(name='ip')
async def ip(ctx, *, ip=None):
    if ip is not None:
        response = requests.get(f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,zip,lat,lon,timezone,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=ru')
        data = response.json()
        if data["status"] == "success":
            embed = nextcord.Embed(
                description = f'> **IP:** {data["query"]}\n> **Город:** {data["city"]}\n> **Регион:** {data["regionName"]}\n> **Страна:** {data["country"]}\n> **Провайдер:** {data["as"]}\n> **Proxy:** {data["proxy"]} | **Mobile:** {data["mobile"]} | **Hosting:** {data["hosting"]}\n**`Прочая информация:`**\n> **Временная зона:** {data["timezone"]}\n> **Код страны:** {data["countryCode"]}\n> **Валюта:** {data["currency"]}\n> **Континент:** {data["continent"]} ({data["continentCode"]})',
                colour = nextcord.Colour.from_rgb(251, 206, 177)
            )
            embed.set_author(
                name = '・Информация об IP:',
                icon_url = image['logo']
            )
            embed.set_footer(
                text=f"・Информацию запросил: {ctx.author.name}#{ctx.author.discriminator}"
            )
            await ctx.message.delete()
            await ctx.send(embed=embed)
        else:
            await ctx.reply(f"[Error]: {data['message']}")
    else:
        await ctx.reply("[Error]: Вы не ввели IP адрес!")

bot.run(settings['token'])