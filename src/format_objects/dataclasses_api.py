from dataclasses import dataclass
from .formatter_text_object import text


@dataclass
class PeopleDataCass:

    """Класс для хранения данных по people"""

    birth_year: str
    eye_color: str
    films: list
    gender: str
    hair_color: str
    height: str
    homeworld: str
    mass: str
    name: str
    skin_color: str
    created: str
    edited: str
    species: list
    starships: list
    url: str
    vehicles: str

    def get_text(self, flag) -> str:
        """
        getter текста по флагу
        getter выдаёт текст в формате json или просто читабельный текст в зависимости от флага
        :param flag:
        :return:
        """
        type_text = "people"
        if flag:
            type_text += "_json"
        return text[type_text].format(
            birth_year=self.birth_year,
            eye_color=self.eye_color,
            films=self.films,
            gender=self.gender,
            hair_color=self.hair_color,
            height=self.height,
            homeworld=self.homeworld,
            mass=self.mass,
            name=self.name,
            skin_color=self.skin_color,
            created=self.created,
            edited=self.edited,
            species=self.species,
            starships=self.starships,
            url=self.url,
            vehicles=self.vehicles,
        )


@dataclass
class StarshipsDataClass:

    """Класс для хранения данных о звездалёте"""

    MGLT: str
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    created: str
    crew: str
    edited: str
    hyperdrive_rating: str
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    passengers: str
    films: list
    pilots: list
    starship_class: str
    url: str

    def get_text(self, flag: bool) -> str:
        """
        getter текста по флагу
        getter выдаёт текст в формате json или просто читабельный текст в зависимости от флага
        :param flag:
        :return:
        """
        type_text = "starship"
        if flag:
            type_text += "_json"
        return text[type_text].format(
            MGLT=self.MGLT,
            cargo_capacity=self.cargo_capacity,
            consumables=self.consumables,
            cost_in_credits=self.cost_in_credits,
            created=self.created,
            crew=self.crew,
            edited=self.edited,
            hyperdrive_rating=self.hyperdrive_rating,
            length=self.length,
            manufacturer=self.manufacturer,
            max_atmosphering_speed=self.max_atmosphering_speed,
            model=self.model,
            name=self.name,
            passengers=self.passengers,
            films=self.films,
            pilots=self.pilots,
            starship_class=self.starship_class,
            url=self.url,
        )


@dataclass
class VehiclesDataClass:

    """Класс для хранения данных о технике"""

    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    created: str
    crew: str
    edited: str
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    passengers: str
    pilots: list
    films: list
    url: str
    vehicle_class: str

    def get_text(self, flag: bool) -> str:
        """
        getter текста по флагу
        getter выдаёт текст в формате json или просто читабельный текст в зависимости от флага
        :param flag:
        :return:
        """
        type_text = "vehicles"
        if flag:
            type_text += "_json"
        return text[type_text].format(
            cargo_capacity=self.cargo_capacity,
            consumables=self.consumables,
            cost_in_credits=self.cost_in_credits,
            created=self.created,
            crew=self.crew,
            edited=self.edited,
            length=self.length,
            manufacturer=self.manufacturer,
            max_atmosphering_speed=self.max_atmosphering_speed,
            model=self.model,
            name=self.name,
            passengers=self.passengers,
            pilots=self.pilots,
            films=self.films,
            url=self.url,
            vehicle_class=self.vehicle_class,
        )


@dataclass
class SpeciesDataClass:

    """Класс для хранения данных о разновидности"""

    average_height: str
    average_lifespan: str
    classification: str
    created: str
    designation: str
    edited: str
    eye_colors: str
    hair_colors: str
    homeworld: str
    language: str
    name: str
    people: list
    films: list
    skin_colors: str
    url: str

    def get_text(self, flag: bool) -> str:
        """
        getter текста по флагу
        getter выдаёт текст в формате json или просто читабельный текст в зависимости от флага
        :param flag:
        :return:
        """
        type_text = "species"
        if flag:
            type_text += "_json"
        return text[type_text].format(
            average_height=self.average_height,
            average_lifespan=self.average_lifespan,
            classification=self.classification,
            created=self.created,
            designation=self.designation,
            edited=self.edited,
            eye_colors=self.eye_colors,
            hair_colors=self.hair_colors,
            homeworld=self.homeworld,
            language=self.language,
            name=self.name,
            people=self.people,
            films=self.films,
            skin_colors=self.skin_colors,
            url=self.url,
        )


@dataclass
class PlanetsDataClass:

    """Класс для хранения данных о планетах"""

    climate: str
    created: str
    diameter: str
    edited: str
    films: list
    gravity: str
    name: str
    orbital_period: str
    population: str
    residents: list
    rotation_period: str
    surface_water: str
    terrain: str
    url: str

    def get_text(self, flag: bool) -> str:
        """
        getter текста по флагу
        getter выдаёт текст в формате json или просто читабельный текст в зависимости от флага
        :param flag:
        :return:
        """
        type_text = "planet"
        if flag:
            type_text += "_json"
        return text[type_text].format(
            climate=self.climate,
            created=self.climate,
            diameter=self.diameter,
            edited=self.edited,
            films=self.films,
            gravity=self.gravity,
            name=self.name,
            orbital_period=self.orbital_period,
            population=self.population,
            residents=self.residents,
            rotation_period=self.rotation_period,
            surface_water=self.surface_water,
            terrain=self.terrain,
            url=self.url,
        )
