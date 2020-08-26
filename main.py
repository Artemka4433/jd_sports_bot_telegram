import json

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

url = "https://api.telegram.org/bot1114875381:AAEYISRMAfW1ywHdFK0SdqkWNp2j_zfV60c/"

chat = "389494971"

size = 4
base_url = ("https://www.global.jdsports.com/men/mens-footwear/sale/?max=204&jd_sort_order=price-low-high")
driver = webdriver.Chrome("chromedriver")

def quick_resp(responce):
    listMessage = responce['result']
    global size
    if len(listMessage) > size:
        for index in range(size,len(listMessage)):
            wellcomeSay(listMessage[index]['message']['text'])
            print( listMessage[index]['message']['text'])
        size = len(listMessage)

    # userMsg = responce['result']['message']['text']
    # if userMsg == "hello":
    #     sendMsg(1231,"boy boy, hay bro")

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

    driver.save_screenshot("landing_page.png")
    driver.find_element_by_class_name("closeLightbox").click()

    elem = driver.find_element_by_css_selector('#productListMain')
    list = elem.get_attribute('innerHTML')
    name = elem.find_element_by_class_name("itemTitle").find_element_by_tag_name("a").get_attribute('innerHTML')

    # oldprice =
    # price =
    # link =
    sendMsg(name)
    # sendMsg(link)

    driver.quit()



def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

parse_jd_sports()


