'''
location    :   This is a property
                Gives the x and y co-ordinates of the element on the page
                SYNTAX  :   web_element.location

size        :   This is a property
                This gives the height and width of the web-element
                SYNTAX  :   web_element.size

rect        :   This is a property
                Combination of location and size
                SYNTAX  :   web_element.rect
'''

import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)
reg = driver.find_element('xpath', '//a[text()="Register"]')
print(reg.location)         ## {'x': 673, 'y': 70}
print(reg.size)             ## {'height': 19, 'width': 55}
print(reg.rect)             ## {'height': 19, 'width': 55, 'x': 673.2625122070312, 'y': 70}
























