from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# reply клавиатура

rkm = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) \
            .row(KeyboardButton('Текст 1'), KeyboardButton('Текст 2'))