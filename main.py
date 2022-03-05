from flask import Flask
from data.db_session import global_init, create_session
from data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init("db/mars.db")
    job = Jobs(team_leader=3, job='1', work_size=12, collaborators='1, 2', start_date=datetime.datetime.now(),
               is_finished=False)
    job2 = Jobs(team_leader=3, job='2', work_size=0, collaborators='1', start_date=datetime.datetime.now(),
                is_finished=True)
    job3 = Jobs(team_leader=3, job='deployment of residential modules 1 and 2', work_size=15, collaborators='2, 3',
                start_date=datetime.datetime.now(),
                is_finished=False)
    session = create_session()
    session.add(job)
    session.add(job3)
    session.add(job2)
    session.commit()
    # app.run()


if __name__ == '__main__':
    main()
