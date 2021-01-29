import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import shutil
import time
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2019, 1, 1)
end_date = date(2020, 1, 1)
    

def get_data_from_date_range(commodity_value, state_value, commodity_name, state_name, start_date, end_date, webdriver):
    for single_date in daterange(start_date, end_date):
        request_link = 'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity='+str(commodity_value)+'&Tx_State='+str(state_value)+'&Tx_District=0&Tx_Market=0&DateFrom='+start_date+'&DateTo='+end_date+'&Fr_Date='+start_date+'&To_Date='+end_date+'&Tx_Trend=2&Tx_CommodityHead=Onion&Tx_StateHead='+str(state_name)+'&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--'
        print(request_link)
        webdriver.get(request_link)
        excel_download = webdriver.find_element_by_xpath('//*[@id="cphBody_ButtonExcel"]').click()
        time.sleep(180)
    return

def rename_download(name):
    path = './downloads/'
    names = os.listdir('./downloads/')  
    os.rename(path + names[0], path + name)

def move_file(name):
    file_path = 'J:\\Crop-Price-Correlation-master\\'
    shutil.move(file_path + "downloads\\" + name, file_path + "commodity_data\\" + name)


def download_all_state(values, states, commodity_value, driver,start_date = '', end_date = ''):
    
    for val, st in zip(values, states):
        try:
            commodity_name = ''
            state_name = st.strip().replace(' ', '+')
            get_data_from_date_range(commodity_value, val, commodity_name, state_name, start_date, end_date, driver)
            name = st + '.xls'
            time.sleep(60)
            rename_download(name)
            move_file(name)
            time.sleep(10)
            print(st, ' has downloaded successfully')
        except:
            # print(st, ' is taking a lot of time extending the download time by 5 minutes')
            # time.sleep(300)
            # rename_download(name)
            # move_file(name)
            # time.sleep(10)
            # print(st, ' has downloaded successfully')
            print('state has not downloaded')
            continue
        break
        Generalised for complete year
