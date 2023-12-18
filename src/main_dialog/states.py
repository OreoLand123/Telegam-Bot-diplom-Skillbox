from aiogram.filters.state import State, StatesGroup


class MainDialog(StatesGroup):

    """Состояния для диалога main"""

    filter_window = State()
    choice_window = State()
    people_window = State()
    starships_window = State()
    vehicles_window = State()
    species_window = State()
    planets_window = State()
    input_window = State()
    input_count_window = State()
    input_window_custom = State()
    process_window = State()
    search_window = State()
    result_window = State()
    process_search_window = State()
