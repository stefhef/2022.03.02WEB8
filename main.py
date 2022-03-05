from flask import Flask
from data.db_session import global_init, create_session
from data.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init("db/mars.db")
    user = User(name="Пользователь 1", surname='GHjjnj', age=16, position='Должность 1', speciality="Инженер",
                address='Земля', hashed_password='password',  email="email2@email.ru")
    user2 = User(name="Пользователь 2", surname='Фамилия', age=17, position='Должность 1', speciality="Медик",
                address='Марс', hashed_password='passwordXex', email="email1@email.ru")
    user3 = User(name="Ridley", surname='Scott', age=21, position='captain', speciality="research engineer",
                 address='module_1', hashed_password='passwordXexk', email="scott_chief@mars.org")

    user4 = User(name="Пользовательwgwg 2", surname='Фамилияwg', age=17, position='Должность fwfw1', speciality="Медик",
                 address='Марсwgwg', hashed_password='passwordXexrhr', email="emaileheh@email.ru")
    session = create_session()
    session.add(user)
    session.add(user2)
    session.add(user3)
    session.add(user4)
    session.commit()
    # app.run()


if __name__ == '__main__':
    main()
