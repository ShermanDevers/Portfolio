import os
from dotenv import load_dotenv


load_dotenv()

DISCORD_API_TOKEN = os.getenv("DISCORD_API_T")
AUTH = os.getenv("AUTH_T")
