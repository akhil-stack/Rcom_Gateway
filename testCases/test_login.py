import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin:
    baseUrl = "https://rcom-gateway-test.com/RCOMUI/#/login"
    client = "Data Elektronik"
    username = "admin@data-elektronik.de"
    password = "1234"

    @pytest.fixture(autouse=True)
    def setup(self):
        # Force WebDriver Manager to re-download the driver
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)

        # Initialize the WebDriver with the service object
        self.driver = webdriver.Chrome(service=service)

        # Maximize the window to ensure visibility of the web page
        self.driver.maximize_window()

        # Yield driver for the tests
        yield
        self.driver.quit()

    def test_homepagetitle(self):
        self.driver.get(self.baseUrl)
        assert self.driver.title == "RCOM Gateway", f"Title mismatch: {self.driver.title}"

    #def test_login(self):
    #    self.driver.get(self.baseUrl)
        # Your login steps here
       # assert self.driver.title == "AI² by MHP", f"Title mismatch: {self.driver.title}"
