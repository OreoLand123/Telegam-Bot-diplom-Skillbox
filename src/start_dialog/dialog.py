from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start, Row
from aiogram_dialog.widgets.text import Const
from main_dialog.states import MainDialog
from start_dialog.state import StartDialog
from help_dialog.states import HelpState
from history_dialog.states import HistoryState

"""Окна для диалога /start"""

start_dialog = Dialog(
    Window(
        Const("Hello"),
        Row(
            Start(Const("Filter"),
                  id="main",
                  state=MainDialog.filter_window,
                ),
            Start(Const("Help"),
                  id="help",
                  state=HelpState.help_main,
                  ),
            Start(Const("History"),
                  id="history",
                  state=HistoryState.history_window,
                  )
        ),
        state=StartDialog.main,
    ))