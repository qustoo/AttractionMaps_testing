from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.Database_User.sqlite import Database
from utils.Database_Photo.sqlite_photo import PhotoDatabase

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# Хранение данных для машины состояний
# Храним в оперативной памяти
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# Импортируем базу данных юзера
db = Database()
# Импортируем базу данных фоток
photo_db = PhotoDatabase()
