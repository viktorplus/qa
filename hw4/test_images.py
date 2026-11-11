from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from hw4.locators import locator3, locator4
from hw4.urls import SITE2


def test_images(driver):
    driver.get(SITE2)
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, locator3), "Done!"))
    images = driver.find_elements(By.CSS_SELECTOR, locator4)
    assert images[2].get_attribute("alt") == "award"
