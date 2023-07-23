import os
from selenium import webdriver
import time
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import glob
import re
import os
import chromedriver_autoinstaller as AutoChrome
import shutil
import pandas as pd
from multiprocessing import Process
from multiprocessing import Manager
# from pathos.multiprocessing import ProcessingPool as Pool
import numpy as np
import os
from selenium import webdriver
import time
from datetime import datetime, timedelta
import re
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import multiprocessing as mp
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
from urllib.parse import parse_qs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import pyperclip
from selenium.webdriver.common.keys import Keys
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from lxml import html
from lxml import etree
def dict_append_as_list(dict1, dict2):  # key별로 list가 할당되어 있고 이걸 기준으로 dataframe만드는데 연결을 위함.
    for key, value in dict2.items():
        if key in dict1:
            dict1[key].extend(value)
        else:
            dict1[key] = value
    return dict1

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

def ad_info_getter(platform_identifier, ad_filter_option):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # i_th = 0# for test
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get('https://pagestage.kakao.com/fantasy')
    driver.set_window_position(-7, 0)
    driver.set_window_size(1650, 1047)


if __name__ == '__main__':
    view_date = datetime.now()  # .strftime('%Y-%m-%d')  # %H-%M-%S')
    # view_date = datetime(2023,3,21,14,21,35)# for test
    start_time = time.time()  # 시작 시간 저장
    platform_identifier = 'GDN'
    createFolder('./' + platform_identifier)
    createFolder("./" + platform_identifier + "/change_log/")
    ad_filter_option = {}
    ad_info_getter(platform_identifier, ad_filter_option)
