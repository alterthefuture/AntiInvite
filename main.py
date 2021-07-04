##NOTE ONLY WORKS WITH VANITY LINKS!!##
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_connect():
    print(f'Bot is running.')

@client.event
async def on_message(message):
    
  ignore_member = ['your id','another id','another one'] #put your id and other people's id you want the bot to ignore
  ignore_channel = client.get_channel(idhere) #this is the channel where the bot ignore the discord invite link
    
  if message.author.id in ignore_member:
    pass
  else:
     if message.channel is ignore_channel:
       pass
     else:
       if "discord.gg/yourserver" in message.content: #replace yourserver with your invite link
         pass
       elif "discord.gg/" in message.content:
         log_channel = client.get_channel(idhere) #this is the channel where the bot logs the message

         await message.delete()
         await message.channel.send(f"**{message.author.mention} self promoting is not allowed.**")

         embed=discord.Embed(title=f"{message.author}",description=f"**Message sent by {message.author.mention} deleted in {message.channel.mention}**\n{message.content}\n\n **Reason**\n Invite link",color=discord.Color.red(),timestamp=message.created_at)
         embed.set_footer(text=f"ID: {message.author.id}")
         embed.set_thumbnail(url=message.author.avatar_url)

         await log_channel.send(embed=embed)

client.run("token here")
