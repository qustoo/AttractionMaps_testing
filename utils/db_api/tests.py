from  utils.db_api.sqlite import Database

db = Database("test.db")

def test():
    db.create_table_users()
    users = db.select_all_users()
    print(f"До добавления: {users=}")
    db.add_user(1, "Vasya")
    users = db.select_all_users()
    print(f"После добавления: {users=}")


test()
