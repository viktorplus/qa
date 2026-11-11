from selenium.webdriver.common.by import By
from locators import locator1, locator2
from urls import SITE1

def test_button(driver):
    driver.get(SITE1)
    input_field = driver.find_element(By.ID, locator1)
    input_field.send_keys("ITCH")
    button = driver.find_element(By.ID, locator2)
    button.click()
    assert button.text == "ITCH"

