import time
from bs4 import BeautifulSoup
import selenium
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re

# --------------------------------
# Step0: Initial Webdriver Chrome (keep browser opening after code running completely)
ser = Service(r"C:\Users\Ba Truong Huu\Downloads\Compressed\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser,options=chrome_option)

# --------------------------------
# Load HTML selenium, write HTML to file
page = 'https://snnptnt.thuathienhue.gov.vn/?gd=1&cn=129&tc=22380'
driver.get(page)
html = driver.page_source
with open('html.txt', 'w', encoding='utf-8') as file:
    file.write(html)

# --------------------------------
time.sleep(20)
# soup = BeautifulSoup(html,'html.parser')
soup = BeautifulSoup(html,'lxml')
soup_text = soup.text
with open('html1.txt', 'w', encoding='utf-8') as f:
    f.write(soup_text)

# --------------------------------
# define function to remove empty line
def cleanline(lines):
    group = [line for line in lines.split('\n') if line.strip()]
    return '\n'.join(group)

# --------------------------------
# filter tables
list_df = []
for x,table in enumerate(soup.find_all('table',{'border':'1'}),0):
    # iterate all tables include border
    for y,row in enumerate(table.find_all('tr'),0):
        # iterate all rows
        for z,td in enumerate(row.find_all('td'),0):
            # iterate all columns
            print(x,y,z,cleanline(td.text))
            list_df[x] = pd.DataFrame()


driver.quit()