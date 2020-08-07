from selenium.webdriver.common.by import By


class XDMSumit:
    def __init__(self,driver):
        self.driver = driver

    add = (By.XPATH,"//input[@name='subBotton' and @value='Add']")

    def AddPackage(self):
        return self.driver.find_element(*XDMSumit.add)

