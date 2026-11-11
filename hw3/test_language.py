from selenium.webdriver.common.by import By
from hw3.locators import locator_8_lang_ru, locator_9_lang_de


def test_language(driver):
    ru = driver.find_element(By.XPATH, locator_8_lang_ru)
    assert ru.is_displayed()

    de = driver.find_element(By.XPATH, locator_9_lang_de)
    assert de.is_displayed()
