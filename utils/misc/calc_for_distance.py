import math

from utils.misc import show_on_gmaps
from aiogram import types

from data.locations import Attractions, find_locale

# Радиус земли
R = 6378.1

New_Attract = Attractions.copy()


def calc_distance(lat1, lon1, lat2, lon2):
    # Преобразовываем
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)

    lat2 = math.radians(float(lat2))
    lon2 = math.radians(float(lon2))

    delta_lon = lon2 - lon1
    delta_lat = lat2 - lat1

    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Итоговое расстояние
    distance = R * c

    return distance


def choose_nearest(message: types.Message, latt, lonn, List_Attractions):
    distances = list()
    for place_name, place_location in List_Attractions:
        distances.append((place_name,
                          calc_distance(latt, lonn,
                                        place_location["lat"],
                                        place_location["lon"]),
                          show_on_gmaps.show(**place_location),
                          place_location
                          ))
    # забираем две ближайшие позиции по долготе и широте
    res_lis = sorted(distances, key=lambda x: x[1])[0:1]

    # передаем имя и список в функцию, получаем нужный индекс
    try:
        index = find_locale(res_lis[0][0], Attract_List=New_Attract)
        print('attraction index = ', index)
        New_Attract.remove(New_Attract[index])
        print('After delete = ', New_Attract)
    except IndexError as index_error:
        print('Ошибка = ', index_error)

    # печатаем список
    print('Список мест=', New_Attract, "\n")

    # возвращаем нужный список
    return res_lis
