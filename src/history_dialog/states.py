from aiogram.fsm.state import StatesGroup, State


class HistoryState(StatesGroup):
    """Состояния для history"""
    history_window = State()