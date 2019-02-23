import discord
from discord.ext import commands
import random

'''
Template for txt files:
--  basics
PLAYER
NAME
--  info
LVL
CLASS
RACE
SUBRACE
BG
ALIGN
SEX
XP
--  stats
STR
DEX
CON
INT
WIS
CHA
--  saves
SSTR
SDEX
SCON
SINT
SWIS
SCHA
--  nums
AC
TotHP
CurrHP
SPEED
INIT
PASSPERCEP
PROFBONUS
--  skills
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
--  langs
LANG
--  weaps
WEAPS
--  spells
SPELLS
--  gear
GEAR
--
'''

TOKEN = "NTQ4NzA2MTEyNzM2NzIyOTQ0.D1JQvA.Y_7u1wv6Wt-iSA9J7G17WvS1JSU"  # Stores bot token. KEEP THIS PRIVATE
client = commands.Bot(command_prefix=",")   # Create new client object

presence = "God"    # Rich presence phrase. 'Playing' will be put before this automatically.

sheets = []


class Sheet:

    char_name = ""
    basics_dict = {
        "player": 0,
        "name": 1,
        "charactername": 1,
        "charname": 1,
        "char_name": 1
    }
    info_dict = {
        "lvl": 0,
        "level": 0,
        "class": 1,
        "race": 2,
        "subrace": 3,
        "background": 4,
        "bg": 4,
        "alignment": 5,
        "align": 5,
        "sex": 6,
        "gend": 6,
        "gender": 6,
        "xp": 7,
        "exp": 7,
        "experience": 7
    }

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

    saves_dict = {
        "str": 0,
        "strength": 0,
        "dex": 1,
        "dexterity": 1,
        "con": 2,
        "constitution": 2,
        "int": 3,
        "intelligence": 3,
        "wis": 4,
        "wisdom": 4,
        "cha": 5,
        "charisma": 5
    }
    basics = []
    info = []
    stats = []
    saves = []
    nums = []
    langs = []  #Array of strings (languages)
    weaps = []  #Array of arrays. Inner array has: [Wep name, damage, special effects]
    spells = [] #Array of arrays. Inner array: [Spell name, spell level, range, VSM, effect]
    gear = []   #Array of arrays. Inner array: [Gear name, effects]

    def __init__(self, name):
        self.stats = [
            0,  #STR
            0,  #DEX
            0,  #CON
            0,  #INT
            0,  #WIS
            0   #CHA
        ]
        self.char_name = name
        self.saves = [
            0,  #STR
            0,  #DEX
            0,  #CON
            0,  #INT
            0,  #WIS
            0   #CHA
        ]
        self.nums = [
            0,  #AC
            0,  #TotHP
            0,  #CurrHP
            0,  #SPEED
            0,  #INIT
            0,  #PASSPERCEP
            0   #PROFBONUS
        ]
        self.skills = [
            0,  #ACRO
            0,  #ANMHAND
            0,  #ARCANA
            0,  #ATH
            0,  #DECEPT
            0,  #HIST
            0,  #INS
            0,  #INTIMI
            0,  #INVEST
            0,  #MED
            0,  #NAT
            0,  #PERCEP
            0,  #PERFORM
            0,  #PERSUA
            0,  #REL
            0,  #SLEIGHT
            0,  #STEALTH
            0   #SURV
        ]

    def set_name(self, name):
        self.char_name = name

    def write_to_file(self):
        print()#   This problem is left as an exercise to the reader

    def read_from_file(self):
        print()#   This problem is left as an exercise to the reader


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=presence))
    print("SheetBot: Ready to role(play)")


@client.command()
async def get_open(name="getopen"):
    if len(sheets) > 0:
        for sh in sheets:
            await client.say(sh.char_name)


@client.command()
async def open_char(char_name):
    new_sheet = Sheet(char_name)
    sheets.append(new_sheet)
    fi_str = char_name + ".txt"
    temp = open(fi_str, "w")
    temp.write("ah")
    temp.close()


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