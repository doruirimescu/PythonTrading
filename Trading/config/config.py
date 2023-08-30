from dotenv import load_dotenv
import json
import os

load_dotenv()

# XTB configurations
USERNAME = os.getenv("XTB_USERNAME")
PASSWORD = os.getenv("XTB_PASSWORD")
MODE = os.getenv("XTB_MODE")
TIMEZONE = os.getenv("BROKER_TIMEZONE", 'Europe/Berlin')

# Email configurations
EMAIL_SENDER=os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD=os.getenv("EMAIL_PASSWORD")
EMAIL_RECIPIENTS=os.getenv("EMAIL_RECIPIENTS")

# Program configurations
MONITOR_FOREX_TRADE_SWAPS_ONCE=os.getenv("MONITOR_FOREX_TRADE_SWAPS_ONCE")
DATA_STORAGE_PATH=os.getenv("DATA_STORAGE_PATH")
SYMBOLS_PATH = DATA_STORAGE_PATH + "symbols/"

ALL_SYMBOLS_PATH = SYMBOLS_PATH + "all_symbols.json"
ALL_SYMBOLS = None
with open(ALL_SYMBOLS_PATH, 'r') as f:
    ALL_SYMBOLS = json.load(f)

DB_USERNAME=os.getenv("DB_USERNAME")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_NAME=os.getenv("DB_NAME")
