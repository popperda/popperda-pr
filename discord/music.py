import discord
import os, platform
from discord.ext import commands

from pytube import YouTube 
SAVE_PATH = r"./"

try:
    import nacl
except ImportError:
    try:
        if platform.system().lower().startswith('win'):
            os.system("pip install pynacl")
        else:
            os.system("pip3 install pynacl")
    except Exception as e:
        print("Error:", e)
        exit()
client = commands.Bot(command_prefix="!")
#@client.command()
#async def join(ctx):
#    channel = ctx.author.voice.channel
#    await channel.connect()
#@client.command()
#async def leave(ctx):
#    await ctx.voice_client.disconnect()
@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return
    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    link = url
    
    try: 
    # object creation using YouTube
    # which was imported in the beginning 
        yt = YouTube(url) 
    except: 
        print("Connection Error") #to handle exception
    yt = YouTube(url) 
    
    # get the video with the extension and
    # resolution passed in the get() function 
    
   
    stream = yt.streams.first()
    stream = yt.streams.get_audio_only()
   
    try: 
        # downloading the video 
        stream.download(SAVE_PATH, "song.mp3" )
        
    except: 
        print("Some Error!") 
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    
    voice.play(discord.FFmpegPCMAudio(r"song.mp3"))
    
@client.command()
async def replace(ctx, url : str):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.pause()
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return
   
    

    link = url
    
    try: 
    # object creation using YouTube
    # which was imported in the beginning 
        yt = YouTube(url) 
    except: 
        print("Connection Error") #to handle exception
    yt = YouTube(url) 
    
    # get the video with the extension and
    # resolution passed in the get() function 
    
   
    stream = yt.streams.first()
    stream = yt.streams.get_audio_only()
   
    try: 
        # downloading the video 
        stream.download(SAVE_PATH, "song.mp3" )
        
    except: 
        print("Some Error!") 
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    
    voice.play(discord.FFmpegPCMAudio(r"song.mp3"))
@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")
@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")
@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")



client.run(os.environ['BOT_TOKEN'])
