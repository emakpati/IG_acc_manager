# BOT INFORMATION #

import pandas as pd
import xlrd
import numpy as np

all_data = pd.read_excel("/Users/Ekene/Desktop/DataScience/data_sets/ig_bot_names.xlsx")
# Excel spreadsheet with pre-made NAME, USERNAME, EMAIL, PASSWORD columns.

usernames = all_data.USERNAME
key = all_data.PASSWORD[0]