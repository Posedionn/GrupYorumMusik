import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "17640497"))
API_HASH = getenv("API_HASH", "503e4410bfca22583ca15884049ff3c8")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6739415206:AAGFHfTBotvGIZ5fkbnlOmpIEjcJDz0AmTY")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://BrandedSupportGroup:BRANDED_WORLD@cluster0.v4odcq9.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001979116207"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "1400179801"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Posedionn/GrupYorumMusik",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/YORUMHANEM")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/GuRuPyOrUm")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "False")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "AQENLDEAel5MG6fF4nYpp3YbfkKCDL-1ByY1v2iHAyCL3Vvdfbv0_Xr8eL5f4Oe2btfv6CFmm_AK84LilLTfRM6xhLev5US1hBZSyHGVrBMh4DS524iZ7WXbKBtpFbNiwR4x-xTZWNczkFtdnYu4QM-o_0jcbCTcGA0ZnU8ZjA6makOAzRmIPNvyz4fV4p374ontcD3aDLdBFS1vLtTKQyxSPrC5DWtg3jafCB6HcLr22qKW4xavSxJGxSD9PoFuD5PPz6iv_4u-WGR-5l7Kjvfr1DZf6IcqjHEUZtg8nDNM1qFHw3Cce5JMcfkhlutcHPA--3aXqYY_Qlv9oga_JZmP9KCEEgAAAAEv6S0IAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/Music-11-30-4"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/Music-11-30-4"
)
PLAYLIST_IMG_URL = "https://telegra.ph/Music-11-30-4"
STATS_IMG_URL = "https://telegra.ph/Music-11-30-4"
TELEGRAM_AUDIO_URL = "https://telegra.ph/Music-11-30-4"
TELEGRAM_VIDEO_URL = "https://telegra.ph/Music-11-30-4"
STREAM_IMG_URL = "https://telegra.ph/Music-11-30-4"
SOUNCLOUD_IMG_URL = "https://telegra.ph/Music-11-30-4"
YOUTUBE_IMG_URL = "https://telegra.ph/Music-11-30-4"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/Music-11-30-4"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/Music-11-30-4"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/Music-11-30-4"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
