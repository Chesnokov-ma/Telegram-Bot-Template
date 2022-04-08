""" Точка входа для бота """
from aiogram import types
from aiogram.utils import executor  # импорт aiogtam-компонентов

import hashlib                          # для articles
from config import dp                   # здесь, общий файл для main и остальных модулей, где лежат Dispatcher и бот
from database.sqlite import start_sql   # создание (IF NOT EXIST) базы данных при страрте

from handlers import admin, client, other   # регистрация хендлеров из других модулей
admin.register_handler_admin(dp)
client.register_handler_client(dp)
other.register_handler_other(dp)


async def on_startup(_):    # функция, срабатывающая при старте
    start_sql()             # создание (IF NOT EXIST) базы данных при страрте


""" У бота может быть только один inline handler """
@dp.inline_handler()
async def inline_message(query: types.InlineQuery):
    text = query.query or "echo"
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(     # ответное сообщение
        id=result_id,
        title='Текст в inline ответе',
        input_message_content=types.InputTextMessageContent(
            message_text= 'строка для вывода' 
        )
    )]
    await query.answer(articles, cache_time=1, is_personal=True)


""" Запуск бота в режиме polling """
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)