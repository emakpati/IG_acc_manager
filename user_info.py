# BOT INFORMATION #

import pandas as pd
import xlrd
import numpy as np

all_data = pd.read_excel("/Users/Ekene/Desktop/DataScience/data_sets/ig_bot_names.xlsx")

usernames = all_data.USERNAME
key = all_data.PASSWORD[0]