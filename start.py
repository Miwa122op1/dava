import discord
import time
from discord.ext import commands
from config import settings
print('Bot start is start')

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Привет, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def goodbuy(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Пока, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def Create(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Автор @Овайка#6703, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def what(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Как дела?, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
@bot.command()  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def op(ctx):  # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'hack admin, {author.mention}!')  # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
    await ctx.send(f'Op hack {author.mention} чтобы продолжить напишите %op1')
@bot.command()  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def op1(ctx):  # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Ваш ник?, {author.mention}!')  # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
    time.sleep(3)
    await ctx.send(f'На ваш ник была видана опка {author.mention}')
@bot.command()
async def clear( cfx, amount : int ):
    await cfx.channel.purge( limit = int(amount) )
@bot.command()
async def ban( cfx, member : discord.Member, *, reason = None, amount = 1 ):
    await cfx.channel.purge( limut = int( amount ) )

    await member.ban( reason = reason)

    await cfx.send(f'')
@clear.error
async def clear_error( cfx, error):
    if isinstance( error, command.MissingReauiredArgument ):
        await cfx.send( f'{cfx.author.name}, обязательно укажите аргумент')

    if isinstance( error, command.MissingPermissions ):
        await cfx.send( f'{cfx.author.name}, у вас не достаточно прав')
bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена