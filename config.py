import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "18382142"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0ead4a1ddaeeea38a0fd231d8f9bf2fb")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://imomsaisingh:uYtvFVboorunDnOx@apister0.ofom2lx.mongodb.net/?retryWrites=true&w=majority&appName=apister0")
