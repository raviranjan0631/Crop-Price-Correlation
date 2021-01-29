from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import Select
from get_commodity_data import download_all_state, get_data_from_date_range
import os
print(os.path.abspath('./')) 
driver_path = './dependency/chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'J:\\Crop-Price-Correlation-master\\Crop-Price-Correlation-master\\dummy_data'}
chrome_options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = driver_path)
print('download path added successfully')
state = pd.read_csv('./data/state.csv')

get_data_from_date_range(23, 'UP', '', 'Uttar+Pradesh', '27-Jan-2017', '27-Jan-2018', driver)

driver.close()