from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config_web import check_exists_by_xpath


def test_standard_user(cursor_with_del, drivers):

    drivers.get("http://localhost/mantisbt/login_page.php")
    btn_element = drivers.find_element_by_xpath(
        "//a[@class='back-to-login-link pull-left'][1]")
    btn_element.click()
    current_url = drivers.current_url
    drivers.find_element_by_id("username").send_keys("Test_User2")
    drivers.find_element_by_id("email-field").send_keys("test_reg2@mail.ru")
    btn_element = drivers.find_element_by_xpath("//input[@type='submit']"
                                               "[@value='Зарегистрироваться']"
                                               "[1]")
    btn_element.click()
    wait = WebDriverWait(drivers, 90)
    wait.until(EC.url_changes(current_url))
    assert check_exists_by_xpath(drivers,
                                 "//*[.='Учётная запись зарегистрирована.']")
