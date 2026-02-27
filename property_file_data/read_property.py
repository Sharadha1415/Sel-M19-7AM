import time
from configparser import ConfigParser

config = ConfigParser()

config.read(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\property_file_data\config.properties')

url = config["DEFAULT"]["url"]
browser = config["DEFAULT"]["browser"]
username = config["DEFAULT"]["username"]
password = config["DEFAULT"]["password"]

##-------------------------------------------------------------------------------------------

from selenium import webdriver

if browser == 'chrome':
    driver = webdriver.Chrome()
elif browser == 'firefox':
    driver = webdriver.Firefox()
elif browser == "edge":
    driver = webdriver.Edge()

driver.get(url)
time.sleep(1)
driver.find_element('id', 'user-name').send_keys(username)
time.sleep(1)
driver.find_element('id', 'password').send_keys(password)
time.sleep(1)
driver.find_element('id', 'login-button').click()



































































