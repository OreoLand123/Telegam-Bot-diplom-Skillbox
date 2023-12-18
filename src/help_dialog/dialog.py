from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Row, SwitchTo, Back, Start
from aiogram_dialog.widgets.text import Const, Format
from help_dialog.states import HelpState
from start_dialog.state import StartDialog
from help_dialog.func_dialog import get_help_text


"""
Окна диалога для event help
"""

help_dialog = Dialog(
    Window(
        Const("Если вам не понятны функции бота то переходите по кнопкам ниже"),
        Row(
            SwitchTo(
                Const("Фильтры"),
                id="filter",
                state=HelpState.help_text,
                on_click=get_help_text,
            ),
            SwitchTo(
                Const("Объекты"),
                id="param",
                state=HelpState.help_text,
                on_click=get_help_text,
            ),
        ),
        Row(
            SwitchTo(
                Const("Поля и запросы"),
                id="arg_param",
                state=HelpState.help_text,
                on_click=get_help_text,
            ),
            SwitchTo(
                Const("Значения"),
                id="value",
                state=HelpState.help_text,
                on_click=get_help_text,
            ),
        ),
        Start(Const("Back to start"), id="go_to_start", state=StartDialog.main),
        state=HelpState.help_main,
    ),
    Window(
        Format("{dialog_data[help_text]}"),
        Back(text=Const("Back")),
        state=HelpState.help_text,
    ),
)
