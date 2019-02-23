import discord
from discord.ext import commands
import random

'''
Template for txt files:
PLAYER
NAME
--
LVL
CLASS
RACE
SUBRACE
BG
ALIGN
SEX
XP
--
STR
DEX
CON
INT
WIS
CHA
--
SSTR
SDEX
SCON
SINT
SWIS
SCHA
--
AC
TotHP
CurrHP
SPEED
INIT
PASSPERCEP
PROFBONUS
--
ACR
ANMHAND
ARCANA
ATH
DECEPT
HIST
INS
INTIMIDATION
INVEST
MED
NAT
PERCEP
PERFORM
PERSUA
REL
SLEIGHT
STEALTH
SURV
--
LANG
--
WEAPS
--
SPELLS
--
GEAR
--
'''

TOKEN = "NTQ4NzA2MTEyNzM2NzIyOTQ0.D1JQvA.Y_7u1wv6Wt-iSA9J7G17WvS1JSU"  # Stores bot token. KEEP THIS PRIVATE
client = commands.Bot(command_prefix=",")   # Create new client object

presence = "God"    # Rich presence phrase. 'Playing' will be put before this automatically.


stat_dict = {
    "str": 0,
    "dex": 1,
    "con": 2,
    "int": 3,
    "wis": 4,
    "cha": 5,
    "strength": 0,
    "dexterity": 1,
    "constitution": 2,
    "intelligence": 3,
    "wisdom": 4,
    "charisma": 5
}

stats = [
    0, #STR     0
    0, #DEX     1
    0, #CON     2
    0, #INT     3
    0, #WIS     4
    0  #CHA     5
]

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=presence))
    print("SheetBot: Ready to roll")


@client.command()
async def set_stat(file_name, a_score, val, name="setstat"):
    a_index = stat_dict.get("a_score", -1)
    if a_index < 0 or a_index > 5:
        print("Input invalid")
    else:
        try:
            stats[a_index] = int(a_score)
        except:
            print("Invalid score inputted")



@client.command()
async def print_sheet(file_name, name="printsheet"):
    sheet = open(file_name, "r")

@client.command()
async def roll(str):
    if "d" in str:
        index = str.find("d")
        num = int(str[0:index])
        if num > 20:
            await client.say("Invalid input: Too many dice.")
            return
        sides = int(str[index+1:len(str)])
        lis = []
        outstr = ""
        for n in range(num):
            lis.append(random.randrange(1, sides+1))

        for num in lis:
            outstr += f"You rolled: **{num}**!\n"

        await client.say(outstr)
    else:
        await client.say("Invalid input! Please try again.")

client.run( TOKEN )