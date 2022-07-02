# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
# A Powerful Music And Management Bot
# Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @PravarNOTfound
# Owner PravarNotFound
# Roses are red, Violets are blue, A face like yours, Belongs in a zoo


import json
import os



def get_user_list(config, key):
    with open('{}/RocksAlexaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 12581410  # integer value, dont use ""
    API_HASH = "150997c7d6077320f71275ef4ad1ebe4"
    TOKEN = "5426231440:AAFBfEZMhc-Wqq59PcpDPfRYfIU2d2MwTVA"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5548097102  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "hckur"
    STRING_SESSION = '1AZWarzkBu2L1VxbjeDpyTmjFzxfCTBVODC3Of64gsp4FltWsiGqytamCd_qDhjq-kBH7eFOdAAVl1T2hhSeuyv0Imn_OHSzItqar60oA9WKhnx87h7crO0HdUQPIOZQRERvGi5nfZS8nfpBMmEtdAZixHx-Q60aiwBDxnAZPb3sRePqNPJash6wbM-JpZo6egHvHFF1yHO3R6It271sJX1Am-Hl6W2YUaNB6kwS8Sj2KWovNFJnoHSaxw4aFrln37bCMB7Bsj7GXFngVkf6xd_0gvolXsHhSEajCzm0rjfL7BwlMKhSct8F3GcTOvLfWsdDHPN3OroPX3mgeklUIjTvdYa6VfLY='
    SUPPORT_CHAT = 'TheNoobHacker'  #Your own group for support, do not add the @
    UPDATES_CHANNEL = 'TheNoobHacker' #Your own channel for Updates of bot, Do not add @
    JOIN_LOGGER = -1001674647560  #Prints any new group the bot is added to, prints just the name and ID.
    REM_BG_API_KEY = "http://removebg.com"
    TEMP_DOWNLOAD_DIRECTORY = ""
    EVENT_LOGS = -1001674647560  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    SQLALCHEMY_DATABASE_URI = '' #do you hub your old heroku app database_URL then put here, most use 25days ago sql
    LOAD = [] #try to kang this db ur big mothersfuckers i know your noob so only kanging my db
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = None
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "pzpO~zXWjQ4_DRNB02DOY0VhJ95mCbtYZvuqBOKmKGilFkYkgTTLSYXTw2q0OgQt"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    BOT_USERNAME = "OliviaCuteBot"
    MONGO_DB_URI = "mongodb+srv://Pravar123:standoff2@cluster0.7s4xy.mongodb.net/?retryWrites=true&w=majority"
    BOT_ID = "5426231440"
    
    DRAGONS = get_user_list('elevated_users.json', 'sudos')

    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    STRICT_GMUTE = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    ARQ_API_URL = "https://thearq.tech"
    ARQ_API_KEY = "GKNOHX-UDSREJ-AWTSGO-XFDSCY-ARQ"
    CASH_API_KEY = 'awoo'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'awoo'  # Get your API key from https://timezonedb.com/api
    OPENWEATHERMAP_ID = 'awoo'
    WALL_API = 'awoo'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = 'awoo'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

