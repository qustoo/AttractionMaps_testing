from loader import photo_db


# добавляем фотки
def do_db_photo(data_base_photo):
    data_base_photo.add_photo(r'quiz_all_files/Quiz_Photos/Easy_Photos/easy_question_1.jpg', "easy_question_1")
    data_base_photo.add_photo(r'quiz_all_files/Quiz_Photos/Easy_Photos/easy_question_2.jpg', "easy_question_2")
    data_base_photo.add_photo(r'quiz_all_files/Quiz_Photos/Easy_Photos/easy_question_3.jpg', "easy_question_3")
    data_base_photo.add_photo(r'quiz_all_files/Quiz_Photos/Easy_Photos/easy_question_4.jpg', "easy_question_4")
    data_base_photo.add_photo(r'quiz_all_files/Quiz_Photos/Easy_Photos/easy_question_5.jpg', "easy_question_5")
    data_base_photo.add_photo(r'quiz_all_files/Quiz_Photos/Easy_Photos/easy_question_55.jpg', "easy_question_55")
    photo_db.add_photo(r'quiz_all_files/Quiz_Photos/Easy_Photos/easy_question_44.jpg', "easy_question_44")
    return

# photos = photo_db.select_all_photos();
# print(f"БД: {photos=}")
# print(str(photo_db.select_photo(name="easy_question_5")[0]))
