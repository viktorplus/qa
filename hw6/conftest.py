import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # Chrome shows a "password found in a data breach" dialog after login,
    # it steals focus and the clicks on the page stop working
    options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
