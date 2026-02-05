import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
    print("Bot Online!!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1375858712731844699)
    if channel:
        emmbed = discord.Embed(
            title = ' ‎ ꕁ・Welcome to the Phantom Troupe! ‎ ꕁ・',
            description = f"| ⩇⩇・Hi new members, {member.mention}\n| ⩇⩇・nice to meet u",
            color = 0xec407a 
        )
        emmbed.set_image(url="https://media.tenor.com/_YgGGcfe-3IAAAAM/chrollo-lucilfer-chrollo-hxh.gif")
        await channel.send(embed=emmbed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1468880194352709768)
    if channel:
        emmbed = discord.Embed(
            title = 'Ba Bye!',
            description = f"| ⩇⩇・Good luck with the path you've chosen, {member.mention}!",
            color = 0xec407a 
        )
        emmbed.set_image(url="https://media.tenor.com/_YgGGcfe-3IAAAAM/chrollo-lucilfer-chrollo-hxh.gif")
        await channel.send(embed=emmbed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    mes = message.content
    if mes == 'ฟา':
        await message.channel.send("ฟาอ้วน")
    await bot.process_commands(message)

@bot.tree.command(name='hibot', description='Replies with Hello')
async def hellocommand(interaction: discord.Interaction):
    await interaction.response.send_message('Say Hi I am Holy bot')

@bot.tree.command(name='fa', description='บอกความลับของฟา')
async def fa_command(interaction: discord.Interaction):
    await interaction.response.send_message('ฟาอ้วน')

server_on()

bot.run(os.getenv('TOKEN'))
