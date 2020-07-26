"""
Password,user name and 16038 file path is selected from excel sheet
FOTA Package path is selected from excel sheet

"""
from pageObjects.XDMdetailsFrom16038 import XDMdetailsFrom16038
from utilities.BaseClass import BaseClass


class TestFOTA(BaseClass):
    def test_200MB(self):
        try:
            log = self.getLogger()
            self.selectProjectDetails()
            sheet = self.excelPathOf16038()
            log.info("Updating 200MB package details")
            file_name = sheet['h23'].value
            log.info(file_name)
            file_description = sheet['i23'].value
            log.info(file_description)
            source_version = sheet['c23'].value
            log.info(source_version)
            target_version = sheet['e23'].value
            log.info(target_version)
            filename = XDMdetailsFrom16038(self.driver)
            filename.appname().send_keys(file_name)
            FileDescription = XDMdetailsFrom16038(self.driver)
            FileDescription.appdesc().send_keys(file_description)
            excel = self.packagesPathFromReadmeExcel()
            path = excel.iloc[15, 2]
            log.info(path)
            uploadfile = XDMdetailsFrom16038(self.driver)
            uploadfile.uplfile().send_keys(path)
            SourceVersion = XDMdetailsFrom16038(self.driver)
            SourceVersion.sourceversion().send_keys(source_version)
            TargetVersion = XDMdetailsFrom16038(self.driver)
            TargetVersion.targetversion().send_keys(target_version)
            self.appSeverityMedium()
        except Exception:
            log.info("upload failed")
            log.info("=============moving to next upload !!!=============")
        finally:
            self.clickAddPackage()
            self.verifyResult()
