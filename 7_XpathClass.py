import time
from selenium import webdriver

browser = 'firefox'

if browser == 'chrome':
    driver = webdriver.Chrome(executable_path="C:/Users/rahul/Downloads/chromedriver_win32/chromedriver.exe")
    # driver = webdriver.Chrome()
    # driver.get("https://www.makemytrip.com/")
elif browser == 'firefox':
    driver = webdriver.Firefox(executable_path="C:/Users/rahul/Downloads/geckodriver-v0.24.0-win64/geckodriver.exe")
    # driver = webdriver.Firefox()
    # driver.get("https://www.makemytrip.com/")
elif browser == 'ie':
    driver = webdriver.Ie(executable_path="C:/Users/Harish/Downloads/IEDriverServer_Win32_3.14.0/IEDriverServer.exe")
    # driver = webdriver.Ie()
else:
    print("Error - Provide appropriate browser name")
driver.get("http://facebook.com")
driver.find_element_by_xpath("//input[@class='inputtext' and @name='email']").send_keys("Hello")
driver.find_element_by_xpath("//input[@type='password']").send_keys("password")
driver.find_element_by_xpath("//a[contains(text(),'Forgotten account?')]").click()


