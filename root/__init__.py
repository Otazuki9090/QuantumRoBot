import os
from pyrogram import *
from pymongo import MongoClient

ROOTREPO = "https://github.com/Otazuki9090/QuantumRoBot" #Your Repo Link
prefix = [".","!","?","*","$","#","/"]
a_id = "10187126" # Your Api Id
a_hash = "ff197c0d23d7fe54c89b44ed092c1752" # Your Api Hash 
b_tok = "6843613815:AAFfQJDa1So1xAE5CPW3FB00OLhJ9A2CnbY" # Your Bot Token
STRING_SESSION = "BQCbcXYASu4PAdVn0BO-dM5UcC8v67IAMO1TWgPEO62tHghGaOsteBB-2_S6Pnhki3V6Eeh0vdssFijhY8ccYa2mJJqydZhrA8Euj54_dWOLM9kIGUs6ipjl33yD_59b8uAygByhqrGNgxpVIkTIjVAeIN04-lBmwuCY6O6wY98ywnkZn_LRguklfU-qygk2QkSO_aIeNhDjciROOincq0AdvjUiNmCY1jnvKBNGT8ACsVWnQdC2-UQz4VkX2HdrjVTJ6nkPdlJUTMaT8APAP2nPaJRKX1rV0n7jFXiI1JaVQzI1Q868ANqcldJT8azM75F1Oc2ya3dfKGgYefszQOoiefnQQgAAAAFji4RfAA"
OWN = 6568136732 #OWNERID
CHAT_S_ID = " " #supportchatid
B_NAME = "QuantumClone" #Botname
OWN_NAME = "Otazuki004" #Ownername
allowbw = True
OWN_USRNAMER = "Otazuki004" #OwnerUsername
DEV = "6916220465" #Add DEV Id
ODEV = [OWN, DEV]
B_F_N = "𝙌𝙪𝙖𝙣𝙩𝙪𝙢𝙍𝙤𝘽𝙤𝙩" #Bot Name in font
S_URL = "FutureCity005" #Support Group url
B_ID = "" #Botid
n_boot = "NO" #Do you need Boot exinternal OS? if Yes Add "YES"
data_store_id = "-1002075414845" #Add your Log group ID and Add the bot in that group 
B_US = "Hyper004Bot" # Bot Username
PRE = [".","/","$","+"]
ROOTVER = "1.0.0" #Bot Version 
#ImageSection
ST_PIC = "https://te.legra.ph/file/283f5c4ae89078521e0df.jpg" # Start Command Picture

#addclients
bot = Client("QuantumRobot", bot_token=b_tok, api_id=a_id, api_hash=a_hash, plugins=dict(root="root/plugins"))
#clientsEND

#Dont Touch This
DIR = f"{os.getcwd()}/"


