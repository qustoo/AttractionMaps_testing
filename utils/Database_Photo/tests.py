from  utils.Database_Photo.sqlite_photo import PhotoDatabase

db = PhotoDatabase("test.db")


def test():
    db.create_table_photos()
    photos = db.select_all_photos()
    print(f"До добавления: {photos=}")
    db.add_photo("001.jpg", "Улица Красная")
    db.add_photo("002.jpg", "Улица Красная")
    db.add_photo("003.jpg", "Улица Советская")
    db.add_photo("004.jpg", "Парк Горького")
    photos = db.select_all_photos()
    print(f"После добавления: {photos=}")
    selected_photos = db.select_photos(name="Улица Красная")
    print(f"Найденные фото: {selected_photos=}")
    db.update_name("002.jpg", "Улица Синяя")
    db.update_region("003.jpg", "Центр")
    db.update_region("001.jpg", "Западный")
    photos = db.select_all_photos()
    print(f"После обновления: {photos=}")

    db.delete_photo_by_filename("004.jpg")
    photos = db.select_all_photos()
    print(f"После удаления: {photos=}")
    print(f"Имя файла Улица Советская: {db.get_one_file_name(name='Улица Советская')}")


test()