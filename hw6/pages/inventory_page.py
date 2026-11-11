from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    ADD_TO_CART_BUTTON = "//div[text()='{}']/ancestor::div[@class='inventory_item']//button"
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, product_name):
        locator = (By.XPATH, self.ADD_TO_CART_BUTTON.format(product_name))
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
