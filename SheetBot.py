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
--  atts
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
--  abilities
ABILITIES
-- avatar
AVATAR
--
'''
# Token the bot uses
TOKEN = "NTQ4NzA2MTEyNzM2NzIyOTQ0.D1JQvA.Y_7u1wv6Wt-iSA9J7G17WvS1JSU"  # Stores bot token. KEEP THIS PRIVATE

auth_failed = "Sheet not found. Open a sheet with the char name."

# Creating new bot object
client = commands.Bot(command_prefix=".")   # Create new client object with '.' as cmd prefix

presence = "God"    # Rich presence phrase. 'Playing' will be put before this automatically.

# List to store currently opened sheets
sheets = []

class Author:
    def auth(file_name):
        sh = None
        found = False
        for s in sheets:
            if s.char_name == file_name:
                found = True
                sh = s
                print( "Name: " + sh.char_name )
        if not found:
            print( "Sheet not found. Open a sheet with the char name." )
            return -1
        return sh

#   Stores all information for a 5e character sheet
class Sheet:

    avatar = ""
    #   Character name
    char_name = ""

    #   Dicts for information
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
        "dex": 1,
        "con": 2,
        "int": 3,
        "wis": 4,
        "cha": 5,
        "charisma": 5,
        "strength": 0,
        "wisdom": 4,
        "intelligence": 3,
        "constitution": 2,
        "dexterity": 1,

    }

    atts_dict = {
        "ac": 0,
        "tothp": 1,
        "currhp": 2,
        "speed": 3,
        "init": 4,
        "passpercep": 5,
        "profbonus": 6,
        "armorclass": 0,
        "armor_class": 0,
        "totalhp": 1,
        "total_hp": 1,
        "currenthp": 2,
        "current_hp": 2,
        "initiative": 4,
        "passiveperception": 5,
        "passive_perception": 5,
        "proficiencybonus": 6,
        "proficiency_bonus": 6
    }

    skills_dict = {
        "acrobatics": 0,
        "animalhandling": 1,
        "arcana": 2,
        "athletics": 3,
        "deception": 4,
        "history": 5,
        "insight": 6,
        "intimidation": 7,
        "investigation": 8,
        "medicine": 9,
        "nature": 10,
        "perception": 11,
        "performance": 12,
        "persuasion": 13,
        "religion": 14,
        "sleightofhand": 15,
        "stealth": 16,
        "survival": 17,
        "acro": 0,
        "animal_handling": 1
    }

    #   Arrays for storing values on a sheet-by-sheet basis
    basics = []
    info = []
    info_atts = [
        "LVL",
        "CLASS",
        "RACE",
        "SUBRACE",
        "BACKGROUND",
        "ALIGNMENT",
        "GENDER",
        "EXP"
    ]
    stats = []
    saves = []
    atts = []
    skills = []
    langs = []  #Array of strings (languages)
    weaps = []  #Array of arrays. Inner array has: [Wep name, damage, special effects]
    spells = [] #Array of arrays. Inner array: [Spell name, spell level, range, VSM, effect]
    gear = []   #Array of arrays. Inner array: [Gear name, effects]

    # Constructor. Initializes values. In the future, should check if file exists and
    # load vals if it does.
    def __init__(self, name, avatar):
        self.avatar = avatar

        self.basics = [
            None,   #Player
            name    #Name
        ]
        self.stats = [
            None,  #STR
            None,  #DEX
            None,  #CON
            None,  #INT
            None,  #WIS
            None   #CHA
        ]
        self.char_name = name
        self.saves = [
            None,  #STR
            None,  #DEX
            None,  #CON
            None,  #INT
            None,  #WIS
            None   #CHA
        ]
        self.atts = [
            None,  #AC
            None,  #TotHP
            None,  #CurrHP
            None,  #SPEED
            None,  #INIT
            None,  #PASSPERCEP
            None   #PROFBONUS
        ]
        self.skills = [
            None,  #ACRO
            None,  #ANMHAND
            None,  #ARCANA
            None,  #ATH
            None,  #DECEPT
            None,  #HIST
            None,  #INS
            None,  #INTIMI
            None,  #INVEST
            None,  #MED
            None,  #NAT
            None,  #PERCEP
            None,  #PERFORM
            None,  #PERSUA
            None,  #REL
            None,  #SLEIGHT
            None,  #STEALTH
            None   #SURV
        ]
        self.info = [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None
        ]

    def set_name(self, name):
        self.char_name = name

    def write_to_file(self):
        print()#   This problem is left as an exercise to the reader

    def read_from_file(self):
        print()#   This problem is left as an exercise to the reader


# Does something when bot goes online
@client.event
async def on_ready():
    # Changes rich presence to presence variable
    await client.change_presence(game=discord.Game(name=presence))
    # Prints ready message to console
    print("SheetBot: Ready to role(play)")


# Says a list of open character sheets
@client.command()
async def get_open(name="getopen"):
    # Checks if any sheets are open currently
    if len(sheets) > 0:
        out_str = ""
        for sh in sheets:
            out_str += sh.char_name + "\n"
        await client.say(out_str)
    else:
        await client.say("No character sheets open at this time.")


@client.command(pass_context = True)
async def open_char(ctx, char_name):
    new_sheet = Sheet(char_name, ctx.message.author.avatar_url)
    sheets.append(new_sheet)
    fi_str = char_name + ".txt"
    temp = open(fi_str, "a")
    temp.close()


@client.command()
async def get_avatar(file_name):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    await client.say(sh.avatar)


@client.command()
async def set_avatar(file_name, url):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    sh.avatar = url


@client.command()
async def add_lang(file_name, lang):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    sh.langs.append(lang)


@client.command()
async def remove_lang(file_name, lang):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    sh.langs.remove(lang)


@client.command()
async def add_weapon(file_name, w_name, damage, effects):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    out_arr = []
    out_arr.append(w_name)
    out_arr.append(damage)
    out_arr.append(effects)
    sh.weaps.append(out_arr)

@client.command()
async def get_weapons(file_name):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    out_str = ""
    for array in sh.weaps:
        out_str = f"{out_str}**{array[0]}:** Deals {array[1]} damage | Effects: {array[2]}\n"
    await client.say(out_str)

@client.command()
async def remove_weapon(file_name, w_name):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    rem = None
    for arr in sh.weaps:
        if w_name == arr[0]:
            rem = arr

    sh.weaps.remove(rem)


''''@client.command()
async def add_spell(file_name, s_name, lvl, range, comp, eff):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
'''


@client.command()
async def get_langs(file_name):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    out_str = ""
    for lang in sh.langs:
        out_str = f"{out_str}{lang} |   "
    await client.say(out_str)


@client.command()
async def set_att(file_name, a_thing, input_name):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    try:
        sh.atts[sh.atts_dict.get(a_thing.lower(), -1)] = input_name
    except:
        await client.say("Invalid data type. Choose a skill.")


@client.command()
async def get_att(file_name, a_thing):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    try:
        await client.say(sh.atts[sh.atts_dict.get(a_thing.lower(), -1)])
    except:
        await client.say("Invalid data type. Choose an attribute.")


@client.command()
async def set_skill(file_name, a_thing, input_name):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    try:
        sh.skills[sh.skills_dict.get(a_thing.lower(), -1)] = input_name
    except:
        await client.say("Invalid data type. Choose a skill.")


@client.command()
async def get_skill(file_name, a_thing):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    try:
        await client.say(sh.skills[sh.skills_dict.get(a_thing.lower(), -1)])
    except:
        await client.say("Invalid data type. Choose a skill.")


@client.command()
async def set_skills(file_name, acr, anm, arc, ath, dec, his, ins, inti, inv, med, nat, perc, perf, pers, rel, sle, ste, sur):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return

    sh.skills[0] = acr
    sh.skills[1] = anm
    sh.skills[2] = arc
    sh.skills[3] = ath
    sh.skills[4] = dec
    sh.skills[5] = his
    sh.skills[6] = ins
    sh.skills[7] = inti
    sh.skills[8] = inv
    sh.skills[9] = med
    sh.skills[10] = nat
    sh.skills[11] = perc
    sh.skills[12] = perf
    sh.skills[13] = pers
    sh.skills[14] = rel
    sh.skills[15] = sle
    sh.skills[16] = ste
    sh.skills[17] = sur


@client.command()
async def get_skills(file_name):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return

    await client.say(
        "Acrobatics: " + sh.skills[0] +
        "\nAnimal Handling:" + sh.skills[1] +
        "\nArcana: " + sh.skills[2] +
        "\nAthletics: " + sh.skills[3] +
        "\nDeception: " + sh.skills[4] +
        "\nHistory: " + sh.skills[5] +
        "\nInsight: " + sh.skills[6] +
        "\nIntimidation: " + sh.skills[7] +
        "\nInvestigation: " + sh.skills[8] +
        "\nMedicine: " + sh.skills[9] +
        "\nNature: " + sh.skills[10] +
        "\nPerception: " + sh.skills[11] +
        "\nPerformance: " + sh.skills[12] +
        "\nPersuasion: " + sh.skills[13] +
        "\nReligion: " + sh.skills[14] +
        "\nSleight of Hand: " + sh.skills[15] +
        "\nStealth: " + sh.skills[16] +
        "\nSurvival: " +sh.skills[17])

@client.command()
async def set_info(file_name, a_thing, input_name):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    try:
        sh.info[sh.info_dict.get(a_thing.lower(), -1)] = input_name
    except:
        await client.say("Invalid data type. Choose lvl, class, race, subrace, background, alignment, gender, or xp.")


@client.command()
async def set_infos(file_name, lvl, cla, race, subr, bg, align, sex, xp):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return

    sh.info[0] = lvl
    sh.info[1] = cla
    sh.info[2] = race
    sh.info[3] = subr
    sh.info[4] = bg
    sh.info[5] = align
    sh.info[6] = sex
    sh.info[7] = xp


@client.command()
async def get_infos(file_name):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return

    outstr = ""
    for e in range(0,8):
        outstr = f"{outstr}{sh.info_atts[e]}: {sh.info[e]}\n"
    await client.say(outstr)


@client.command()
async def get_info(file_name, a_thing):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    try:
        await client.say(sh.info[sh.info_dict.get(a_thing.lower(), -1)])
    except:
        await client.say("Invalid data type. Choose 1v1, class, race, subrace, background, alignment, gender, or xp.")


@client.command()
async def set_basic(file_name, a_thing, input_name):
    a = Author
    sh = a.auth(file_name)
    print(a_thing)
    print(sh.basics_dict.get(a_thing, -1))
    if sh == -1:
        await client.say(auth_failed)
        return
    try:
        sh.basics[sh.basics_dict.get(a_thing, -1)] = input_name
    except:
        await client.say("Invalid data type. Choose player or name.")
    print(input_name)


@client.command()
async def get_basic(file_name, a_thing):
    a = Author
    sh = a.auth(file_name)
    print(a_thing)
    print(sh.basics_dict.get(a_thing, -1))
    if sh == -1:
        await client.say(auth_failed)
        return
    print(sh.basics[sh.basics_dict.get(a_thing, -1)])
    try:
        await client.say(sh.basics[sh.basics_dict.get(a_thing.lower(), -1)])
    except:
        await client.say("Invalid data type. Choose player or name.")


@client.command()
async def set_basics(file_name, plyr, nm):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return
    try:
        sh.basics[sh.basics_dict.get("player")] = plyr
        sh.basics[sh.basics_dict.get("name")] = nm
    except:
        await client.say("Invalid entries.")


@client.command()
async def get_basics(file_name):
    a = Author
    sh = a.auth(file_name)
    if sh == -1:
        await client.say(auth_failed)
        return

    await client.say(f"Player: {sh.basics[0]}\nCharacter name: {sh.basics[1]}")


@client.command()
async def get_stats(file_name):
    a = Author
    sh = a.auth( file_name=file_name )
    if sh == -1:
        await client.say("Sheet not found. Open a sheet with the char name.")
        return

    out_str = ""
    for key in sh.stat_dict:
        if key == "strength":
            break
        out_str = f"{out_str}{key.upper()}: {sh.stats[sh.stat_dict.get(key)]}\n"
    await client.say(out_str)


# Set all stats for a character
@client.command()
async def set_stats(file_name, stre, dex, con, inte, wis, cha):
    a = Author
    sh = a.auth( file_name=file_name )
    if sh == -1:
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
async def get_saves(file_name):
    a = Author
    sh = a.auth( file_name=file_name )
    if sh == -1:
        await client.say("Sheet not found. Open a sheet with the char name.")
        return

    out_str = ""
    for key in sh.saves_dict:
        if key == "charisma":
            break
        out_str = f"{out_str}{key.upper()}: {sh.saves[sh.saves_dict.get(key)]}\n"
    await client.say(out_str)


# Set all stats for a character
@client.command()
async def set_saves(file_name, stre, dex, con, inte, wis, cha):
    a = Author
    sh = a.auth( file_name=file_name )
    if sh == -1:
        await client.say( "Sheet not found. Open a sheet with the char name." )
        return

    place = 0;
    try:
        sh.saves[0] = int(stre)
        place += 1
        sh.saves[1] = int(dex)
        place += 1
        sh.saves[2] = int(con)
        place += 1
        sh.saves[3] = int(inte)
        place += 1
        sh.saves[4] = int(wis)
        place += 1
        sh.saves[5] = int(cha)
    except:
        await client.say(f"Invalid score inputted at index {str(place)}")


# Sets an individual stat for a sheet
@client.command()
async def set_stat(file_name, a_score, val, name="setstat"):
    a = Author
    sh = a.auth( file_name=file_name )
    if sh == -1:
        await client.say( "Sheet not found. Open a sheet with the char name." )
        return

    a_index = sh.stat_dict.get(a_score.lower(), -1)
    print("Index: " + str(a_index))

    if a_index < 0 or a_index > 5:
        await client.say("Input invalid")
    else:
        try:
            print(sh.char_name)
            sh.stats[a_index] = int(val)
            print(sh.stats[a_index])
        except:
            await client.say("Invalid score inputted")


# Get a single statistic from a sheet
@client.command()
async def get_stat(file_name, a_score):

    a = Author
    sh = a.auth(file_name = file_name)
    if sh == -1:
        await client.say( "Sheet not found. Open a sheet with the char name." )
        return

    a_index = sh.stat_dict.get(a_score.lower(), -1)

    if a_index < 0 or a_index > 5:
        await client.say("Input invalid")
    else:
        try:
            await client.say(str(sh.stats[a_index]))
        except:
            await client.say("Print failed")


@client.command()
async def set_save(file_name, a_score, val, name="setsave"):
    a = Author
    sh = a.auth( file_name=file_name )
    if sh == -1:
        await client.say( "Sheet not found. Open a sheet with the char name." )
        return

    a_index = sh.saves_dict.get(a_score.lower(), -1)
    print("Index: " + str(a_index))

    if a_index < 0 or a_index > 5:
        await client.say("Input invalid")
    else:
        try:
            print(sh.char_name)
            sh.saves[a_index] = int(val)
            print(sh.saves[a_index])
        except:
            await client.say("Invalid score inputted")


# Get a single statistic from a sheet
@client.command()
async def get_save(file_name, a_score):

    a = Author
    sh = a.auth(file_name = file_name)
    if sh == -1:
        await client.say( "Sheet not found. Open a sheet with the char name." )
        return

    a_index = sh.saves_dict.get(a_score.lower(), -1)

    if a_index < 0 or a_index > 5:
        await client.say("Input invalid")
    else:
        try:
            await client.say(str(sh.saves[a_index]))
        except:
            await client.say("Print failed")


#   Prints a character sheet to the discord channel
@client.command()
async def print_sheet(file_name, name="printsheet"):
    sheet = open(file_name, "r")
    sheet.close()


# Rolls x y-sided dice
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

# Runs the client using the token
client.run( TOKEN )
