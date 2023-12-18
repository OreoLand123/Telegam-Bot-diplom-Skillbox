from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import StubScroll, ScrollingGroup, NumberedPager, Start
from aiogram_dialog.widgets.text import Format, Const
from start_dialog.state import StartDialog
from history_dialog.func_dialog import paging_getter
from history_dialog.states import HistoryState

"""Диалог окон для event history"""

history_dialog = Dialog(
    Window(
        Format("Запрос: {current_page}"),
        Format("{result}"),
        StubScroll(
            id="stub_scroll",
            pages="pages"),
        ScrollingGroup(NumberedPager(
            scroll="stub_scroll"),
            width=5,
            height=1,
            id="obj"),
        Start(Const("Back to start"),
              state=StartDialog.main,
              id="go_to_main_window"),
        state=HistoryState.history_window,
        getter=paging_getter,
    ),
)