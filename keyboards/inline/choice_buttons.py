from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_datas import buy_callback

choice = InlineKeyboardMarkup(
    # 2 кнопки в сообщение
    row_width=2, inline_keyboard=
    [
        [
            InlineKeyboardButton
                (
                text="Карты метности:",
                callback_data=buy_callback.new(item_name="terrain_map", skale=5000)
            ),
            InlineKeyboardButton
                (
                text="Карты маршрута:",
                callback_data=buy_callback.new(item_name="route_map", skale=1000)
            )
        ],
        [
            InlineKeyboardButton
                (
                text="Отмена",
                callback_data="cancel"
            )

        ],
    ]
)
# создаем клавы
pear_keyboard_terrain = InlineKeyboardMarkup()

# url на карту местности
TERRAIN_MAP_LINK = "https://img.tourister.ru/files/3/0/0/8/2/5/1/original.gif"

terrain_map_keyboard = InlineKeyboardButton(text="Открыть карту: ", url=TERRAIN_MAP_LINK)

# вставляем кнопки в клаву
pear_keyboard_terrain.insert(terrain_map_keyboard)

# создаем клавы
pear_keyboard_route = InlineKeyboardMarkup()

# url на карту маршрутов
ROUTE_MAP_LINK = "https://regnum.ru/uploads/pictures/news/2016/10/12/regnum_picture_1476263204584409_normal.jpg"

route_map_link = InlineKeyboardButton(text="Открыть карту: ", url=ROUTE_MAP_LINK)

# вставляем кнопки в клаву
pear_keyboard_route.insert(route_map_link)
