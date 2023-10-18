from re import A
import discord
import os
import requests
import json
from datetime import datetime
import random
from discord.ext import commands,tasks
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)
green = []
yellow = []
green2 = ["X","X","X","X","X"]
yellow2 = ["X","X","X","X","X"]
answer = "Hello"
a = ["start"]
allot = ["a"]
data = requests.get("https://random-words-api.vercel.app/word").json()
def hex(a):
  hexa = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
  ansswer = []
  zamn = int(a)
  result = zamn
  remainder = zamn
  while result != 0:
    remainder = result%16
    result = result//16
    ansswer.insert(0,hexa[remainder])
  return ansswer

def generate():
    word = 'hi'
    while(len(word)!=5):
      data = requests.get("https://random-words-api.vercel.app/word").json()
      word = (data[0]["word"]).lower()
      
    print(word)
    return word
client = discord.Client(intents=discord.Intents.default())
def generation():
  with open(r'words.txt') as f:
    line = f.readline()
    while line:
        line = f.readline()
        a.append(line.lower())
  
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
def discount(a,b,c):
    familycount = 0
    at = 0
    ct = 0
    st = 0
    g = 0
    if((a+b) * 2 < c):
      return "INVALID"
    while (a>1 and c>2) :
        familycount +=1
        a -= 2
        c -= 3
    while (a>0 and b>0 and (b+a) >1 and c>2):
        familycount +=1
        a-=1
        b-=1
        c-=3
    while (b>1 and c>2) :
        familycount +=1
        b -= 2
        c -= 3
   
    print(a,b,c)
    if(a+b+c>= 6):
      print("group")
      g += 1
    else:
      at += a
      st += b
      ct += c
    return (familycount,at,st,ct,g)
def Convert(a):
    list1=[]
    list1[:0]=a
    return list1
def dashboard(day):
  homie = []
  jaree = ["EC203,EN203,HI203,WB708,SC205","EC203,MA201,HI203,EN203,CS201","a","b","c","d"]
  return jaree[day]
    
def wordle(a):
  green2 = ["X","X","X","X","X"]
  yellow2 = ["X","X","X","X","X"]
  green = []
  yellow = []
  z = allot[0]
  print(a)
  guess = Convert(a)
  for n in range (0,5):
    if (z[n] == guess[n]):
      green.append(n)
  for i in range (0,5):
    for n in range(0,5):
      if (z[i] == guess[n]):
        yellow.append(n)
        break;
  print(yellow,green)
  for i in range (0,5):
    try:  
      yellow2[yellow[i]] = "Y"  
    except IndexError:
      print("You got nothing")
  for n in range (0,5): 
    try:
      yellow2[green[n]] = "G"
    except IndexError:
      print("nothing")
  if (yellow2 == ["G","G","G","G","G"]):
    return " YOU WIN "
  return(yellow2)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  if message.content.startswith('$'):
      x = message.content
      z = x.replace("$","")
      print(z)
      adult = int(z[0])
      senior = int(z[1])
      child = int(z[2])
      print(child)
      price = discount(adult,senior,child)
      print(price)
      
      await message.channel.send(price)
  if message.content.startswith('wordle'):
    green = [0]
    yellow = [0] 
    x = message.content
    z = x.replace("wordle","")
    generation()
    answer = (a[random.randint(0,662)])
    allot.pop(0)
    allot.append(answer)
    print(answer) 
  if message.content.startswith("guess"):
    x = message.content
    y = x.replace("guess","")
    z = y.strip()

    print(z)
    answer = wordle(z)
    await message.channel.send(answer)
  if message.content.startswith("math"):
    await message.channel.send("θζηπ∫√∝°")
  if message.content.startswith("hex"):
    x = message.content
    y = x.replace("hex","")
    z = y.strip()
    answer = hex(z)
    await message.channel.send(answer)
  if message.content.startswith("dash"):
    

    asda = (datetime.today().weekday())
    await message.chennel.send(dashboard(asda ))
    
@bot.command()
async def play(ctx, url : str):
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  await voiceChannel.connect()
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()  

#client.run(os.environ['BOT_TOKEN'])
client.run("OTQwODAzMzY0MDIxNzYwMDQ1.YgMtaQ.4TjtEZn04ktuJYInH2tS9-3757g")