import math, re
from utils.misc import show_on_gmaps
from aiogram import types

from data.locations import Attractions

# Радиус земли
R = 6378.1

New_Attract = Attractions.copy()


# Функция сброса карты
def SetTrueForAllAttractions(List_Attractions):
    index = 0
    for i in List_Attractions:
        List_Attractions[index] = (
            List_Attractions[index][0], {'lat': List_Attractions[index][1]['lat'],
                                         'lon': List_Attractions[index][1]['lon'],
                                         'bypass': True})
        index += 1


# поиск индекса объекта в листе словарей
def find_locale(name_object, Attract_List):
    for i in range(0, len(Attract_List)):
        if name_object == Attract_List[i][0]:
            return i


# вычисляем расстояние
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


def choose_nearest(lat, lon, List_Attractions, name_object):
    distances = list()
    for place_name, place_location in List_Attractions:
        # Если обход по локации True
        if place_location['bypass'] and re.search(name_object, place_name, re.IGNORECASE) is not None:
            distances.append((place_name,
                              calc_distance(lat, lon,
                                            place_location["lat"],
                                            place_location["lon"]),
                              show_on_gmaps.show(place_location['lat'], place_location['lon']),
                              place_location
                              ))

    # формируем список, в которым лежит: (название_объекта, расстояние_до_него, ссылка на гугл_карту, {координаты, обход})
    res_lis = sorted(distances, key=lambda x: x[1])[0:1]
    # print('собранный список ', res_lis)

    # если флаг прохода = True, меняем его на false в Attractions и в res_lis
    try:
        name_of_found_place = res_lis[0][0]
        index = find_locale(name_of_found_place, Attract_List=List_Attractions)
        # print('индекс локации ', List_Attractions[index][-1])
        if List_Attractions[index][-1].get('bypass'):
            List_Attractions[index] = (List_Attractions[index][0], {'lat': List_Attractions[index][1]['lat'],
                                                                    'lon': List_Attractions[index][1]['lon'],
                                                                    'bypass': False})
            # устанавливаем, что мы прошли этот объект
            res_lis[-1][-1]['bypass'] = False
            # print('test_Attractions after false =', List_Attractions)
    # ловим ошибку пустого листа, когда все объекты пройдены
    except Exception as err:
        print(err)

    return res_lis
