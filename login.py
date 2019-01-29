# LOGIN TO IG #

# Imports #
from selenium import webdriver
import pandas as pd
import user_info as usr

# Setup Driver #
# https://sites.google.com/a/chromium.org/chromedriver/downloads
driver = webdriver.Chrome(executable_path="/Users/Ekene/Downloads/chromedriver")

# Login #
login_url = "https://www.instagram.com/accounts/login/"
driver.get(login_url)

i = 0  # To go through usernames series.
user = usr.usernames[i]


