from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from hw5.locators import locator1, locator2
from hw5.urls import SITE1


def test_iframe(driver):
    driver.get(SITE1)
    iframe = driver.find_element(By.ID, locator1)
    driver.switch_to.frame(iframe)
    text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator2)))
    assert text.is_displayed()
