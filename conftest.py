import pytest
from config_sql import get_session, get_connect_my_sql
from db_clearing import clear_all_data
from selenium import webdriver


@pytest.fixture(scope='session')
def session():
    print('Фикстура')
    return get_session()


@pytest.fixture(scope='session')
def connect():
    conn = get_connect_my_sql(
        host='localhost',
        user='root',
        password='',
        db='bugtracker',
        charset='utf8mb4'
    )
    yield conn
    conn.close()


@pytest.fixture(scope='function')
def cursor_with_del(connect):
    cur = connect.cursor()
    clear_all_data(cur, 'Test_User2')
    yield cur   # выступает в роли return. Ниже отработает после завершения ТК
    clear_all_data(cur, 'Test_User2')
    cur.close()


@pytest.fixture(scope='function')
def drivers():
    driver = webdriver.Firefox(
        executable_path="C:\\Users\\djon\\PycharmProjects"
                        "\\seleniumTest\\drivers\\geckodriver.exe")
    yield driver
    driver.quit()

