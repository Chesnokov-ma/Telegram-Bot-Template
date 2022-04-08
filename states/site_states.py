from aiogram.dispatcher.filters.state import State, StatesGroup

# стейты

class States(StatesGroup):
    default_workState = State()
    chose_siteState = State()