from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import Select
from get_commodity_data import download_all_state
import os
print(os.path.abspath('./')) 
driver_path = './dependency/chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'C:\\Users\\ravir\\Desktop\\Crop-Price-Correlation\\downloads\\'}
chrome_options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = driver_path)
print('download path added successfully')
state = pd.read_csv('./data/state.csv')

download_all_state(state['value'].values, state['state'].values, 23, driver,start_date = '', end_date = '')

driver.close()