import os
from dotenv import load_dotenv


load_dotenv()

BOT_API_TOKEN = os.getenv("DISCORD_API_T")
DISCORD_API_AUTH = os.getenv("AUTH_T")
