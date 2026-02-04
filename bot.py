import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Bot Online!!")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1375858712731844699)

    emmbed = discord.Embed(title = 'Welcome to the Phantom Troupe!' ,                     
                        description = f"| ⩇⩇・Hi new members, {member.mention}!",
                        color = 0xec407a )
    emmbed.set_image(url="https://media.tenor.com/_YgGGcfe-3IAAAAM/chrollo-lucilfer-chrollo-hxh.gif")

    await channel.send(content=text, embed=emmbed)
    #await member.send(text)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1375858712731844699)
    text = f"{member.mention} Ba Bye My Bro!"
    await channel.send(text)

@bot.event
async def on_message(message):
   mes = message.content
   if mes == 'ฟา':
      await message.channel.send("ฟาอ้วน")

@bot.tree.command(name='hibot' ,description='Replies with Hello')
async def hellocommand(interaction):
    await interaction.response.send_message('Say Hi I am Holy bot')


server_on()

bot.run(os.getenv('TOKEN'))
