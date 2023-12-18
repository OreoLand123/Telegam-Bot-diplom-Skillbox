import asyncio

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, BaseDialogManager
from aiogram_dialog.widgets.kbd import Button
from result_dialog.states import ResultDialog

"""--------------------------------------------------Getter func-----------------------------------------------------"""


async def get_bg_data(dialog_manager: DialogManager, **kwargs) -> dict:
    """
    :param dialog_manager:
    :param kwargs:
    :return:

    getter для процесса загрузки
    """
    return {"progress": dialog_manager.dialog_data.get("progress", 0)}


async def paging_getter(dialog_manager: DialogManager, **_kwargs) -> dict:
    """
    :param dialog_manager:
    :param _kwargs:
    :return:
    getter для пагинации результата работы API
    """
    current_page = await dialog_manager.find(
        "stub_scroll"
    ).get_page()  # Текущая страница
    result_data: list = dialog_manager.dialog_data["result_data"]  # Достаём результат
    dialog_manager.dialog_data[
        "current_page_json"
    ] = current_page  # Записываем текущую страницу для получения нужног json формата из списка
    count_pages: int = len(result_data)  # Кол-во страниц
    if (
        result_data
    ):  # Если пришли данные от API то вызываем у объектов в списке result_data метод для получения форматированного текста
        dialog_manager.dialog_data["text"] = [
            i.get_text(flag=False) for i in result_data
        ][current_page]
        result = result_data[current_page]
    else:  # Иначе выводим сообщение
        dialog_manager.dialog_data["text"] = "По данному запросу ничего не найдено"
        result = 0
    return {
        "pages": count_pages,
        "current_page": current_page + 1,
        "result": result,
    }


async def get_json(callback: CallbackQuery, button: Button, manager: DialogManager):
    """
    :param callback:
    :param button:
    :param manager:
    :return:

    getter для получения данных в формате JSON
    """
    current_page = manager.dialog_data["current_page_json"]  # Достаём кол-во страниц
    result_data = manager.dialog_data["result_data"]  # Достаём результат API
    if (
        result_data
    ):  # Вызываем метод get_text с флагом True для форматирования текста в виде JSON
        manager.dialog_data["text_json"] = result_data[current_page].get_text(flag=True)
    else:
        manager.dialog_data["text_json"] = "У объекта нет json"


"""-----------------------------------------------Main func----------------------------------------------------------"""


async def background(callback: CallbackQuery, manager: BaseDialogManager) -> None:
    """
    :param callback:
    :param manager:
    :return:

    Функция визуализации процесса
    """
    count = 10
    for i in range(1, count + 1):
        await asyncio.sleep(0.5)
        await manager.update(
            {
                "progress": i * 100 / count,
            }
        )
    await asyncio.sleep(0.5)
    await manager.switch_to(ResultDialog.result)
