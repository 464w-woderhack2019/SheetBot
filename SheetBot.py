import discord
from discord.ext import commands
import random

'''
Template for txt files:
1       Means file has been modified previously
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
client = commands.Bot(command_prefix=".")   # Create new client object

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
    stats = [
        None,
        None,
        None,
        None,
        None,
        None
    ]
    saves = []
    nums = []
    langs = []  #Array of strings (languages)
    weaps = []  #Array of arrays. Inner array has: [Wep name, damage, special effects]
    spells = [] #Array of arrays. Inner array: [Spell name, spell level, range, VSM, effect]
    gear = []   #Array of arrays. Inner array: [Gear name, effects]

    def __init__(self, name):
        self.stats = [
            self.stats[0],  #STR
            self.stats[1],  #DEX
            self.stats[2],  #CON
            self.stats[3],  #INT
            self.stats[4],  #WIS
            self.stats[5]   #CHA
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


@client.event
async def on_error():
    print("ERROR: Unknown")


@client.command()
async def get_open(name="getopen"):
    if len(sheets) > 0:
        out_str = ""
        for sh in sheets:
            out_str += sh.char_name + "\n"
        await client.say(out_str)
    else:
        await client.say("No character sheets open at this time.")

@client.command()
async def open_char(char_name):
    new_sheet = Sheet(char_name)
    sheets.append(new_sheet)
    fi_str = char_name + ".txt"
    temp = open(fi_str, "a")
    temp.close()


@client.command()
async def get_stats(file_name):
    sh = None
    found = False

    for s in sheets:
        if s.char_name == file_name:
            print( s.char_name )
            found = True
            sh = s
    if not found:
        found = False
        await client.say( "Sheet not found. Open a sheet with the char name." )
        return
    out_str = ""
    for key in sh.stat_dict:
        if key == "strength":
            break
        out_str = f"{out_str}{key.upper()}: {sh.stats[sh.stat_dict.get(key)]}\n"
    await client.say(out_str)


@client.command()
async def set_stats(file_name, stre, dex, con, inte, wis, cha):
    sh = None
    found = False

    for s in sheets:
        if s.char_name == file_name:
            print( s.char_name )
            found = True
            sh = s
    if not found:
        found = False
        await client.say( "Sheet not found. Open a sheet with the char name." )
        return
    place = 0;
    try:
        sh.stats[0] = int(stre)
        place += 1
        sh.stats[1] = int(dex)
        place += 1
        sh.stats[2] = int(con)
        place += 1
        sh.stats[3] = int(inte)
        place += 1
        sh.stats[4] = int(wis)
        place += 1
        sh.stats[5] = int(cha)
    except:
        await client.say(f"Invalid score inputted at index {str(place)}")


@client.command()
async def set_stat(file_name, a_score, val, name="setstat"):
    sh = None
    found = False

    for s in sheets:
        if s.char_name == file_name:
            print(s.char_name)
            found = True
            sh = s
    if not found:
        found = False
        await client.say("Sheet not found. Open a sheet with the char name.")
        return
    print("AAAHHHH")
    a_index = sh.stat_dict.get(a_score.lower(), -1)
    print("Index: " + str(a_index))

    if a_index < 0 or a_index > 5:
        print("Input invalid")
    else:
        try:
            print(sh.char_name)
            sh.stats[a_index] = int(val)
            print(sh.stats[a_index])
        except:
            print("Invalid score inputted")


@client.command()
async def get_stat(file_name, a_score):
    sh = None
    found = False
    for s in sheets:
        if s.char_name == file_name:
            found = True
            sh = s
            print("Name: " + sh.char_name)
            print("Index: " + str(sh.stat_dict.get(a_score)))
            print("Val: " + str(sh.stats[sh.stat_dict.get(a_score)]))
            print("Forced val: " + str(sh.stats))
    if not found:
        await client.say("Sheet not found. Open a sheet with the char name.")
        return

    #sh = auth(file_name)   Not doing this anymore
    if sh == -1:
        return

    a_index = sh.stat_dict.get(a_score, -1)

    if a_index < 0 or a_index > 5:
        print("Input invalid")
    else:
        try:
            await client.say(str(sh.stats[a_index]))
        except:
            print("Print failed")


@client.command()
async def print_sheet(file_name, name="printsheet"):
    sheet = open(file_name, "r")
    sheet.close()

'''def auth(file_name):
    sh = None
    found = False
    for s in sheets:
        if s.char_name == file_name:
            found = True
            sh = s
            print( "Name: " + sh.char_name )
            print( "Index: " + str( sh.stat_dict.get( a_score ) ) )
            print( "Val: " + str( sh.stats[sh.stat_dict.get( a_score )] ) )
            print( "Forced val: " + str( sh.stats ) )
    if not found:
        client.say( "Sheet not found. Open a sheet with the char name." )
        return -1
    return sh'''
# Calling functions with coroutines is hard


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