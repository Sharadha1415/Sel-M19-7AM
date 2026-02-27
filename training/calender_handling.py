import time

# ## SOLUTION 1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.makemytrip.com/")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
# time.sleep(3)
#
# driver.find_element('xpath', '//span[text()="Departure"]').click()
# time.sleep(2)
#
# while True:
#     current_month = driver.find_element('xpath', '(//div[@class="DayPicker-Caption"])[1]')
#     print(current_month.text)       ## Jan
#
#     if current_month.text == 'November 2026':           ## Jan == Nov
#         driver.find_element('xpath', '(//p[text()="30"])[1]').click()
#         break
#     else:
#         driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()

'''
month = Jan, Jan==Nov --> False -->     next month
month = Feb, Feb==Nov --> False -->     next month
month = Mar, Mar==Nov --> False -->     next month
month = Apr, Apr==Nov --> False -->     next month
month = May, May==Nov --> False -->     next month
month = Jun, Jun==Nov --> False -->     next month
..
..
..
month = Nov, Nov==Nov --> True  -->     select the date
'''

####################################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(2)

driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
time.sleep(3)

driver.find_element('xpath', '//span[text()="Departure"]').click()
time.sleep(2)

while True:
    try:
        driver.find_element('xpath', '//div[text()="November 2026"]/../..//p[text()="30"]').click()
        break
    except:
        driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()







































































