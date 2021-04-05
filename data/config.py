import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

admins = [
    449640182
]

ip = os.getenv("ip")
QIWI_TOKEN = os.getenv("qiwi")
WALLET_QIWI = os.getenv("wallet")
QIWI_PUBLIC_KEY = os.getenv("qiwi_public_key")