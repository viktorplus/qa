from selenium.webdriver.common.by import By
from locators import locator_1_ich_logo

def test_logo(driver):
    logo = driver.find_element(By.XPATH, locator_1_ich_logo)
    assert logo.is_displayed()

