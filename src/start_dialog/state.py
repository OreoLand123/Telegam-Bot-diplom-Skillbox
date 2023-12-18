from aiogram.fsm.state import StatesGroup, State


class StartDialog(StatesGroup):
    """Состояние для диалога start"""
    main = State()