import discord.ext
from discord.ext.commands import bot

client = discord.ext.commands.Bot(command_prefix="bl.")


@client.command()
async def hi(ctx):
    await ctx.send(f'{ctx.message.author.mention}, Привет!')


@client.command()
async def helps(ctx):
    await ctx.send(
        'Я бот, да ты и сам знаешь.\n**Мои команды:**\n```!привет - Вывод сообщения с приветом.``` ```!хелп - эта '
        'команда.```')


@client.command()
async def print(ctx, *, text, var=None):
    await ctx.send(f'{text}')


@client.command()
async def ping(ctx):
    await ctx.send(f'{ctx.message.author.mention}, pong')


@client.command()
async def gay(ctx):
    await ctx.send(f'{ctx.message.author.mention}, сам gay')


def restart_program(pass_contex):
    pass


@client.command()
async def restart(ctx):
    restart_program(pass_contex)
    await ctx.send(f'{ctx.message.author.mention}, I am successfull restarted')


client.run('OTMzNDI1MzAzMjkwNzczNTA0.YehWDg.kfV4q_E8MCyq_FvxYJkCB9ysbKw')
