from aiogram.fsm.state import State, StatesGroup


class HelpState(StatesGroup):
    """
    Состояния для окон help
    """

    help_main = State()
    help_text = State()
