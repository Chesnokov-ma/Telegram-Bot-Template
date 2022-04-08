from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext       # контекст для простотра текущего State

from config import admin_id, bot
from states.site_states import States as SiteStates     # стейты
from database.sqlite import add_user                    # sql-функция

from keyboards.reply_keyboard import rkm        # клавиатуры
from keyboards.inline_keyboard import ikm


# @dp.message_handler(commands=['start', 'help'], state='*')
async def start_messages(message: types.Message):
    await bot.send_message(chat_id=int(admin_id),
                               text=f'Подключился: {message.from_user.full_name}\nid = {message.from_user.id}')
    add_user()
        


# @dp.message_handler(commands=['info'], state=SiteStates.default_workState)  # узнать свой id
async def info_messages(message: types.Message):
    # код


# @dp.message_handler(commands=['all'], state=SiteStates.default_workState)  # все обрабатываемые биржи и ссылки на них
async def all_messages(message: types.Message):
    # код


# @dp.message_handler(commands=['sites'], state=SiteStates.default_workState)
async def sites_messages(message: types.Message, state: FSMContext):
    # код


# @dp.message_handler(commands=['cancel'], state=SiteStates.chose_siteState)
async def cancel_messages(message: types.Message):
    # код


# @dp.message_handler(state=SiteStates.chose_siteState)   # выбор биржи
async def chose_site_messages(message: types.Message):
    await SiteStates.default_workState.set()
    await message.answer(text='Снова введите /sites, чтобы открыть клавиатуру',
                             reply_markup=types.ReplyKeyboardRemove())
    # код


""" Регистрация хендлеров """
def register_handler_client(dp : Dispatcher):
    dp.register_message_handler(start_messages, commands=['start', 'help'], state='*')
    dp.register_message_handler(info_messages, commands=['info'], state=SiteStates.default_workState)
    dp.register_message_handler(all_messages, commands=['all'], state=SiteStates.default_workState)
    dp.register_message_handler(sites_messages, commands=['sites'], state=SiteStates.default_workState)
    dp.register_message_handler(cancel_messages, commands=['cancel'], state=SiteStates.chose_siteState)
    dp.register_message_handler(chose_site_messages, state=SiteStates.chose_siteState)


