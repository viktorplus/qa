from hw6.pages import LoginPage, InventoryPage, CartPage, CheckoutInfoPage, CheckoutOverviewPage


def test_checkout_total(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_to_cart("Sauce Labs Onesie")
    inventory_page.open_cart()

    CartPage(driver).checkout()
    CheckoutInfoPage(driver).fill_form("Ivan", "Petrov", "10115")
    total = CheckoutOverviewPage(driver).get_total()

    assert total == "Total: $58.29"
