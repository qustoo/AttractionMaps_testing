URL = "http://maps.google.com/maps?q={lat},{lon}"


def show(lat, lon):
    return URL.format(lat=lat, lon=lon)


Attractions_test = [
    ("Церковь Екатерины Великомученицы", {
        "lat": 47.200084,
        "lon": 39.629942
    })]

# так возвращаем название
# print(Attractions_test[0][1])

# так возвращаем lat
# print(Attractions_test[0][1]["lat"])

# так возвращаем lon
# print(Attractions_test[0][1]["lon"])

# print(show(Attractions_test[0][1]["lat"],Attractions_test[0][1]["lon"]))
