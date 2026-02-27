'''
xpath   :   It is a locator to locate any element on the application uniquely.
            Using xpath, we can locate the web elements using attributes, using text, can do indexing, can locate
            dynamically changing elements.
            We can locate any element on the application using xpath

            There are 2 types of xpath
            *   Absolute xpath  :   Starts from the root of html
                                    We use / to write the absolute xpath
                                    / represents immediate child

                                    DRAWBACKS
                                    *   Depends on the full path from the root
                                    *   Difficult to maintain
                                    *   Not reusable
                                    *   Not readable
                                    *   Very lengthy and time consuming

            *   relative xpath  :   Doesnot start from the root of html
                                    We use // to write the relative xpath
                                    // represents any child

'''
import time

# ## EG1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\css_selector.html')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/table[2]/tbody/tr[1]/td/input').send_keys('Mathew')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/table[2]/tbody/tr[2]/td/input').send_keys('mathew@12345')

#######################################################################################################

# ## EG2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/input').click()

#######################################################################################################

'''
        Attribute name and attribute value
        SYNTAX  :   //tagname[@attr_name="attr_value"]
'''

# ## EG1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="login-button"]').click()
# time.sleep(3)
# driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@id="logout_sidebar_link"]').click()
#

#######################################################################################################

## EG2

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.activision.com/')
# time.sleep(3)
#
# driver.find_element('xpath', '//a[@aria-label="Log into your account"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@name="emailOrPhone"]').send_keys('sumeet@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="password"]').send_keys('sumeet@12345')
# time.sleep(1)
# driver.find_element('xpath', '//button[@aria-label="Sign In"]').click()

####################################################################################################

# ## EG3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/accounts/emailsignup/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="emailOrPhone"]').send_keys('9874562310')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="password"]').send_keys('shaheed@12345')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="fullName"]').send_keys('shaheed')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="username"]').send_keys('shaheed_123')

####################################################################################################

## EG4

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.amazon.in/')
# time.sleep(2)
# driver.find_element('xpath', '//input[@name="field-keywords"]').send_keys('Perfume')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="nav-search-submit-button"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[@class="a-truncate-cut"]').click()

####################################################################################################

## EG5

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[@data-group="men"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@data-group="kids"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@data-group="beauty"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@data-group="genz"]').click()

####################################################################################################

## EG6

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.jiomart.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[@id="btn_location_close_icon"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="rel_pincode"]').send_keys('560003')
# time.sleep(2)
# driver.find_element('xpath', '//button[@id="btn_pincode_submit"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@type="search"]').send_keys('Phone')
# time.sleep(1)
# driver.find_element('xpath', '//span[@class="line-clamp"]').click()

####################################################################################################
#
# ## EG7
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://chat.qspiders.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="username"]').send_keys('chaithra@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="password"]').send_keys('chaitra@1234')
# time.sleep(1)
# driver.find_element('xpath', '//button[@type="submit"]').click()


####################################################################################################

'''
text    :   //tagname[text()="text"]
'''

# ## EG1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.flipkart.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Home & Kitchen"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Become a Seller"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//button[text()="Start Selling"]').click()

#############################################################################################

# ## EG2
#
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
# driver.find_element('xpath', '//a[text()="Men"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Women"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Kids"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Home"]').click()


#############################################################################################
#
# ## EG3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.amazon.in/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Sell"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Bestsellers"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Amazon Launchpad"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Collections"]').click()

#############################################################################################

## EG4

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="ADD TO CART"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@class="cart-icon"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//button[text()="PROCEED TO CHECKOUT"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@class="promoCode"]').send_keys('CAP1234')
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Apply"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//button[text()="Place Order"]').click()

#############################################################################################

## EG5

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://x.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Create account"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//button[@aria-label="Close"]').click()
# time.sleep(3)
# driver.find_element('xpath', '//span[text()="Sign up with Google"]').click()

#############################################################################################

'''
group indexing  :   (any_xpath)[index_num]
'''

# ## EG1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
# driver.find_element('xpath', '(//input[@type="text"])[1]').send_keys('Shravya')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[2]').send_keys('Shetty')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[5]').send_keys('shravya@gmail.com')

#############################################################################################

# ## EG2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\css_selector.html')
# time.sleep(2)
#
# driver.find_element('xpath', '(//input[@name="fname"])[1]').send_keys('chandrashekar')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@name="fname"])[2]').send_keys('Mathew')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@name="fname"])[3]').send_keys('Shaheed')

#############################################################################################

# ## EG3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[1]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[3]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[4]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[5]').click()

###############################################################################################

'''
contains    :   //tagname[contains(text(), "partial_text")]
'''

# ## EG1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://selectorshub.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[contains(text(), "Products")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "Courses")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "Practice Page")]').click()

#############################################################################################

# ## EG2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.giva.co/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[contains(text(), "New Launch")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "Gold with Lab Diamonds")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "GIVA Gift Card")]').click()

#############################################################################################

# ## EG3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.kushals.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[contains(text(), "Bangles")])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "92.5 Silver")])[5]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Happy Customers")])[2]').click()

#############################################################################################

## EG4

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.purplle.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[contains(text(), "BRANDS")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[contains(text(), "OFFERS")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[contains(text(), "MAGAZINE")]').click()
#
#############################################################################################

## EG5

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
# driver.find_element('xpath', '(//a[contains(text(), "Books")])[3]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Computers")])[3]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Electronics")])[3]').click()


#############################################################################################

'''
Dependent-independent xpath
    *   Identify the dependent and independent element
    *   Write the xpath of the independent element  
    *   Traverse back until we get the common match for dependent independent element
    *   Continue writing the xpath for the dependent element 
    
'''

'''
1.  wap to click on the checkbox of Ruby in demo.html
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
# driver.find_element('xpath', '//td[text()="Ruby"]/..//input[@name="download"]').click()

##########################################################################################

'''
2.  wap to click on the download link of windows demo.html
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
# driver.find_element('xpath', '//td[text()="Windows"]/..//a[text()="Download"]').click()

##########################################################################################

'''
3.  wap to click on the release notes of python 3.13.8 
'''

# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www.python.org/')
# time.sleep(2)
# driver.find_element('xpath', '(//a[text()="Downloads"])[1]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Python 3.13.8"]/../..//a[text()="Release notes"]').click()

##########################################################################################

'''
4.  wap to print the price of mrf in https://in.tradingview.com/
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://in.tradingview.com/')
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Search"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@name="query"]').send_keys('MRF')
# time.sleep(1)
# driver.find_element('xpath', '(//button[@aria-label="Search"])[3]').click()
# time.sleep(2)
# mrf = driver.find_element('xpath', '(//span[text()="MRF"])[4]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
# print(mrf.text)

##########################################################################################

'''
5.  wap to print the sellprice and buyprice of gold in https://www.iforex.in/tools/live-rates
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.iforex.in/tools/live-rates")
# time.sleep(2)
# driver.find_element('xpath', '//div[@id="ai-chat-close"]').click()
# time.sleep(4)
#
# sellprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[2]')
# print(sellprice.text)
#
# buyprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[3]')
# print(buyprice.text)


##########################################################################################

'''
Parent - child
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
# driver.find_element('xpath', '//div[@class="block block-category-navigation"]//a[contains(text(), "Books")]').click()

##########################################################################################

'''
Child - Parent
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
# driver.find_element('xpath', '(//a[contains(text(), "Books")])[3]/..')      ## Go to the immediate parent
#
# ##
# driver.find_element('xpath', '(//a[contains(text(), "Books")])[3]/parent::li')  ##

##########################################################################################

'''
ancestor
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/")
#
# driver.find_element('xpath', '(//a[contains(text(), "Books")])[3]/ancestor::div')
#
# ## Incase of multiple occurances, we can do indexing
# driver.find_element('xpath', '(//a[contains(text(), "Books")])[3]/ancestor::div[2]')

##########################################################################################

'''
descendant
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/")
#
# driver.find_element('xpath', '//div[@class="block block-category-navigation"]/descendant::a')
#
# ## Incase of multiple occurances, we can do indexing
# driver.find_element('xpath', '//div[@class="block block-category-navigation"]/descendant::a[3]')

##########################################################################################

'''
siblings
'''

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.python.org/downloads/")
time.sleep(2)

## preceding-sibling
driver.find_element('xpath', '(//span[text()="Dec. 5, 2025"])[1]/preceding-sibling::span')

## Incase of multiple occurances we can do indexing
driver.find_element('xpath', '(//span[text()="Dec. 5, 2025"])[1]/preceding-sibling::span[2]')

## following-sibling
driver.find_element('xpath', '(//span[text()="Dec. 5, 2025"])[1]/following-sibling::span')

## Incase of multiple occurances we can do indexing
driver.find_element('xpath', '(//span[text()="Dec. 5, 2025"])[1]/following-sibling::span[2]')


































