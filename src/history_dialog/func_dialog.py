from aiogram_dialog import DialogManager
from src.model import session, User, Log
from format_objects.formatter_text_object import text_history


async def paging_getter(dialog_manager: DialogManager, **_kwargs) -> dict:
    """
    :param dialog_manager:
    :param _kwargs:
    :return:

    Пагинация страниц по getter
    """
    current_page = await dialog_manager.find("stub_scroll").get_page()
    user_id = _kwargs.get("event_from_user").id  # Получаем tg id юзера
    history_data = (
        session.query(Log).join(User).filter(User.tg_id == user_id).all()
    )  # Получаем логи истории из db
    text_history_data = list()
    if history_data:
        for obj in history_data:  # форматируем лог для текста
            format_value = {
                "url": obj.url,
                "filter_name": obj.filter_name,
                "param": obj.param,
                "arg_param": obj.arg_param,
                "value": obj.value,
                "count_value": obj.count_value,
                "status_request": obj.status_request,
                "count_obj": obj.count_obj,
            }
            text_history_data.append(
                text_history.format(**format_value)
            )  # Добавляем в список текст лога
    count_pages = len(history_data)  # Кол-во страниц
    if count_pages:
        text = text_history_data[current_page]
    else:
        text = "История пуста"
    return {
        "pages": count_pages,
        "current_page": current_page + 1,
        "result": text,
    }
