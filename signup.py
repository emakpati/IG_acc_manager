# SIGNUP FOR IG #

# Imports #
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # For sending keyboard keys
import user_info as usr

driver = webdriver.Chrome(executable_path="/chromedriver")

# Signup #
signup_url = "https://www.instagram.com/"
driver.get(signup_url)

i = 0
user = usr.all_data.USERNAME[i]

def create_user():
    # Locate elements
    enter_email = driver.find_element_by_name("emailOrPhone")
    enter_name = driver.find_element_by_name("fullName")

    enter_username = driver.find_element_by_name("username")
    enter_psswd = driver.find_element_by_name("password")

    # Send keys
    enter_email.send_keys(usr.all_data.EMAIL[2])
    enter_name.send_keys(usr.all_data.NAME[2])

    enter_username.send_keys(usr.all_data.USERNAME[2])
    enter_psswd.send_keys(usr.key)
    enter_psswd.send_keys(Keys.RETURN)
