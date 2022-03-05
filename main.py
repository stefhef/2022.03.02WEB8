from flask import Flask
from data.db_session import global_init, create_session
from data.jobs import Jobs
import datetime

from data.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main(db_name):
    # db_name = "db/mars.db"
    global_init(db_name)

    session = create_session()
    for user in session.query(User).filter(User.address == 'module_1').all():
        print(user)
    session.commit()
    # app.run()


if __name__ == '__main__':
    main(input())
