# inorder to reuse the driver method we create a separate fixture which we can use commonly

from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver
