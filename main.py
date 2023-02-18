import nextcord
import sys
sys.path.insert(1, "C:\\Users\\posei\\OneDrive\\Документы\\BOT")
from nextcord.ext import commands
from config import settings
from config import links
from config import image
from select_role import SelectSTRP

class StartBot(commands.Bot):
    def __init__(self):
        intents = nextcord.Intents.all()
        intents.message_content = True
        super().__init__(command_prefix=commands.when_mentioned_or(settings['prefix']), intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        self.add_view(view=SelectSTRP(), message_id=1076398513665097788)
        await bot.change_presence(status=nextcord.Status.idle, activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=settings['drp']))

bot = StartBot()
bot.remove_command('help')

@bot.command()
async def ку(ctx):
    await ctx.send(file=nextcord.File(r"C:\Users\posei\OneDrive\Документы\BOT\1676705615678.png")) 

@bot.command()
async def say(ctx, message):
    await ctx.message.delete()
    if message != None:
        await ctx.send(message)
    elif message == None:
        await ctx.send("Я не умею пустоту отправлять, балбес")


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

    await interaction.response.send_message(embed=embed)

@bot.slash_command(description='Ссылка на этот сервер')
async def link(interaction: nextcord.Interaction):
    await interaction.response.send_message(links['discord_short'])

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
    await interaction.response.send_message(embed=embed)

bot.run(settings['token'])