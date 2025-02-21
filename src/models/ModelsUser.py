from .entities.User import User

class ModelUser():

    @classmethod
    def get_by_id(cls, db, id):
        try:
            cursor = db.connection.cursor()
            cursor.execute('SELECT id, username, email FROM users WHERE id = %s', (id,))
            data = cursor.fetchall()
            print(data)

            if data:
                user = User(data[0][0],data[0][2], None, data[0][1])
                return user
        except Exception as e:
            raise Exception(e)

    @classmethod
    def register(cls, db, password, email, username):
        try:
            hashed_pass = User.generate_hash(password)
            cursor = db.connection.cursor()
            cursor.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s)', (username, hashed_pass, email))
            db.connection.commit()

        except Exception as e:

            raise Exception(e)

    @classmethod
    def login(cls, db, password, username):

        try:
            cursor = db.connection.cursor()
            cursor.execute('SELECT id, email, username, password FROM users WHERE  username = %s', (username,))
            data = cursor.fetchone()
            print(data)

            if data:
                id = data[0]
                email = data[1]
                username = data[2]
                password = User.check_password(data[3], password)

                user = User(id, email, password, username)

                return user

        except Exception as e:
            raise Exception(e)

