import time


'''     uploading single files      '''

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# ac = ActionChains(driver)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ref_ele = driver.find_element('xpath', '//td[text()="Master In JS"]')
# ac.scroll_to_element(ref_ele).perform()
#
# file_path = r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\rep.html'
# driver.find_element('xpath', '//input[@id="singleFileInput"]').send_keys(file_path)

##-------------------------------------------------------------------------------------------------

'''     uploading multiple files      '''

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# ac = ActionChains(driver)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ref_ele = driver.find_element('xpath', '//td[text()="Master In JS"]')
# ac.scroll_to_element(ref_ele).perform()
# time.sleep(2)
#
# file1 = r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\css_selector.html'
# file2 = r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\css_selector_dup.html'
# file3 = r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\demo.html'
#
# driver.find_element('xpath', '//input[@id="multipleFilesInput"]').send_keys(f'{file1}\n{file2}\n{file3}')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Upload Multiple Files"]').click()

########################################################################################################

'''     file-download popup     '''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demoqa.com/upload-download')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Download"]').click()
# ## The file will be downloaded in the downloads folder

# ##------------------------------------------------------------------------------
#
# ## Chrome
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# prefs = {
#     "download.default_directory" : r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\notes',
#     "download.prompt_for_download":False,
#     "safebrowsing.enabled":True,
#     "plugins.always_open_pdf_externally":True
# }
#
# opts.add_experimental_option("prefs", prefs)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demoqa.com/upload-download')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Download"]').click()
#

'''
download.default_directory  -->     Sets the folder where the downloaded files will be stored
download.prompt_for_download    --> 
safebrowsing.enabled    -->     Enables Chromes's safe browsing so it doesnt block the download
'''

##------------------------------------------------------------------------------

## Firefox

from selenium import webdriver

opts = webdriver.FirefoxOptions()

opts.set_preference("browser.download.folderList", 2)
opts.set_preference("browser.download.dir", r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\screenshots')

driver = webdriver.Firefox(opts)

driver.get('https://demoqa.com/upload-download')
time.sleep(2)

driver.find_element('xpath', '//a[text()="Download"]').click()


'''
opts.set_preference("browser.download.folderList", 2)   --> This will tell the Firefox where to save the files  
    0   --> Download happens in desktop
    1   --> Dwwnload happens in Downloads default folder
    2   --> Custom folder(we can give the location)

opts.set_preference("browser.download.dir", r'')        --> This will set the custom location

'''

######################################################################################

''' verify if file is downloaded'''

import os

file_path = r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\screenshots\sampleFile.jpeg'

if os.path.exists(file_path):
    print("file downloaded")
else:
    print("file is not downloaded")


































































