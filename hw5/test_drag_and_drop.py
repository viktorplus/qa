from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from hw5.locators import locator3, locator4, locator5, locator6, locator7
from hw5.urls import SITE2


def test_drag_and_drop(driver):
    driver.get(SITE2)
    iframe = driver.find_element(By.CSS_SELECTOR, locator3)
    driver.switch_to.frame(iframe)

    photo = driver.find_element(By.XPATH, locator4)
    trash = driver.find_element(By.ID, locator5)
    ActionChains(driver).drag_and_drop(photo, trash).perform()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locator6)))
    assert len(driver.find_elements(By.XPATH, locator6)) == 1
    assert len(driver.find_elements(By.XPATH, locator7)) == 3
