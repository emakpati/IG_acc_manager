# LOGIN TO IG #

# Imports #
from selenium import webdriver
import pandas as pd
import user_info as usr

# Setup Driver #
# https://sites.google.com/a/chromium.org/chromedriver/downloads
driver = webdriver.Chrome(executable_path="/chromedriver")

# Login #
login_url = "https://www.instagram.com/accounts/login/"
driver.get(login_url)

i = 0  # To go through usernames series in excel sheet.
user = usr.usernames[i]

# Form Inputs Func #
# https://www.w3schools.com/xml/xpath_syntax.asp

def get_user_and_login():

    input_user = driver.find_element_by_xpath('//*[@name="username"]')
    input_user.send_keys(user)

    input_psswd = driver.find_element_by_xpath('//*[@name="password"]')
    input_psswd.send_keys(usr.key)

    input_psswd.submit()
    input_user.submit()

# Login Call #
get_user_and_login()

