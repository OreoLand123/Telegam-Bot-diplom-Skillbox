from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import (
    StubScroll,
    ScrollingGroup,
    NumberedPager,
    SwitchTo,
    Back,
    Start,
)
from aiogram_dialog.widgets.text import Const, Progress, Multi, Format

from result_dialog.func_dialog import get_bg_data, get_json, paging_getter
from result_dialog.states import ResultDialog
from main_dialog.states import MainDialog

"""Окна диалога event result"""

result_dialog = Dialog(
    Window(
        Multi(
            Const("Запрос обрабатывается"),
            Progress("progress", 10),
        ),
        state=ResultDialog.progress,
        getter=get_bg_data,
    ),
    Window(
        Format("Oбъект: {current_page}"),
        Format("{dialog_data[text]}"),
        StubScroll(id="stub_scroll", pages="pages"),
        ScrollingGroup(
            NumberedPager(scroll="stub_scroll"), width=8, height=1, id="obj"
        ),
        SwitchTo(
            Const("Get JSON object"),
            id="json",
            state=ResultDialog.get_json_obj,
            on_click=get_json,
        ),
        Start(
            Const("Back to main menu"),
            state=MainDialog.filter_window,
            id="go_to_main_window",
        ),
        state=ResultDialog.result,
        getter=paging_getter,
    ),
    Window(
        Format("Формат JSON для объекта {dialog_data[current_page_json]}"),
        Format("{dialog_data[text_json]}"),
        Back(text=Const("Go to normal text")),
        state=ResultDialog.get_json_obj,
    ),
)
