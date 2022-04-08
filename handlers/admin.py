""" Здесь описывается логика работы с пользоватилем с id = admin_id """

from aiogram import types, Dispatcher
from states.site_states import States as SiteStates     # состояния


# @dp.message_handler(commands=['id'], state='*')  # узнать свой id
async def admin_messages(message: types.Message):
    # код


""" Регистрация хендлеров """
def register_handler_admin(dp : Dispatcher):
    dp.register_message_handler(admin_messages, commands=['admin'], state=SiteStates.default_workState)