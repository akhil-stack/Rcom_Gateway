# Create a Page Object Class
import self
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login :
    def __init__(self, driver):
     self.driver = driver
     self.dropdown_menu_button = (By.ID, "dropdownMenuButton1")
     self.dropdown_option = (By.XPATH, "//a[contains(text(), 'Data Elektronik')]")
     self.username_field = (By.XPATH, "//input[@placeholder='Username']")
     self.password_field = (By.XPATH, "//input[@placeholder='Password']")
     self.login_button = (By.XPATH, "//input[@value='Login']")
    
    def select_client(self):
        dropdown = self.driver.find_element(*self.dropdown_menu_button)
        
    def select_client_option(self):
        option = self.driver.find_element(*self.dropdown_option)
        
    
    def enter_username(self, username):
        username_element = self.driver.find_element(*self.username_field)
        username_element.send_keys(username)

    def enter_password(self, password):
        password_element = self.driver.find_element(*self.password_field)
        password_element.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()
    def click(self, dropdown_menu_button):
        pass

    def enter_text(self, username_field, username):
        pass

    def clickdropdown_menu_button(self):
        pass

    def clickLogin(self):
        pass

    def clickdropdown_option(self):
        pass
