import re

import requests
from requests.exceptions import RequestException
from format_objects.dataclasses_api import PeopleDataCass, SpeciesDataClass, VehiclesDataClass, PlanetsDataClass, StarshipsDataClass
from src.model import Log, session, User

"""API к сайту SWAPI"""


class API:

    url = "https://swapi.dev/api/{}"  # Базовый url

    def create_obj_data_class(self, param_name: str, obj: dict):
        """
        :param param_name:
        :param obj:
        :return:

         Создания объекта по названию параметра
        """
        match param_name:  # фильтрация по param_name
            case "people":
                dataclass_obj = PeopleDataCass(**obj)
            case "starships":
                dataclass_obj = StarshipsDataClass(**obj)
            case "vehicles":
                dataclass_obj = VehiclesDataClass(**obj)
            case "species":
                dataclass_obj = SpeciesDataClass(**obj)
            case "planets":
                dataclass_obj = PlanetsDataClass(**obj)
            case _:
                dataclass_obj = None
        return dataclass_obj

    def validator(self, obj: str):
        """
        :param obj:
        :return:

        Валидатор для приведения типов данных к типу float.
        Возвращает либо тип данных либо False если не получается
        привести к типу данных float
        """
        if re.match(r"^\d+?\,\d+?$", obj) is not None:
            return float(obj.replace(",", "."))
        elif re.match(r"^\d+?\-\d+?$", obj) is not None:
            return float(obj.replace("-", ""))
        elif re.match(r"^\d+?\.\d+?$", obj) is not None:
            return float(obj)
        elif obj.isdigit():
            return float(obj)
        else:
            return False

    def object_verification(self, data_json: list, result: list, filter_name: str, arg_param: str,
                            param_name: str, value) -> list:
        """
        :param data_json:
        :param result:
        :param filter_name:
        :param arg_param:
        :param param_name:
        :param value:
        :return:

        Нахождение объекта по фильтру и его значению
        """
        for obj in data_json:
            obj_valid = self.validator(obj[arg_param])  # Приведение к типу float
            if not obj_valid:
                continue
            match filter_name.lower():
                case "low":
                    if obj_valid <= value:
                        data_obj = self.create_obj_data_class(param_name, obj)
                        result.append(data_obj)
                case "height":
                    if obj_valid >= value:
                        data_obj = self.create_obj_data_class(param_name, obj)
                        result.append(data_obj)
                case "custom":
                    if value[0] >= value[1]:
                        if value[1] <= obj_valid <= value[0]:
                            data_obj = self.create_obj_data_class(param_name, obj)
                            result.append(data_obj)
                    else:
                        if value[0] <= obj_valid <= value[1]:
                            data_obj = self.create_obj_data_class(param_name, obj)
                            result.append(data_obj)
        return result

    def result_request(self, filter_name: str, param_name: str,
                       arg_param: str, value, count_value: int, user_id: int) -> list:
        """
        :param filter_name:
        :param param_name:
        :param arg_param:
        :param value:
        :param count_value:
        :param user_id:
        :return:

        Осуществление запрса и его логирование
        Так же фильтрация объектов запроса
        """
        result = list()
        try:
            request = requests.get(self.url.format(param_name)).json()
        except RequestException:
            self.register_log(self.url.format(param_name), filter_name, param_name,
                              arg_param, value, count_value, 400, 0, user_id)  # Логирование
            return result
        data_json = request["results"]
        if count_value > int(request["count"]):  # Проверка на кол-во запросов в случае привышения выдаются все объекты удовлетворяющиее фильтрацию
            count_value = int(request["count"])
        elif request["count"] == 0:
            self.register_log(self.url.format(param_name), filter_name, param_name,
                              arg_param, value, count_value, 200, 0, user_id)
            return result
        self.object_verification(data_json, result, filter_name, arg_param, param_name, value)  # Проверка и фильтрация объектов
        if count_value < len(result):
            result = result[:count_value]
        self.register_log(self.url.format(param_name), filter_name, param_name,
                          arg_param, value, count_value, 200, len(result), user_id)
        return result

    def register_log(self, url: str, filter_name: str, param_name: str, arg_param: str, value, count_value: int,
                     status_request: int, count_obj: int, user_id) -> None:
        """
        :param url:
        :param filter_name:
        :param param_name:
        :param arg_param:
        :param value:
        :param count_value:
        :param status_request:
        :param count_obj:
        :param user_id:
        :return:

        Функция регистрации лога при запросах
        для записи их в db
        Каждый лог зафиксирован за каждым польователям
        """
        user_object_id = session.query(User.id).where(User.tg_id == user_id).first()[0]  # Находим пользователя
        history_data = session.query(Log).join(User).filter(User.tg_id == user_id).all()  # Находим все логи привязанные к нему
        if len(history_data) == 10:  # Проверяем кол-во привязанных к нему логов
            session.delete(history_data[0])  # Удаляем первый лог в списке в случае успешной проверки
            session.commit()
        log = Log(user_id=user_object_id,
                  url=url,
                  filter_name=filter_name,
                  param=param_name,
                  arg_param=arg_param,
                  value=str(value),
                  count_value=count_value,
                  status_request=status_request,
                  count_obj=count_obj)  # Создаём объект лога
        session.add(log)  # Добавляем лог в бд
        session.commit()
        session.flush()

    def search_obj(self, param_name: str, search_input: str, user_id: int, filter_name: str) -> list:
        """
        :param param_name:
        :param search_input:
        :param user_id:
        :return:

        Функция поиска по аргументу параметра name
        """
        result = list()
        request = requests.get(self.url.format(param_name) + f"/?search={search_input}").json()
        if int(request["count"]):
            data_json = request["results"]
            for obj in data_json:
                data_class_obj = self.create_obj_data_class(param_name, obj)
                result.append(data_class_obj)

        self.register_log(self.url.format(param_name), filter_name=filter_name, param_name=param_name, arg_param="name",
                          value=search_input,
                          count_value=0, status_request=200, count_obj=len(result), user_id=user_id)
        return result

