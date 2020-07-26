import pytest
import pandas as pd
from selenium import webdriver  # Importing web driver

driver = None

#browser code for selecting different browser at run time :
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver  #defined driver as global so screenshot capture can use it
    browser_name = request.config.getoption("browser_name")      #browser code for selecting different browser at run time
    if browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="D:\Python_XDM\\geckodriver.exe")
    elif browser_name == "chrome":
        driver = webdriver.Chrome("D:\Python_XDM\\chromedriver.exe")

    driver.maximize_window()
    driver.get("https://xdme.wireless.att.com/jsp/login/login.jsp")  # open the web page provided
    driver.implicitly_wait(30)  # implicitly wait will wait for the events to occur
    print(driver.title)  # title of web page
    print(driver.current_url)  # url loaded to be printed
    excel = pd.read_excel(r"D:\Python_XDM\FOTA_Setup_Readme.xlsx", sheet_name=1)  # using pandas for calling excel
    username = excel.iloc[0, 2]  # used to locate values
    password = excel.iloc[1, 2]
    driver.find_element_by_name("LOGIN").send_keys(
        username)  # Username read from FOTA_Setup_readme.txt using name method
    print("Username entered")
    driver.find_element_by_css_selector("input[name='PASSWORD']").send_keys(
        password)  # enter password using css selector method
    print("Password entered")
    driver.find_element_by_xpath("//input[@type='submit']").click()  # to select the sumit button using xpath method
    if driver.current_url == "https://xdme.wireless.att.com/jsp/main/main.jsp":
        print("Login success")
    else:
        print("Invalid Login Please Try Again")
        print("Login failed - !!!XDM account will be blocked on three incorrect password.!!!")
        # driver.close()
    #assert driver.current_url == "https://xdme.wireless.att.com/jsp/main/main.jsp"
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)