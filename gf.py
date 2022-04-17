# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 00:40:58 2021

@author: Huang
"""

# from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

import time

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://gfb.gameflier.com/Billing/ONLINE_SERVICES/W2/index.aspx?redct=G4")

#序號
cardInfo = [
	"W3EOD01000058236", 	"yqgMhQBc5fcjqQXS", 
	"W3EOD01000000293", 	"fsaY9raNU73netpd", 
	"W3EOD01000064784", 	"fXUCe3a8fv4Rb6mh", 
];

##切換到iframe
"""
https://stackoverflow.com/questions/44834358/switch-to-an-iframe-through-selenium-and-python?rq=1
"""


#%%

iframe = browser.find_element_by_xpath("//*[@id='actfm']")
browser.switch_to.frame(iframe)

#%%
#選擇遊戲帳號
Game_ID = Select(browser.find_element_by_xpath('//*[@id="Game_ID"]'))
Game_ID.select_by_index(3)

#選擇伺服器
Game_Svr = Select(browser.find_element_by_xpath('//*[@id="Game_Svr"]'))
Game_Svr.select_by_index(1)

#選擇角色名稱
Game_Role = Select(browser.find_element_by_xpath('//*[@id="Game_Role"]'))
Game_Role.select_by_index(2)

#%%儲值序號/儲值密碼輸入
length = len(cardInfo)

for i in range(0,int(length),2):
    print(i)

    Card_ID = browser.find_element_by_name("Card_ID")
    Card_ID.clear()
    Card_ID.send_keys(cardInfo[i])
    time.sleep(0.8)
    
    Card_PW = browser.find_element_by_name("Card_PW")
    Card_PW.clear()
    Card_PW.send_keys(cardInfo[i+1])
    time.sleep(0.8)
    
    commit = browser.find_element_by_xpath('//*[@id="ButtonOK"]')
    commit.click()
    time.sleep(3)
