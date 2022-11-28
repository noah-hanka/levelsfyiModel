import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

entryOffset = 0
url = f'https://www.levels.fyi/companies/google/salaries/software-engineer?limit=50&offset={entryOffset}'
serv = Service('/home/noah/dev/school/stat4185/levelsfyiModel/chromedriver')
driver = webdriver.Chrome(service=serv)

# driver.get(url)
# time.sleep(5)
# html = driver.page_source
# soup = bs(html, 'html.parser')