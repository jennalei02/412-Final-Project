from discord.ext import commands
import discord
import psycopg2
import emojis

#psycopg2
hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'ASU412'
port_id = 5432
conn = None
cur = None
#discord
BOT_TOKEN = "MTA0ODMyNzYxNjk1Mzg0Mzc2Mw.GktaYc.wfOi5eYXwRBHUF1glmW4F3_nDpGf34zvYzpAeI"
CHANNEL_ID = 760236760411275267
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("First AM is now Online")

@bot.command()
async def hi(ctx):
    await ctx.send("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠛⠛⠛⠿⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⡀⠠⠤⠒⢂⣉⣉⣉⣑⣒⣒⠒⠒⠒⠒⠒⠒⠒⠀⠀⠐⠒⠚⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⡠⠔⠉⣀⠔⠒⠉⣀⣀⠀⠀⠀⣀⡀⠈⠉⠑⠒⠒⠒⠒⠒⠈⠉⠉⠉⠁⠂⠀⠈⠙⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠔⠁⠠⠖⠡⠔⠊⠀⠀⠀⠀⠀⠀⠀⠐⡄⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠉⠲⢄⠀⠀⠀⠈⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠊⠀⢀⣀⣤⣤⣤⣤⣀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠜⠀⠀⠀⠀⣀⡀⠀⠈⠃⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠥⠐⠂⠀⠀⠀⠀⡄⠀⠰⢺⣿⣿⣿⣿⣿⣟⠀⠈⠐⢤⠀⠀⠀⠀⠀⠀⢀⣠⣶⣾⣯⠀⠀⠉⠂⠀⠠⠤⢄⣀⠙⢿⣿⣿
⣿⡿⠋⠡⠐⠈⣉⠭⠤⠤⢄⡀⠈⠀⠈⠁⠉⠁⡠⠀⠀⠀⠉⠐⠠⠔⠀⠀⠀⠀⠀⠲⣿⠿⠛⠛⠓⠒⠂⠀⠀⠀⠀⠀⠀⠠⡉⢢⠙⣿
⣿⠀⢀⠁⠀⠊⠀⠀⠀⠀⠀⠈⠁⠒⠂⠀⠒⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⢀⣀⡠⠔⠒⠒⠂⠀⠈⠀⡇⣿
⣿⠀⢸⠀⠀⠀⢀⣀⡠⠋⠓⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠈⠢⠤⡀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⡠⠀⡇⣿
⣿⡀⠘⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠈⠑⡦⢄⣀⠀⠀⠐⠒⠁⢸⠀⠀⠠⠒⠄⠀⠀⠀⠀⠀⢀⠇⠀⣀⡀⠀⠀⢀⢾⡆⠀⠈⡀⠎⣸⣿
⣿⣿⣄⡈⠢⠀⠀⠀⠀⠘⣶⣄⡀⠀⠀⡇⠀⠀⠈⠉⠒⠢⡤⣀⡀⠀⠀⠀⠀⠀⠐⠦⠤⠒⠁⠀⠀⠀⠀⣀⢴⠁⠀⢷⠀⠀⠀⢰⣿⣿
⣿⣿⣿⣿⣇⠂⠀⠀⠀⠀⠈⢂⠀⠈⠹⡧⣀⠀⠀⠀⠀⠀⡇⠀⠀⠉⠉⠉⢱⠒⠒⠒⠒⢖⠒⠒⠂⠙⠏⠀⠘⡀⠀⢸⠀⠀⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠑⠄⠰⠀⠀⠁⠐⠲⣤⣴⣄⡀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢸⠀⠀⠀⠀⢠⠀⣠⣷⣶⣿⠀⠀⢰⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠁⢀⠀⠀⠀⠀⠀⡙⠋⠙⠓⠲⢤⣤⣷⣤⣤⣤⣤⣾⣦⣤⣤⣶⣿⣿⣿⣿⡟⢹⠀⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠑⠀⢄⠀⡰⠁⠀⠀⠀⠀⠀⠈⠉⠁⠈⠉⠻⠋⠉⠛⢛⠉⠉⢹⠁⢀⢇⠎⠀⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠈⠢⢄⡉⠂⠄⡀⠀⠈⠒⠢⠄⠀⢀⣀⣀⣰⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢀⣎⠀⠼⠊⠀⠀⠀⠘⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠉⠢⢄⡈⠑⠢⢄⡀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⢀⠀⠀⠀⠀⠀⢻⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⡈⠑⠢⢄⡀⠈⠑⠒⠤⠄⣀⣀⠀⠉⠉⠉⠉⠀⠀⠀⣀⡀⠤⠂⠁⠀⢀⠆⠀⠀⢸⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠁⠉⠒⠂⠤⠤⣀⣀⣉⡉⠉⠉⠉⠉⢀⣀⣀⡠⠤⠒⠈⠀⠀⠀⠀⣸⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣤⣤⣤⣤⣀⣀⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿""")

@bot.command()
async def playTime(ctx, userID):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(emojis.encode("Now calculating User " + userID + "'s total playtime on their playlist. (the actual music looks :thumbsdown: ) \n"))
    query = 'SELECT SUM(playTime) FROM Users, Songs, ListensTo WHERE Users.userID = ' + userID + ' AND Users.userID = ListensTo.userID AND ListensTo.songID = Songs.SongID'
    await run(ctx, query)

@bot.command()
async def songsInAlbum(ctx, albumID):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(emojis.encode("You want me to look at THAT album?! Alright... :unamused: \n"))
    query = 'SELECT songID FROM Songs, Albums WHERE Songs.albumID = Albums.albumID AND Songs.albumID = ' + albumID
    await run(ctx, query)

@bot.command()
async def songsOfArtist(ctx, artistID):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(emojis.encode("Oh dude I love this artist omg :running: :running: :running: \n"))
    query = 'SELECT songID FROM Songs, Artists WHERE Songs.artistID = Artists.artistID AND Artists.artistID = ' + artistID
    await run(ctx, query)

@bot.command()
async def userListensToArtists(ctx, userID):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(emojis.encode("thinking... calculating... crunching the numbers... :eggplant: \n"))
    query = 'WITH Table1 AS (SELECT * FROM Artists NATURAL JOIN Songs) SELECT COUNT(distinct(artistID)) from Table1, ListensTo , Users where Table1.songID =  ListensTo.songID AND ListensTo.userID = Users.userID AND Users.userID = ' + userID
    await run(ctx, query)

@bot.command()
async def userListensToAlbums(ctx, userID):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(emojis.encode(":sparkles: get new music taste, buddy :sparkles: \n"))
    query = 'SELECT COUNT(DISTINCT(Songs.albumID)) FROM Songs, Users, ListensTo WHERE Users.userID = ListensTo.userID AND ListensTo.songID = Songs.songID AND Users.userID = ' + userID
    await run(ctx, query)

@bot.command()
async def numSongsInGenre(ctx, genre):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(emojis.encode("Why didn't you just do this command yourself??? You're a full-grown college student are u srs :question: \n"))
    query = 'SELECT COUNT(DISTINCT(Songs)) FROM Songs WHERE Songs.genre = ' + "\'" + genre + "\'"
    await run(ctx, query)

@bot.command()
async def hello(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(emojis.encode(":shit: \n"))
    await ctx.send(emojis.encode(":sparkles: Hello!!!! :sparkles: "))

@bot.command()
async def updateC(ctx, someTable, varToUpdate, updateVariable, someCondition):
    someQuery = 'UPDATE ' + someTable + ' SET ' + varToUpdate + ' = ' + updateVariable + ' WHERE ' + someCondition
    print(someQuery)
    await run(ctx, someQuery)
    await ctx.send("Updated.")

@bot.command()
async def update(ctx, someTable, varToUpdate, updateVariable):
    someQuery = 'UPDATE ' + someTable + ' SET ' + varToUpdate + ' = ' + updateVariable
    print(someQuery)
    await run(ctx, someQuery)
    await ctx.send("Updated.")

@bot.command()
async def selectC(ctx, variable, table, someCondition):
    someQuery = 'SELECT ' + variable + ' FROM ' + table + ' WHERE ' + someCondition
    print(someQuery)
    await run(ctx, someQuery)

@bot.command()
async def select(ctx, variable, table):
    someQuery = 'SELECT ' + variable + ' FROM ' + table
    print(someQuery)
    await run(ctx, someQuery)

@bot.command()
async def insert(ctx, table, variable):
    someQuery = 'INSERT INTO ' + table + ' VALUES' + variable
    print(someQuery)
    await ctx.send("Your operation has ran successfully.")
    await run(ctx, someQuery)

@bot.command()
async def delete(ctx, table, condition):
    someQuery = 'DELETE FROM ' + table + ' WHERE ' + condition
    print(someQuery)
    await ctx.send("Your operation has ran successfully.")
    await run(ctx, someQuery)

@bot.event
async def on_message(message):
   if message.content == ":(":
      await message.channel.send("cry about it")
   await bot.process_commands(message)

@bot.command()
async def run(ctx, *arr):
    #await ctx.send("Please be careful with the SQL code format to allow the query to run properly.")
    for command in arr:
        try:
            conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)
            cur = conn.cursor()
            query_script = command
            cur.execute(query_script)
            if command.__contains__('INSERT'):
                await ctx.send(" :boom: No information was returned but database was modified. :boom:")
                pass
            else:
                result = cur.fetchall()
            conn.commit()
        except Exception as error:
            print(error)

        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
        if 'result' in locals():
            for data in result:
                data = list(data)
                await ctx.send(emojis.encode(":star:") + str(data) + emojis.encode(":star:"))
                print(data)

bot.run(BOT_TOKEN)