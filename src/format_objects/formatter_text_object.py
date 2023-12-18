"""
Текст для форматирования для диалогов result, help, history
"""

text = {
    "people": """
              Имя: {name}
              День рождения: {birth_year}
              Цвет глаз: {eye_color}
              Фильмы: {films}
              Гендер: {gender}
              Цвет волос: {hair_color}
              Рост: {height}
              Место рождения: {homeworld}
              Вес: {mass}
              Цвет кожи: {skin_color}
              Дата создания: {created}
              Дата изменения: {edited}
              Разновидность: {species}
              Звездолёт: {starships}
              URL: {url}
              Транспортное средство: {vehicles}
              """,

    "starship": """
                Название: {name}
                MGLT: {MGLT}
                Грузоподъёмность: {cargo_capacity}
                Из чего изготовлен: {consumables}
                Стоимость: {cost_in_credits}
                Создан в: {created}
                Кол-во экипажа: {crew}
                Изменён: {edited}
                Рейтиг: {hyperdrive_rating}
                Длина: {length}
                Производитель: {manufacturer}
                Максимальная атмосферная скорость: {max_atmosphering_speed}
                Модель: {model}
                Пассажиры: {passengers}
                Фильмы: {films}
                Пилоты: {pilots}
                Класс корабля: {starship_class}
                URL: {url}
                """,

    "vehicles": """
                Название: {name}"
                Грузоподъёмность: {cargo_capacity}
                Из чего изготовлен: {consumables}
                Стоимость: {cost_in_credits}
                Создан в: {created}
                Кол-во экипажа: {crew}
                Изменён: {edited}
                Длина: {length}
                Производитель: {manufacturer}
                Максимальная атмосферная скорость: {max_atmosphering_speed}
                Модель: {model}
                Пассажиры: {passengers}
                Пилоты: {pilots}
                Фильмы: {films}
                URL: {url}
                Класс техники: {vehicle_class}
                """,

    "species": """
               Название: {name}
               Имя: {name}
               Средний рост: {average_height}
               Средняя продолжительность жизни: {average_lifespan}
               Классификация: {classification}
               Создан в: {created}
               Обозначение: {designation}
               Изменён: {edited}
               Цвет глаз: {eye_colors}
               Цвет волос: {hair_colors}
               Место рождения: {homeworld}
               Язык: {language}
               Люди: {people}
               Цвет кожи: {skin_colors}
               URL: {url}
               """,

    "planet": """
              Климат: {climate}
              Создан в: {created}
              Диаметр: {diameter}
              Изменён: {edited}
              Фильмы: {films}
              Гравитация: {gravity}
              Орбитальный период: {orbital_period}
              Население: {population}
              Жители: {residents}
              Период: {rotation_period}
              Поверхность воды: {surface_water}
              Местность: {terrain}
              URL: {url}
              """,

    "people_json":
        """
        {{
            "birth_year": "{birth_year}",
            "eye_color": "{eye_color}",
            "films": {films},
            "gender": "{gender}",
            "hair_color": "{hair_color}",
            "height": "{height}",
            "homeworld": "{homeworld}",
            "mass": "{mass}",
            "name": "{name}",
            "skin_color": "{skin_color}",
            "created": "{created}",
            "edited": "{edited}",
            "species": {species},
            "starships": {starships},
            "url": "{url}",
            "vehicles": {vehicles}
        }}
        """,

    "starship_json":
        """
        {{
            "MGLT": "{MGLT}",
            "cargo_capacity": "{cargo_capacity}",
            "consumables": "{consumables}",
            "cost_in_credits": "{cost_in_credits}",
            "created": "{created}",
            "crew": "{crew}",
            "edited": "{edited}",
            "hyperdrive_rating": "{hyperdrive_rating}",
            "length": "{length}",
            "manufacturer": "{manufacturer}",
            "max_atmosphering_speed": "{max_atmosphering_speed}",
            "model": "{model}",
            "name": "{name}",
            "passengers": "{passengers}",
            "films": {films},
            "pilots": {pilots},
            "starship_class": "{starship_class}",
            "url": "{url}"
        }}
        """,

    "vehicles_json":
        """
        {{
            "cargo_capacity": "{cargo_capacity}",
            "consumables": "{consumables}",
            "cost_in_credits": "{cost_in_credits}",
            "created": {created}",
            "crew": "{crew}",
            "edited": "{edited}",
            "length": "{length}",
            "manufacturer": {manufacturer}",
            "max_atmosphering_speed": "{max_atmosphering_speed}",
            "model": "{model}",
            "name": "{name}",
            "passengers": "{passengers}",
            "pilots": {pilots},
            "films": {films},
            "url": "{url}",
            "vehicle_class": "{vehicle_class}"
        }}
        """,

    "species_json":
        """
        {{
            "average_height": "{average_height}",
            "average_lifespan": "{average_lifespan}",
            "classification": "{classification}",
            "created": "{created}",
            "designation": "{designation}",
            "edited": "{edited}",
            "eye_colors": "{eye_colors}",
            "hair_colors": "{hair_colors}",
            "homeworld": "{homeworld}",
            "language": "{language}",
            "name": "{name}",
            "people": {people},
            "films": {films},
            "skin_colors": "{skin_colors}",
            "url": "{url}"
        }}
        """,

    "planet_json":
        """
        {{
            "climate": "{climate}",
            "created": "{created}",
            "diameter": "{diameter}",
            "edited": "{edited}",
            "films": {films},
            "gravity": "{gravity}",
            "name": "{name}",
            "orbital_period": "{orbital_period}",
            "population": "{population}",
            "residents": {residents},
            "rotation_period": "{rotation_period}",
            "surface_water": "{surface_water}",
            "terrain": "{terrain}",
            "url": "{url}"
        }}
        """
}

text_help = {
    "filter":
        """
        Фильтры бота делятся на low, height, custom
        low - Фильтр для нахождения объектов значения полей которых меньше или равны введёному вами значению
        Пример: значение поля API <= ваше значение

        height - Фильтр для нахождения объектов значения полей которых больше или равны введёному вами значению
        Пример: значение поля API >= ваше значение

        custom - Филтр для нахождения объектов которые в ходят в заданный вами диапазон значений
        Пример 1: ваше стартовое значение <= значение поля API <= ваше конечное значение
        Пример 2: ваше стартовое значение >= значение поля API >= ваше конечное значение

        Пример 2 работет при вводе стартового значения бльше конечного значения 
        """,

    "param":
        """
        Объекты по которым можно фильтровать

        Значения объектов:
        people - Люди (персонажи)
        starships - Звездолеты
        vehicles - Техника
        species - Разновидности (рассы)
        planets - Планеты

        У каждого объекта есть свои наборы полей по которым можно фильтровать
        """,

    "arg_param":
        """
        У каждого объекта есть своё поле фильтрации
        Так же бот принимает кол-во запрашиваемых объектов

        Примечание: Бот не выдаёт те API объекты в которых фильтруемое поле является None

        Каждое поле кроме поля name принимает в себя только цифры, при необхости найти объект по
        его имени используйте фильтрацию по полю name.

        Поле name ищет объект по его имени
        Пример: Sand Crawler найдёт объект чьё поле name: Sand Crawler

        Если ваше введённое значение или даипазон не совпадает по фильтрации со значением поля
        лбого объекта, то Бот вернёт 0 кол-во объектов

        Если вы введёте кол-во запрашиваемых объектов изначально привышающее кол-во объектов API
        То бот выдаст все объекты удовлетворяющие фильтрации

        Если кол - во удовлетворяющих фильтрации объектов меньше чем вы задали то бот вернёт так же
        все объекты удовлетворяющие фильтрации

        Иначе бот вернёт то кол-во объектов которе вы запросили
        """,

    "value":
        """
        Бот выдаёт значения объектов в виде читаемого тектса и 
        в виде текста в формате JSON
        """
}

text_history = """
                URL: {url}
                Фильтр: {filter_name}
                Объект: {param}
                Поле: {arg_param}
                Значение: {value}
                Кол-во запрошеных объектов: {count_value}
                Cтатус запроса: {status_request}
                Кол-во объектов получено: {count_obj}
               """