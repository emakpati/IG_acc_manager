# SIGNUP FOR IG #

# Imports #
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # For sending keyboard keys
import user_info as usr

driver = webdriver.Chrome(executable_path="/Users/Ekene/Downloads/chromedriver")

# Signup #
signup_url = "https://www.instagram.com/"
driver.get(signup_url)

i = 0
user = usr.all_data.USERNAME[i]

