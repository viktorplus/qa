from selenium.webdriver.common.by import By
from locators import (locator_2_program,
                      locator_3_payment,
                      locator_4_about,
                      locator_5_contacts,
                      locator_6_reviews,
                      locator_7_blog
                      )

def test_links(driver):
    program = driver.find_element(By.XPATH, value=locator_2_program)
    # assert program.is_displayed()
    assert program.text == "Программы"

    payment = driver.find_element(By.XPATH, value=locator_3_payment)
    assert payment.text == "Способы оплаты"

    about = driver.find_element(By.XPATH, locator_4_about)
    assert about.is_displayed()
    assert about.text == "О нас"

    contacts = driver.find_element(By.XPATH, locator_5_contacts)
    assert contacts.is_displayed()
    assert contacts.text == "Контакты:"

    reviews = driver.find_element(By.XPATH, locator_6_reviews)
    assert reviews.is_displayed()
    assert reviews.text == "Отзывы"

    blog = driver.find_element(By.XPATH, locator_7_blog)
    assert blog.is_displayed()
    assert blog.text == "Блог"
