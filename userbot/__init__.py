import asyncio
import logging
import os
import sys
import time
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
import wget
import pylast
from antispaminc.connect import Connect
from dotenv import load_dotenv
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from requests import get
from telethon import TelegramClient
from telethon.sessions import StringSession

from userbot.thunderconfig import Config
from var import Var

from .function import thunderfunction as topfunc

StartTime = time.time()
telever = "5.0"

Lastupdate = time.time()
sed = logging.getLogger("WARNING")
sedprint = logging.getLogger("WARNING")
CMD_HNDLR = Config.CMD_HNDLR

if Var.STRING_SESSION:
    session_name = str(Var.STRING_SESSION)
    bot = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)



INT_PLUG = ""
LOAD_PLUG = {}
COOL_CMD = {}
# PaperPlaneExtended Support Vars
ENV = os.environ.get("ENV", False)
""" PPE initialization. """



# Bot Logs setup:
if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
        )
    LOGS = getLogger(__name__)

    # Check if the config was edited by using the already used variable.
    # Basically, its the 'virginity check' for the config file ;)
    CONFIG_CHECK = os.environ.get(
        "___________PLOX_______REMOVE_____THIS_____LINE__________", None
    )

    if CONFIG_CHECK:
        LOGS.info(
            "Please remove the line mentioned in the first hashtag from the config.env file"
        )
        quit(1)

    # Logging channel/group configuration.
    BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
    try:
        BOTLOG_CHATID = int(BOTLOG_CHATID)
    except:
        pass

    # Userbot logging feature switch.
    BOTLOG = sb(os.environ.get("BOTLOG", "True"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "True"))

    # Bleep Blop, this is a bot ;)
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "True"))

    # Console verbose logging
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    # SQL Database URI
    DB_URI = os.environ.get("DATABASE_URL", None)

    # OCR API key
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

    # remove.bg API key
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

    # Chrome Driver and Headless Google Chrome Binaries
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

    # OpenWeatherMap API Key
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)

    # Anti Spambot Config
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))

    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

    # FedBan Premium Module
    F_BAN_LOGGER_GROUP = os.environ.get("F_BAN_LOGGER_GROUP", None)

    # Autopic
    AUTOPIC_FONT_COLOUR = os.environ.get("AUTOPIC_FONT_COLOUR", None)
    AUTOPIC_FONT = os.environ.get("AUTOPIC_FONT", None)
    AUTOPIC_COMMENT = os.environ.get("AUTOPIC_COMMENT", None)

    # Cbutton
    PRIVATE_CHANNEL_BOT_API_ID = os.environ.get("PRIVATE_CHANNEL_BOT_API_ID", None)

    # SUDOUSERS
    SUDO_USERS = os.environ.get("SUDO_USERS", None)

    # CommandHandler
    CMD_HNDLR = os.environ.get("CMD_HNDLR", "\.")
    SUDO_HNDLR = os.environ.get("SUDO_HNDLR", "\!")

    # Heroku Credentials for updater.
    HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

    # Youtube API key
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

    # Default .alive name
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    AUTONAME = os.environ.get("AUTONAME", None)
    
    # Personal Info
    YT_NAME = os.environ.get("YT_NAME", None)
    YT_NAME = os.environ.get("YT_NAME", None)
    YT_LINK = os.environ.get("YT_LINK", None)
    TG_GRUP = os.environ.get("TG_GRUP", None)
    TG_CHANNEL = os.environ.get("TG_CHANNEL", None)


    # Custom pm permi
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
    # Time & Date - Country and Time Zone
    COUNTRY = str(os.environ.get("COUNTRY", "India"))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    FBAN_REASON = os.environ.get("FBAN_REASON", None)
    FBAN_USER = os.environ.get("FBAN_USER", None)
    # Clean Welcome
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    # for Logging
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
    # Custom Module
    CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None)
    CUSTOM_ANIMATED_PACK_NAME = os.environ.get("CUSTOM_ANIMATED_PACK_NAME", None)

    # Pm Permit Img
    PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)

    # Gban
    USER_IS = os.environ.get("USER_IS", None)

    # For Bot Purposes
    OWNER_ID = os.environ.get("OWNER_ID", None)

    # Last.fm Module
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    BIO_MSG = os.environ.get("BIO_MSG", None)
    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
    if not LASTFM_USERNAME == "None":
        lastfm = pylast.LastFMNetwork(
            api_key=LASTFM_API,
            api_secret=LASTFM_SECRET,
            username=LASTFM_USERNAME,
            password_hash=LASTFM_PASS,
        )
    else:
        lastfm = None

    # Google Drive Module
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./downloads")
else:
    # Put your ppe vars here if you are using local hosting
    PLACEHOLDER = None

# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists("bin"):
    os.mkdir("bin")

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown": "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py": "bin/cmrudl",
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
SUDO_LIST = {}
CMD_HELP = {}
DETAIL_CMD_HELP = {}
CMD_LIST = {}
CUSTOM_PMPERMIT_MSG = {}
CUSTOM_BOTSTART = {}
ISAFK = False
AFKREASON = None

######Anti Spam system ######
link = "https://people.eecs.berkeley.edu/~rich.zhang/projects/2016_colorization/files/demo_v2/colorization_release_v2.caffemodel"
km = "./resources/imgcolour/colorization_release_v2.caffemodel"
pathz = "./resources/imgcolour/"
if os.path.exists(km):
    pass
else:
    try:
        sedlyf = wget.download(link, out=pathz)
    except:
        sedprint.info("I Wasn't Able To Download Cafee Model. Skipping")

if Config.ANTI_SPAMINC_TOKEN == None:
    sclient = None
    sedprint.info("[Warning] - AntispamInc is None")
else:
    try:
        sclient = Connect(Config.ANTI_SPAMINC_TOKEN)
    except Exception as e:
        sclient = None
        sedprint.info("[Warning] - " + e)
