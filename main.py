import discord
from discord.ext import commands
import json

# Load configuration from config.json
with open('config.json', 'r') as f:
  config = json.load(f)

# Initialize bot
intents = discord.Intents.all()  
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionary to store points
points = {}


# Function to save points to file
def save_points():
  with open('points.json', 'w') as f:
    json.dump(points, f)


# Load points from file
def load_points():
  global points
  try:
    with open('points.json', 'r') as f:
      points = json.load(f)
  except FileNotFoundError:
    print("Points file not found, starting with empty points.")
    points = {}


# Event: When bot is ready
@bot.event
async def on_ready():
  print('Logged in as', bot.user.name)
  load_points()



# Event: When a message is sent
@bot.event
async def on_message(message):
  # Check if the message is sent in the "success" channel and contains an attachment
  if message.channel.name == config['success_channel'] and message.author.name != bot.user.name:
    member_name = message.author.name
    points[member_name] = points.get(member_name, 0) + 10
    save_points()
    await message.channel.send(
        f" 🪙 10 POINTS ADDED <@{message.author.id}> ! Your message here "
    )
    print(f"Added 10 points to<@{message.author.id}> ")

  if message.content.startswith('!leaderboard'):
    try:
      sorted_points = sorted(points.items(), key=lambda x: x[1], reverse=True)
      leaderboard_str = "Leaderboard:\n"
      for idx, (member_name, point) in enumerate(sorted_points, start=1):
        leaderboard_str += f"{idx}. <@!{member_name}>: {point} points\n"
      await message.channel.send(leaderboard_str)
      print("I was here")
    except Exception as e:
      await message.channel.send(f"An error occurred: {e}")
  await bot.process_commands(message)


# Run the bot
bot.run(config['token'])
