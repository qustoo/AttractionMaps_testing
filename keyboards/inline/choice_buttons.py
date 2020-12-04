from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Купить \nкарту местности: ",
                                          callback_data=buy_callback.new(item_name="terrain_map", quantity=2
                                                                         )
                                      ),
                                      InlineKeyboardButton(
                                          text="Купить \nкарту маршрутов: ",
                                          callback_data=buy_callback.new(item_name="route_map", quantity=3
                                                                         )

                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Отмена",
                                          callback_data="cancel"
                                      )

                                  ],
                              ]
                              )
# url на карту местности
pear_keyboard_terrain = InlineKeyboardMarkup()

Map_Link_terrain = "https://img.tourister.ru/files/3/0/0/8/2/5/1/original.gif"

map_link_terrain = InlineKeyboardButton(text="Ссылка на товар: ", url=Map_Link_terrain)

pear_keyboard_terrain.insert(map_link_terrain)


# url на карту маршрутов
pear_keyboard_route = InlineKeyboardMarkup()

Map_link_route = "https://regnum.ru/uploads/pictures/news/2016/10/12/regnum_picture_1476263204584409_normal.jpg"


map_link_route = InlineKeyboardButton(text="Ссылка на товар: ", url=Map_link_route)

pear_keyboard_route.insert(map_link_route)


