import re
from pyrogram import filters
from root.__main__ import bot
from root import allowbw
#An a Hyper Speed Project
# List of words to filter
bad_words = [
    "fuck", "Kena", "Mairu", "Sex", "Girlfriendsex", "Mf", "Tf", "Wtf", "Ass", 
    "Boobs", "Kunji", "Punda", "Otha", "Umbu", "Coolip", "Drugs", "Saaraku", 
    "Ponnupunda", "Motherfucker", "Fucker", "Fuckers", "Pundaboys", "Sunni", 
    "MadanGowri", "AdamGaming", "Ff", "Mr", "Pundaaaa", "Omala", "Ombuu", "Ombu", 
    "Savu", "Podapunda", "Kenaaa", "cum", "creampie", "Pea", "Fuckit", "Just die",
    "bitch", "Kunjaa", "Kanja", "bothaiporul", "KenaPunda", "MairuPunda", "Omalaoli",
    "sethapunda", "Othapunda", "Enadapunda", "Sexy", "ifuckit", "pornhub", "xhamster.desi", "pornhub.com", 
    "SavuleMairupunda", "OmalaPunda", "Kunjipunda", "pundaaaaaaaaaaaaaaa", "Othaaaa", "Othaaa", "Othaa", "Ommalaa", 
    "porn", "girlnodress", "motherfuckergirls", "gay", "lesbian", "promf", "ultrasex", 
    "desi", "masterbating", "masterbate", "masterbat", "hot porn", "hot girl", "hot man", "super sex", 
    "handjob", "cock", "dick", "Thayoli", "pussy", "Fuk", "Kundi", "kunja", "kunji", "kuunju"
]

# Build a regex pattern with variations
pattern = r"\b(?:{})\b".format('|'.join(['{}(?:{})?'.format(re.escape(word), '[a-zA-Z]*' * (len(word)-1)) for word in bad_words]))
if allowbw == True:
    @bot.on_message(filters.text & filters.regex(pattern, re.IGNORECASE))
    async def remove_message(_, message):
        try:
            await message.delete()
        except Exception as e:
            print(e)
            await bot.send_message(message.chat.id, f"Error: {e}")
