import time
import inspect
import logging
import pytest
import openpyxl
import pandas as pd
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def selectProjectDetails(self):
        pass
        '''
        self.driver.find_element_by_link_text("Setup").click()  # to select setup text in main screen
        time.sleep(2)
        self.driver.find_element_by_link_text("Firmware").click()  # to select Firmware from sub text of Setup
        dropdown = Select(self.driver.find_element_by_xpath(
            "//select[@name ='GROUP_ID']"))  # To handle the drop options we are using select class method by importing Select
        dropdown.select_by_visible_text("ATT.SONIM")  # select ATT.SONIM from drop box
        dropdown = Select(self.driver.find_element_by_xpath("//select[@name='MANU_ID']"))  # selecting next drop down
        dropdown.select_by_visible_text("Sonim Technologies Inc")  # select Sonim Technologies Inc from drop box
        #dropdown = Select(self.driver.find_element_by_xpath("//select[@name='IMEI_ID']"))  # selecting next drop down
        #dropdown.select_by_visible_text("XP5800")  # select XP5800 from drop box
        '''

    def appSeverityMedium(self):
        dropdown = Select(self.driver.find_element_by_xpath("//select[@name ='APP_SEVERITY']"))
        time.sleep(2)
        dropdown.select_by_visible_text("Medium")  # select Medium from drop box
        time.sleep(2)

    def appSeverityHigh(self):
        dropdown = Select(self.driver.find_element_by_xpath("//select[@name ='APP_SEVERITY']"))
        time.sleep(2)
        dropdown.select_by_visible_text("High")
        time.sleep(2)

    def clickAddPackage(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath(
            "//input[@name='subBotton' and @value='Add']").click()  # for clicking upgrade radio buttion , commented bec by default its selected
        log.info("Package uploading started,please wait")

    def selectDowngrade(self):
        self.driver.find_element_by_xpath("//input[@name='UPGRADE' and @value='']").click()

    def verifyResult(self):
        log = self.getLogger()
        WebDriverWait(self.driver, 1800).until(
            EC.presence_of_element_located((By.XPATH, "//span[@name='null' and @value]")))
        output = self.driver.find_element_by_xpath("//span[@name='null' and @value]").text
        log.info(output)
        time.sleep(2)
        assert output == "     Firmware added successfully     "

    def verifyResult2hrTimeout(self):
        log = self.getLogger()
        WebDriverWait(self.driver, 7200).until(
            EC.presence_of_element_located((By.XPATH, "//span[@name='null' and @value]")))
        output = self.driver.find_element_by_xpath("//span[@name='null' and @value]").text
        log.info(output)
        time.sleep(2)
        assert output == "     Firmware added successfully     "

    def excelPathOf16038(self):
        excel = pd.read_excel(r"D:\Python_XDM\FOTA_Setup_Readme.xlsx", sheet_name=1)
        path = excel.iloc[3, 2]
        openpyxl.load_workbook(path)
        workbook = openpyxl.load_workbook(path)  # loading workbook from the path given
        sheet = workbook["Section 3 Packages (OMADM)"]  # Select particular sheet by name
        return sheet

    def packagesPathFromReadmeExcel(self):
        excel = pd.read_excel(r"D:\Python_XDM\FOTA_Setup_Readme.xlsx", sheet_name=1)
        return excel
