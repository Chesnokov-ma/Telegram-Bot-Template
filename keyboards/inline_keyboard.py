from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# инлайн клавиатура

ikm = InlineKeyboardMarkup(row_width=1)
button0 = InlineKeyboardButton(text='Текст 1', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
ikm.add(button0)