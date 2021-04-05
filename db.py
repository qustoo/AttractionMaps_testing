from utils.Database_Photo.sqlite_photo import PhotoDatabase
photo_db = PhotoDatabase()

photo_db.create_table_photos()

photo_db.add_photo(r'quiz_all_files/Quiz_Photos/Easy_Photos/easy_question_1.jpg', "easy_question_1")
photo_db.add_photo(r'quiz_all_files/Quiz_Photos/Easy_Photos/easy_question_2.jpg', "easy_question_2")
photo_db.add_photo(r'quiz_all_files/Quiz_Photos/Easy_Photos/easy_question_3.jpg', "easy_question_3")
photo_db.add_photo(r'quiz_all_files/Quiz_Photos/Easy_Photos/easy_question_4.jpg', "easy_question_4")

photos = photo_db.select_all_photos();
print(f"БД: {photos=}")