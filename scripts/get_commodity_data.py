import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import shutil
import time


def get_data_from_date_range(commodity_value, state_value, start_date, end_date, webdriver):
    request_link = 'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity='+str(commodity_value)+'&Tx_State='+str(state_value)+'&Tx_District=0&Tx_Market=0&DateFrom=04-Jan-2020&DateTo=04-Jan-2021&Fr_Date=04-Jan-2020&To_Date=04-Jan-2021&Tx_Trend=0&Tx_CommodityHead=Onion&Tx_StateHead=Gujarat&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--'
    webdriver.get(request_link)
    excel_download = webdriver.find_element_by_xpath('//*[@id="cphBody_ButtonExcel"]').click()
    return

def rename_download(name):
    path = './downloads/'
    names = os.listdir('./downloads/')  
    os.rename(path + names[0], path + name)

def move_file(name):
    file_path = 'C:\\Users\\ravir\\Desktop\\Crop-Price-Correlation\\'
    shutil.move(file_path + "downloads\\" + name, file_path + "commodity_data\\" + name)


def download_all_state(values, states, commodity_value, driver,start_date = '', end_date = ''):
    
    for val, st in zip(values, states):
        try:
            get_data_from_date_range(commodity_value, val, start_date, end_date, driver)
            name = st + '.xls'
            time.sleep(60)
            rename_download(name)
            move_file(name)
            time.sleep(10)
            print(st, ' has downloaded successfully')
        except:
            print(st, ' is taking a lot of time extending the download time by 5 minutes')
            time.sleep(300)
            rename_download(name)
            move_file(name)
            time.sleep(10)
            print(st, ' has downloaded successfully')
            continue
        