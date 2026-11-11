import pytest
from selenium import webdriver
from hw3.urls import HOMEPAGE


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOMEPAGE)

    yield driver

    driver.quit()