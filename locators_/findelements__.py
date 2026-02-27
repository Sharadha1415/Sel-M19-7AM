import time


'''
1.  wap to fetch the elements present in the footer of https://demowebshop.tricentis.com/
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# footer_elements = driver.find_elements('xpath', '//div[@class="footer-menu-wrapper"]//a')
# # print(footer_elements)      ## list of web-elements     ## [wb1, wb2, wb3, wb4, wb5, wb6,...wb22]
#
# for ele in footer_elements:
#     print(ele.text)

##############################################################################################

'''
2.  wap to fetch the elements present in the categories of https://demowebshop.tricentis.com/
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# categories = driver.find_elements('xpath', '//div[@class="block block-category-navigation"]//a')
# # print(categories)       ## list of web-elements     ## [wb1, wb2, wb3,..wb7]
#
# for ele in categories:
#     print(ele.text)

##############################################################################################

'''
3.  wap to print all the popular searches from https://www.myntra.com/
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# popular_searches = driver.find_elements('xpath', '//div[@class="desktop-pSearchlinks"]/a')
# # print(popular_searches)     ## list of web-elements     ## [wb1, wb2, wb3, wb4, wb5,...wb47]
#
# for ele in popular_searches:
#     print(ele.text)


##############################################################################################

'''
4.  wap to enter the data for all the textboxes present in demo.html
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\demo.html')
# time.sleep(2)
#
# all_textboxes = driver.find_elements('xpath', '//input[@name="fname"]')
# # print(all_textboxes)        ## list of web-elements     ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7, wb8, wb9]
#
# data_list = ['spiderman', 'alchemy of souls', 'Game of thrones', 'Power rangers', 'kartoon', 'labrea', 'ben10', 'avatar', 'tulsa king']
#
# i = 0       ## 2
# for textbox in all_textboxes:
#     textbox.send_keys(data_list[i])
#     i += 1

##############################################################################################

'''
5.    wap to click on the checkboxes present in demo.html
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A13-Dec26-2025\files\demo.html')
# time.sleep(2)
#
# all_checkboxes = driver.find_elements('xpath', '//input[@name="download"]')
# # print(all_checkboxes)       ## list of web-elements     ## [wb1, wb2, wb3, wb4, wb5, wb6]
#
# for checkbox in all_checkboxes:
#     checkbox.click()
#     time.sleep(0.5)

##############################################################################################

'''
1.  Go to https://www.myntra.com/, enter adidas in the search bar, select any auto-suggestion, 
    wap to print the name and price of all the shoes available (Shoename = Price)
2.  Go to https://www.myntra.com/, enter adidas in the search bar, select any auto-suggestion,
    wap to print all the colors
3.  Go to https://in.bookmyshow.com/, select the city. wap to print all the recommended movies
4.  Go to https://www.zomato.com/bangalore/restaurants, search for pizza, select pizza delivery, 
    choose any restaurant, wap to print the names of all the items present.
'''







































