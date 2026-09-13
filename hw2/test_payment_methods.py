from selenium.webdriver.common.by import By
import time

def test_payment_methods(driver):
    payment_methods_button = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_methods_button.click()
    payment_section = driver.find_element(By.XPATH, "//*[@id='rec1921734713']/div/div/div[5]/h2")
    time.sleep(1)
    payment_section.screenshot('lesson_2/payment.png')
    # driver.save_screenshot('lesson_2/payment1.png') # скриншот всей страницы