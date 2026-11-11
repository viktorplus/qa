import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from locators import (locator_4_about,
                      locator_10_contacts_link,
                      locator_11_callback,
                      locator_12_popup_text
                      )


def test_contacts_callback(driver):
    driver.find_element(By.XPATH, locator_4_about).click()
    time.sleep(2)
    driver.find_element(By.XPATH, locator_10_contacts_link).click()
    time.sleep(2)

    callback = driver.find_element(By.XPATH, locator_11_callback)
    # СПОСОБ РЕШИТЬ ПРОБЛЕМУ С КЛИКОМ ПО КНОПКЕ "ОБРАТНЫЙ ЗВОНОК" (кнопка перекрыта футером)
    from selenium.webdriver import ActionChains
    ActionChains(driver).move_to_element_with_offset(callback, 50, 0).click().perform()
    time.sleep(2)
    popup = driver.find_element(By.XPATH, locator_12_popup_text)
    assert popup.text == "Запишитесь на бесплатную карьерную консультацию"
