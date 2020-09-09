import json
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import os
import datetime
import sys
import pytest
import requests
from bs4 import BeautifulSoup

import mysql.connector

from db import insert, read

url = "https://api.telegram.org/bot1114875381:AAEYISRMAfW1ywHdFK0SdqkWNp2j_zfV60c/"

chat = "389494971"

size = 4
base_url = ("https://www.global.jdsports.com/men/mens-footwear/brand/adidas-originals,puma,adidas,nike,under-armour,fred-perry,lacoste,new-balance,tommy-hilfiger,emporio-armani-ea7,champion,asics,adidas-skateboarding,vans/sale/?jd_sort_order=price-low-high&max=204&minprice-gbp=0&maxprice-gbp=50")
driver = webdriver.Chrome("chromedriver")

def quick_resp(responce):
    listMessage = responce['result']
    global size
    if len(listMessage) > size:
        for index in range(size,len(listMessage)):
            wellcomeSay(listMessage[index]['message']['text'])
            print( listMessage[index]['message']['text'])
        size = len(listMessage)



def wellcomeSay(userMsg):
    if userMsg == "hi":
        sendMsg("Hello my lord")
    elif userMsg == "hello":
        sendMsg("say me hello as my bro, bro :)")
    else:
        sendMsg("what are you want, bro>?")


def sendMsg(msg):
    params = {'chat_id': chat, 'text': msg}
    response = requests.post(url + 'sendMessage', data=params)
    return response.json()

def get_updates_json(url):
    response = requests.get(url + 'getUpdates')
    data = json.loads(response.text)
    quick_resp(data)

def parse_jd_sports():
    driver.get(base_url)
    driver.maximize_window()

    #driver.save_screenshot("landing_page.png")
    # driver.find_element_by_class_name("closeLightbox").click()

    elem = driver.find_elements_by_css_selector('.productListItem')
    links = []
    for i in elem:
        link = i.find_element_by_class_name("itemImage").get_attribute('href')
        links.append(link)
    # driver.quit()
    return links

def parse_footlocker():
    driver.get("https://www.jimmyjazz.com/collections/mens-clearance")
    driver.maximize_window()

    # driver.quit()
    elem = driver.find_elements_by_css_selector('.grid__item')
    links = []
    for i in elem:
        link = i.find_element_by_css_selector(".grid-product__link").get_attribute('href')
        links.append(link)
        print(link)

    return links

def send_mess( text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def checkLink (old_links, new_links):
    for i in new_links:
        isTrue = False
        for j in old_links:
            if i == j:
                isTrue = True
                break
        if isTrue == False:
            sendMsg(i)
            insert(i)
    print("заперсено :)")

# parse_footlocker()

while True:
    checkLink(read(),parse_jd_sports())
    time.sleep(random.randint(4,11))
    print("отоспано, идем парсить")


