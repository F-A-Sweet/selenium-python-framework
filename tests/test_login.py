from pages.login_page import LoginPage

def test_login(driver):

    driver.get("https://opensource-demo.orangehrmlive.com/")

    login = LoginPage(driver)

    login.login("Admin", "admin123")

    assert "dashboard" in driver.current_url.lower()