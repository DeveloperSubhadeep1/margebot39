import os


class Config(object):
    API_HASH = os.environ.get("API_HASH","6e7e2f5cdddba536b8e603b3155223c1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","7305658772:AAEuEsdmgmnJ7nhoJqlt3pt0YEYDG2uicn0")
    TELEGRAM_API = os.environ.get("TELEGRAM_API","27972068")
    OWNER = os.environ.get("OWNER","27972068")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","@Developer_Devil_01")
    PASSWORD = os.environ.get("PASSWORD","devil")
    DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://ytclone:ytclone@cluster0.uldqgds.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("LOGCHANNEL","-1002363002982" )  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
    PORT = int(os.environ.get("PORT", "8080"))
