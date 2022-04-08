""" Все прочие сообщения """

from aiogram import types, Dispatcher
from states.site_states import States as SiteStates


# @dp.message_handler(state='*')  # все прочие сообщения
async def other_messages(message: types.Message):
    # код


""" Регистрация хендлеров """
def register_handler_other(dp : Dispatcher):
    dp.register_message_handler(other_messages, state='*')