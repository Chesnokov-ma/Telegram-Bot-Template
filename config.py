""" Общий файл для main и остальных модулей, где лежат Dispatcher и бот """

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage    # хранение временной информации в опреативной памяти
                                                                # важная вносится в БД

import json

with open('config.json', 'r') as fp:    # json - файл со всеми конфигами
    data = json.load(fp)

admin_id = data['admin_id']                         # id администратора бота

bot = Bot(token=data['TOKEN'])                      # создание бота
dp = Dispatcher(bot, storage=MemoryStorage())       # создание диспатчера