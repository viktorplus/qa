from selenium.webdriver.common.by import By
import time

def test_payment_methods(driver):
    payment_methods_button = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_methods_button.click()
    payment_section = driver.find_element(By.XPATH, "/html/body/div[1]/div[34]/div")
    time.sleep(1)
    payment_section.screenshot('hw2/screenshots/payment.png')
    # driver.save_screenshot('hw2/screenshots/payment1.png') # скриншот всей страницы