from discord.ext import commands
import discord
import random
import os

# This line finds the command prefix of '!' so 
# the bot can understand it is a command 
TOKEN = ''
bot = commands.Bot(command_prefix='!')

# This is a command to tell the user how to use the bot
@bot.command(name = 'karenhelp')
async def help(ctx):
    await ctx.send('Type in !katy, !kanano, or !karen to prompt the bot to post an image of a ZOC idol')
    await ctx.send('If you type the words christian or eli, the bot will also say a random phrase')

# If user prompts the word !karen
# Post image of Karen from ZOC
@bot.command(name = 'karen')
async def karen(ctx):
    channel = ctx.message.channel
    karen_dir = 'C:\\Users\\Logan\\Desktop\\Karen'
    rand_karen = random.choice(os.listdir(karen_dir))
    karen = os.path.join(karen_dir, rand_karen)
    await channel.send(file = discord.File(karen))

# If user prompts the word !katy
# Post image of Karen from ZOC
@bot.command(name ='katy')
async def katy(ctx):
    channel = ctx.message.channel
    katy_dir = 'C:\\Users\\Logan\\Desktop\\Katy'
    rand_katy = random.choice(os.listdir(katy_dir))
    katy = os.path.join(katy_dir, rand_katy)
    await channel.send(file =discord.File(katy))

# If user prompts the word !kanano
# Post image of Karen from ZOC
@bot.command(name = 'kanano')
async def kanano(ctx):
    channel = ctx.message.channel
    kanano_dir = 'C:\\Users\\Logan\\Desktop\\Kanano'
    rand_kanano = random.choice(os.listdir(kanano_dir))
    kanano = os.path.join(kanano_dir, rand_kanano)
    await channel.send(file=discord.File(kanano))

# If user prompts the word christian or eli
# Post a random phrase for those two words
@bot.event
async def on_message(message):
    content = message.content.lower()
    list_of_christian_replies = ["It's demon time :smiling_imp:",
                             "this dooooood",
                             "Christian be like: Stop it or ill kiss you!",
                             "Christian the type of dude to still play fortnite in 2020",
                             "Chrissy the GOAT"]
    
    list_of_eli_replies = ["Eli the GOAT",
                             "*Cringes*",
                             "Eli was the number 1 minecrafter in 2017 yall",
                             "Eli when we gonna link up big dawg",
                             "he's too lit"]

    if 'christian' in content and not message.author.bot:
        channel = message.channel
        await channel.send(random.choice(list_of_christian_replies))
    
    if 'eli' in content and not message.author.bot:
        channel = message.channel
        await channel.send(random.choice(list_of_eli_replies))

    await bot.process_commands(message)

bot.run(TOKEN)