import asyncio

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from api import API
from main_dialog.states import MainDialog
from result_dialog.func_dialog import background
from result_dialog.states import ResultDialog

"""-----------------------------------------------Getter Func--------------------------------------------------------"""


async def get_filter_name(callback: CallbackQuery, button: Button, manager: DialogManager):
    """
    :param callback:
    :param button:
    :param manager:
    :return:

    getter для получении названия фильтра
    """
    manager.dialog_data['filter_name'] = button.widget_id


async def get_arg_param(callback: CallbackQuery, button: Button, manager: DialogManager):
    """
    :param callback:
    :param button:
    :param manager:
    :return:

    getter для получении названия аргумента параметра
    """
    manager.dialog_data['arg_param'] = button.widget_id


async def get_param(callback: CallbackQuery, button: Button, manager: DialogManager):
    """
    :param callback:
    :param button:
    :param manager:
    :return:

    getter для поулчения текста по фильтру в случаее если фильр costum то текст меняется
    """
    manager.dialog_data['param'] = button.widget_id
    if manager.dialog_data["filter_name"] == "custom":
        manager.dialog_data["text_custom"] = "Введите старт для поля: "
    else:
        manager.dialog_data["text_custom"] = "Введите значение для поля: "


"""--------------------------------------------------Main func-------------------------------------------------------"""


async def input_message_value(message: Message, message_input: MessageInput, manager: DialogManager):
    """
    :param message:
    :param message_input:
    :param manager:
    :return:

    Валидация вводимых данных и переход к новому окну
    """
    if manager.is_preview():
        await manager.next()
        return
    obj_name = manager.dialog_data["arg_param"]  # Получаем название аргумента параметра
    try:
        float(message.text)
        flag = True
    except ValueError:
        flag = False
    if not flag and obj_name != "name":
        await message.answer("Для данного поля нужно вводить число")
        await manager.switch_to(MainDialog.input_window)
        return
    elif obj_name != "name" and manager.dialog_data["filter_name"] == "custom":  # Вводим старт при названии фильтра custom
        manager.dialog_data["value_1"] = float(message.text)  # Записываем стартовое значение
        await manager.switch_to(MainDialog.input_window_custom)  # Переходим к окну ввода стоп значения
        return
    manager.dialog_data["value"] = float(message.text) if flag else message.text  # Записываем значение при успешной валидации
    if obj_name == "name":
        await manager.switch_to(MainDialog.process_search_window)  # Переход на окно старта запроса
        return
    await manager.switch_to(MainDialog.input_count_window)  # Переход на окно ввода кол-во запросов


async def input_message_value_custom(message: Message, message_input: MessageInput, manager: DialogManager):
    """
    :param message:
    :param message_input:
    :param manager:
    :return:

    Ввод кастомного значения (стоп значение)
    """
    if manager.is_preview():
        await manager.next()
        return
    try:
        float(message.text)
        flag = True
    except ValueError:
        flag = False

    if not flag:  # Валидация данных
        await message.answer("Для данного поля нужно вводить число")
        await manager.switch_to(MainDialog.input_window_custom)
        return
    value_1 = manager.dialog_data["value_1"]  # Достаём значения старта
    manager.dialog_data["value"] = (value_1, float(message.text))  # Записываем в виде tuple диапазон
    await manager.switch_to(MainDialog.input_count_window)  # Переход на окно ввода кол-во запросов


async def input_message_count_value(message: Message, message_input: MessageInput, manager: DialogManager):
    """
    :param message:
    :param message_input:
    :param manager:
    :return:

    Ввод кол-во запросов
    """
    if manager.is_preview():
        await manager.next()
        return
    if not message.text.isdigit():  # Валидация по целому числу
        await message.answer("Нужно вводить целое число")
        await manager.switch_to(MainDialog.input_count_window)
        return
    manager.dialog_data["count_value"] = int(message.text)  # Записываем кол-во запросов
    await manager.next()  # Переход к следующему окну


async def go_to_result_dialog(callback: CallbackQuery, button: Button, manager: DialogManager) -> None:
    """
    :param callback:
    :param button:
    :param manager:
    :return:

    Переход к диалогу result_dialog и выполнения API Запроса по введённым данным
    """
    api = API()  # Инициализируем класс API
    count_value: int = manager.dialog_data.get("count_value")  # Достаём из memorystorage кол-во запросов
    value = manager.dialog_data.get("value")  # Достаём из memorystorage значения поля
    filter_name: str = manager.dialog_data.get("filter_name")  # Достаём из memorystorage название фильтра
    param_name: str = manager.dialog_data.get("param")  # Достаём из memorystorage название параметра
    arg_param: str = manager.dialog_data.get("arg_param")  # Достаём из memorystorage аргумент параметра (название поля)
    user_id = int(callback.from_user.id)
    data = {
        "filter_name": filter_name,
        "param_name": param_name,
        "arg_param": arg_param,
        "value": value,
        "count_value": count_value,
        "user_id": user_id
    }  # Формируем словарь данных
    if arg_param == "name":  # Проверка на поиск по имени
        result_data = api.search_obj(param_name=param_name,
                                     search_input=value,
                                     user_id=user_id,
                                     filter_name=filter_name)  # Поиск по имени
    else:
        result_data = api.result_request(**data)  # Фильрация по конкретному полю
    await manager.start(ResultDialog.progress)  # Запускаем состояния дял процесса
    manager.dialog_data["result_data"] = result_data  # Записываем результат апи
    asyncio.create_task(background(callback, manager.bg()))
