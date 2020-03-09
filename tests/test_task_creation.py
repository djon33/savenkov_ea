from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config_web import authorization
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def test_create_standard_task(drivers):
    authorization(
        drivers=drivers,
        username='Test1',
        password='Test1'
    )
    wait = WebDriverWait(drivers, 90)
    btn_element = drivers.find_element_by_xpath(
        "//a[@href='/mantisbt/bug_report_page.php'][1]")
    btn_element.click()
    select = Select(drivers.find_element_by_xpath(
        "//select[@id='reproducibility']"))
    select.select_by_value('10')
    select = Select(drivers.find_element_by_xpath(
        "//select[@id='severity']"))
    select.select_by_value('80')
    # btn_element = drivers.find_element_by_xpath(  #для JS
    #     "//a[@id='profile_open_link']")
    # drivers.execute_script("arguments[0].click();", btn_element)
    wait.until(EC.visibility_of_element_located((By.ID, 'platform')))
    drivers.find_element_by_id("platform").send_keys("MOAP(s)")
    drivers.find_element_by_id("os").send_keys("Symbian OS")
    drivers.find_element_by_id("os_build").send_keys("10.3")
    drivers.find_element_by_id("summary").send_keys(
        "Не работает проверка поля «e-mail» на содержание e-mail")
    drivers.find_element_by_id("description").send_keys(
        "Не выполняется проверка поля «e-mail» на то, что это действительно "
        "e-mail. Можно зарегистрироваться с любыми данными в этом поле.")
    drivers.find_element_by_id("steps_to_reproduce").send_keys(
        "1.	Открыть сайт с формой регистрации. \n"
        "2.	Ввести в поле «Email» адрес testmail.ru \n"
        "3.	Ввести в поле «Пароль» фразу test \n"
        "4.	Ввести в поле «Подтверждение пароля» фразу test \n"
        "5.	Нажать кнопку «Регистрация»")
    current_url = drivers.current_url
    btn_element = drivers.find_element_by_xpath(
        "//input[@type='submit']"
        "[@value='Создать задачу'][1]")
    btn_element.click()
    wait.until(EC.url_changes(current_url))
    current_url = drivers.current_url
    wait.until(EC.url_changes(current_url))
    assert "mantisbt/view.php?id=" in drivers.current_url
