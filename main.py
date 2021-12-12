from discord.ext import commands

bot = commands.Bot(command_prefix = "?")

bot.lava_nodes = {
  'host': 'lava.link',
  'port': 80,
  'rest_uri': 'https://lava.link:80',
  'identifier': 'MAIN',
  'password': 'anything',
  'region': 'signapore'
}

@bot.event
async def on_ready():
  print('Kart is online!')
  bot.load_extension('dismusic')
  bot.load_extension('dch')

bot.run("TOKEN")
