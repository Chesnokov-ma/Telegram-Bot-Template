import sqlite3 as sq        # для демонстрации используется sqlite3, постовляемы вместе с питоном


""" Создание (IF NOT EXIST) базы данных и таблиц при запуске бота """
def start_sql():
    global base, cur
    base = sq.connect('database.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS users(id TEXT PRIMARY KEY, name TEXT)')
    base.commit()
    # print('База данных подключена')



""" Пример sql-операции : запись нового пользователя (id, ник в телеграмме) в базу данных при /start """
async def add_user(id, name):
    global base, cur
    try:
        base.execute(f'INSERT INTO users VALUES("{id}", "{name}")')
        base.commit()
        # print(f'Пользователь {name}, id = {id} добавлен')
    except:
        # print('Пользователь уже есть в БД')
        pass

