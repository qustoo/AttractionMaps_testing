from dataclasses import dataclass


@dataclass
class Map:
    id: int
    title: str
    description: str
    price: int
    photo_link: str


First_Map = Map(
    id=5,
    title="Карта маршрута",
    description="Оригинальная карта маршрута",
    price=1,
    photo_link="https://levencovka.ru/wp-content/uploads/2019/03/plan_new_full.jpg"

)

Second_Map = Map(
    id=10,
    title="Карта Местности",
    description="Оригинальная карта Местности",
    price=1,
    photo_link="https://s0.rbk.ru/v6_top_pics/resized/1200xH/media/img/2/52/756142415802522.jpg"

)
Maps = [First_Map, Second_Map]