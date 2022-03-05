from flask import Flask
from data.db_session import global_init, create_session
from data.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init("db/blogs.db")
    user = User(name="Пользователь 2", about="биография пользователя 2", email="email2@email.ru")
    session = create_session()
    session.add(user)
    session.commit()
    # app.run()


if __name__ == '__main__':
    main()
