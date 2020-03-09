from selenium.common.exceptions import NoSuchElementException


"""
Проверка на существование элемента.
Поиск выполняется по всей странице. Например: 
search = "//*[.='Учётная запись зарегистрирована.']"
"""


def check_exists_by_xpath(drivers, search):
    try:
        drivers.find_element_by_xpath(search)
    except NoSuchElementException:
        return False
    return True


"""
Автоматическая авторизация.
"""


def authorization(drivers, username, password):
    drivers.get("http://localhost/mantisbt/login_page.php")
    drivers.find_element_by_id("username").send_keys(username)
    btn_element = drivers.find_element_by_xpath(
        "//input[@class="
        "'width-40 pull-right btn btn-success btn-inverse bigger-110']"
        "[@value='Войти'][1]")
    btn_element.click()
    drivers.find_element_by_id("password").send_keys(password)
    btn_element = drivers.find_element_by_xpath("//input[@type='submit']"
                                                "[@value='Войти'][1]")
    btn_element.click()

