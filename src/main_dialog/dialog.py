from aiogram.enums import ContentType
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, SwitchTo, Column, Button, Start
from aiogram_dialog.widgets.text import Const, Format
from main_dialog.states import MainDialog
from start_dialog.state import StartDialog

from src.main_dialog.func_dialog import (
    get_filter_name,
    get_param,
    get_arg_param,
    input_message_value_custom,
    input_message_count_value,
    input_message_value,
    go_to_result_dialog,
)

"""Окна для диалога event filter"""

main_dialog = Dialog(
    Window(
        Const("Выберите команду для фильтрации API"),
        Row(
            SwitchTo(
                Const("Low"),
                id="low",
                state=MainDialog.choice_window,
                on_click=get_filter_name,
            ),
            SwitchTo(
                Const("height"),
                id="height",
                state=MainDialog.choice_window,
                on_click=get_filter_name,
            ),
            SwitchTo(
                Const("Custom"),
                id="custom",
                state=MainDialog.choice_window,
                on_click=get_filter_name,
            ),
        ),
        Start(Const("Back"), id="back_to_start", state=StartDialog.main),
        state=MainDialog.filter_window,
    ),
    Window(
        Format(
            "Выберите что именно вы хотите запросить для фильтра {dialog_data[filter_name]}"
        ),
        Row(
            SwitchTo(
                Const("people"),
                id="people",
                state=MainDialog.people_window,
                on_click=get_param,
            ),
            SwitchTo(
                Const("starships"),
                id="starships",
                state=MainDialog.starships_window,
                on_click=get_param,
            ),
            SwitchTo(
                Const("vehicles"),
                id="vehicles",
                state=MainDialog.vehicles_window,
                on_click=get_param,
            ),
        ),
        Row(
            SwitchTo(
                Const("species"),
                id="species",
                state=MainDialog.species_window,
                on_click=get_param,
            ),
            SwitchTo(
                Const("planets"),
                id="planets",
                state=MainDialog.planets_window,
                on_click=get_param,
            ),
        ),
        SwitchTo(Const("Back"), id="back_to_filter", state=MainDialog.filter_window),
        state=MainDialog.choice_window,
    ),
    Window(
        Format("Выберете по какому полю фильтравать запрос для {dialog_data[param]}"),
        Row(
            SwitchTo(
                Const("height"),
                id="height",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("mass"),
                id="mass",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("name"),
                id="name",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
        ),
        SwitchTo(Const("Back"), id="back_to_choice", state=MainDialog.choice_window),
        state=MainDialog.people_window,
    ),
    Window(
        Format("Выберете по какому полю фильтравать запрос для {dialog_data[param]}"),
        Column(
            SwitchTo(
                Const("cargo_capacity"),
                id="cargo_capacity",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("cost_in_credits"),
                id="cost_in_credits",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("hyperdrive_rating"),
                id="hyperdrive_rating",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("length"),
                id="length",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("passengers"),
                id="passengers",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("name"),
                id="name",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
        ),
        SwitchTo(Const("Back"), id="back_to_choice", state=MainDialog.choice_window),
        state=MainDialog.starships_window,
    ),
    Window(
        Format("Выберете по какому полю фильтравать запрос для {dialog_data[param]}"),
        Column(
            SwitchTo(
                Const("cargo_capacity"),
                id="cargo_capacity",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("cost_in_credits"),
                id="cost_in_credits",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("crew"),
                id="crew",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("length"),
                id="length",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("passengers"),
                id="passengers",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("max_atmosphering_speed"),
                id="max_atmosphering_speed",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("name"),
                id="name",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
        ),
        SwitchTo(Const("Back"), id="back_to_choice", state=MainDialog.choice_window),
        state=MainDialog.vehicles_window,
    ),
    Window(
        Format("Выберете по какому полю фильтравать запрос для {dialog_data[param]}"),
        Row(
            SwitchTo(
                Const("average_height"),
                id="average_height",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("average_lifespan"),
                id="average_lifespan",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("name"),
                id="name",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
        ),
        SwitchTo(Const("Back"), id="back_to_choice", state=MainDialog.choice_window),
        state=MainDialog.species_window,
    ),
    Window(
        Format("Выберете по какому полю фильтравать запрос для {dialog_data[param]}"),
        Column(
            SwitchTo(
                Const("diameter"),
                id="diameter",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("orbital_period"),
                id="orbital_period",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("population"),
                id="population",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("rotation_period"),
                id="rotation_period",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("surface_water"),
                id="surface_water",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
            SwitchTo(
                Const("name"),
                id="name",
                state=MainDialog.input_window,
                on_click=get_arg_param,
            ),
        ),
        SwitchTo(Const("Back"), id="back_to_choice", state=MainDialog.choice_window),
        state=MainDialog.planets_window,
    ),
    Window(
        Format("{dialog_data[text_custom]} {dialog_data[arg_param]}"),
        Column(
            SwitchTo(Const("Back"), id="back_to_choice", state=MainDialog.choice_window)
        ),
        MessageInput(input_message_value, content_types=[ContentType.TEXT]),
        state=MainDialog.input_window,
    ),
    Window(
        Format("Введите стоп для поля: {dialog_data[arg_param]}"),
        SwitchTo(Const("Back"), state=MainDialog.input_window, id="back_to_window1"),
        MessageInput(input_message_value_custom, content_types=[ContentType.TEXT]),
        state=MainDialog.input_window_custom,
    ),
    Window(
        Format("Ведите кол-во запрашиваемых объектов {dialog_data[arg_param]}"),
        MessageInput(input_message_count_value, content_types=[ContentType.TEXT]),
        SwitchTo(Const("Back"), state=MainDialog.input_window, id="back_to_window_2"),
        state=MainDialog.input_count_window,
    ),
    Window(
        Format(
            "Данные которые вы ввели:\n"
            "Фильтр: {dialog_data[filter_name]}\n "
            "Поле: {dialog_data[arg_param]}\n "
            "Значение поля: {dialog_data[value]}\n"
            "Кол-во получаемых объектов: {dialog_data[count_value]}"
        ),
        Button(Const("Start"), id="start", on_click=go_to_result_dialog),
        SwitchTo(
            Const("Back ot choice"), id="back_to_choice", state=MainDialog.choice_window
        ),
        state=MainDialog.process_window,
    ),
    Window(
        Format(
            "Данные которые вы ввели:\n"
            "Фильтр: {dialog_data[filter_name]}\n "
            "Поле: {dialog_data[arg_param]}\n "
            "Значение поля: {dialog_data[value]}\n"
        ),
        Button(Const("Start"), id="start", on_click=go_to_result_dialog),
        SwitchTo(
            Const("Back ot choice"), id="back_to_choice", state=MainDialog.choice_window
        ),
        state=MainDialog.process_search_window,
    ),
)
