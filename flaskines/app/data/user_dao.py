from app.data.models.user import User

class UserDao:
    def select_all(self,db) -> list[User]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM usuarios')
        users_en_db = cursor.fetchall()
        users : list[User]=list()
        for user_en_db in users_en_db:
           users.append(User(user_en_db[0],user_en_db[1],user_en_db[2],user_en_db[3] ))
        cursor.close()
        return users