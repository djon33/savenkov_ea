import requests
import pymysql


def get_session():
    session = requests.Session()
    session.auth = ('root', 'root')
    return session


def get_connect_my_sql(
                host='localhost',
                user='user',
                password='password',
                db='iata',
                charset='utf8mb4'
            ):
    return pymysql.connect(host=host, user=user, password=password, db=db
                           , port=3306, charset=charset, autocommit=True
                           )
