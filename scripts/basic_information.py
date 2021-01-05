from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import Select

driver_path = './dependency/chromedriver.exe'
url = 'https://agmarknet.gov.in/'

driver = webdriver.Chrome(executable_path = driver_path)
driver.get(url)

# select_commodity = Select(driver.find_element_by_xpath('//*[@id="ddlCommodity"]'))

soup = BeautifulSoup(driver.page_source, 'html.parser')
select_commodity = soup.find_all('select', {'id':'ddlCommodity'})[0]
option_commodity = select_commodity.find_all('option')
commodity = dict()
commodity['value'] = []
commodity['name'] = []

for option in option_commodity:
    commodity['value'].append(option['value'])
    commodity['name'].append(option.text)

commodity = pd.DataFrame(commodity)
commodity.to_csv('./data/commodity.csv', index = False)

select_state = soup.find_all('select', {'id':'ddlState'})[0]
option_state = select_state.find_all('option')
state = dict()
state['value'] = []
state['state'] = []

for option in option_state:
    state['value'].append(option['value'])
    state['state'].append(option.text)

state = pd.DataFrame(state)
state.to_csv('./data/state.csv', index = False)

driver.close()