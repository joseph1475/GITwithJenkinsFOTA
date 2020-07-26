from selenium.webdriver.common.by import By

class XDMdetailsFrom16038:
    def __init__(self, driver):
        self.driver = driver

#self.driver.find_element_by_name("APP_NAME").send_keys(file_name)
    XDMappname =(By.NAME,"APP_NAME")
    def appname(self):
        return self.driver.find_element(*XDMdetailsFrom16038.XDMappname)

#self.driver.find_element_by_name("APP_DESC").send_keys(file_description)
    XDMappdesc =(By.NAME,"APP_DESC")
    def appdesc(self):
        return self.driver.find_element(*XDMdetailsFrom16038.XDMappdesc)

#self.driver.find_element_by_xpath("//input[@name='uplfile']").send_keys(path)
    XDMuplfile = (By.XPATH,"//input[@name='uplfile']")
    def uplfile(self):
        return self.driver.find_element(*XDMdetailsFrom16038.XDMuplfile)

#self.driver.find_element_by_name("SOURCE_VERSION").send_keys(source_version)
    XDMsourceversion = (By.NAME,"SOURCE_VERSION")
    def sourceversion(self):
        return self.driver.find_element(*XDMdetailsFrom16038.XDMsourceversion)

#self.driver.find_element_by_name("TARGET_VERSION").send_keys(target_version)
    XDMtargetversion = (By.NAME,"TARGET_VERSION")
    def targetversion(self):
        return self.driver.find_element(*XDMdetailsFrom16038.XDMtargetversion)