
def test_standard_user(drivers):

    drivers.get("http://localhost/mantisbt/login_page.php")
    drivers.find_element_by_id("username").send_keys("Test1")
    btn_element = drivers.find_element_by_xpath(
        "//input[@class="
        "'width-40 pull-right btn btn-success btn-inverse bigger-110']"
        "[@value='Войти'][1]")
    btn_element.click()
    drivers.find_element_by_id("password").send_keys("Test1")
    btn_element = drivers.find_element_by_xpath("//input[@type='submit']"
                                                "[@value='Войти'][1]")
    btn_element.click()
    assert "mantisbt/my_view_page.php" in drivers.current_url
