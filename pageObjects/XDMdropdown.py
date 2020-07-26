from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class XDMdropdown:
    def __init__(self, driver):
        self.driver = driver

    XDMsetup = (By.LINK_TEXT, "Setup")  # tupple

    def dropdowns(self):
        return self.driver.find_element(*XDMdropdown.XDMsetup)
        # self.driver.find_element_by_link_text("Setup").click()

    XDMfirmware = (By.LINK_TEXT, "Firmware")

    def firmware(self):
        return self.driver.find_element(*XDMdropdown.XDMfirmware)
        # self.driver.find_element_by_link_text("Firmware").click()

"""
Class Homepage:

    shop=(By.CSS_SELECTOR,"actual css selector")  #shop is object
    def shopItems(self):   #create a method
        return self.driver.find_element(*Homepage.shop)  #class name.object and use * to treat as tupile

#in main program
homepage = Homepage(self.driver)
#homepage is new object = class name (driver)
homepage.shopItems().click
#new object.Method.action
"""


