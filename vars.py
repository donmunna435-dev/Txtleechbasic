

from os import environ

API_ID = environ.get("API_ID", "24754824")
API_HASH = environ.get("API_HASH", "e24a9c7a6aa24e1c56fa349e104ee")
BOT_TOKEN = environ.get("BOT_TOKEN", "82282399:AAHQapxFlhTrl0nd_zr5CfnOLCnqxNaYs")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "bot_subscription")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/bot_subscription")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "968292174").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "968292174"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")









