from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from format_objects.formatter_text_object import text_help


async def get_help_text(callback: CallbackQuery, button: Button, manager: DialogManager) -> None:
    """
    :param callback:
    :param button:
    :param manager:
    :return:

    getter для текста help
    """
    manager.dialog_data["help_text"] = text_help[button.widget_id]



