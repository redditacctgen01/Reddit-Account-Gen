#!/usr/bin/env python
from selenium import webdriver
import time 
import os
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import undetected_chromedriver.v2 as uc
from random import randint
import string
import random
# 
# driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

loginFile = 'createdNames.txt'

#update with comment link or post link to upvote
postLink = 'https://old.reddit.com/r/loopringorg/comments/qo4lde/lrc_loopring_top_3_coin_on_reddit_this_is_awesome'
commentPermaLink = ''

def upvote_post(browser,username, password, postLink, proxyType='N'):
    #get reddit account creation page
    browser.set_window_size(900, 1150)
    browser.get('http://old.reddit.com/login')
    #insert username
    time.sleep(randint(1,4))
    browser.find_element_by_id('user_login').click()
    browser.find_element_by_id('user_login').send_keys(username)
    #insert password
    time.sleep(randint(1,5))
    browser.find_element_by_id('passwd_login').click()
    browser.find_element_by_id('passwd_login').send_keys(password)
    #login
    time.sleep(randint(1,5))
    # readytomove = False
    # while not readytomove:
    #     captchaResponse = input("[*] Login then press Y... enter 'N' as input if captcha doesn't appear to skip username" + '\n')

    #     if (captchaResponse == 'N'):
    #         # os.system('clear')
    #         browser.quit()
    #         return False
    #     elif (captchaResponse == "Y"):
    #         browser.quit()
    #         return True
    #         readytomove = True

    browser.find_element_by_css_selector('#login-form > div.c-clearfix.c-submit-group > button').click()
    time.sleep(randint(2,5))
    #get link page
    browser.get(postLink)
    time.sleep(randint(2,5))

    browser.find_element_by_css_selector('div.arrow:nth-child(1)').click()
    #header-bottom-right > form > a
    browser.find_element_by_css_selector('#header-bottom-right > form > a').click()
    # readytomove = False
    # while not readytomove:
    #     captchaResponse = input("[*] Logout then press Y... enter 'N' as input if captcha doesn't appear to skip username" + '\n')
    #     if (captchaResponse == 'N'):
    #         return False
    #     elif (captchaResponse == "Y"):
    #         readytomove = True
    # time.sleep(2)
    # browser.get('http://www.old.reddit.com/login')
    

def upvote_comment(browser, username, password, commentLink):
    ChromOptions = uc.ChromeOptions()
    # setting profile
    # ChromOptions.user_data_dir ='./ghostdriver'

    # ChromOptions.add_argument(f"--proxy-server=http://127.0.0.1:6662") # Proxy Server
    ChromOptions.add_argument(f"--proxy-server=socks5://127.0.0.1:9052") # Tor

    
    # just some options passing in to skip annoying popups
    ChromOptions.add_argument('--no-first-run --no-service-autorun ')
    browser = uc.Chrome(options=ChromOptions)
    # browser = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    browser.get('http://old.reddit.com/login')
    time.sleep(randint(1,4))

    #insert username
    browser.find_element_by_id('user_login').click()
    browser.find_element_by_id('user_login').send_keys(username)
    #insert password
    browser.find_element_by_id('passwd_login').click()
    browser.find_element_by_id('passwd_login').send_keys(password)
    #login
    browser.find_element_by_css_selector('.btn').click()
    time.sleep(2)
    #get link page
    browser.get(commentLink)
    browser.find_element_by_css_selector('div.midcol:nth-child(2) > div:nth-child(1)').click()
    #logout
    browser.find_element_by_css_selector('.logout > a:nth-child(4)').click()
    time.sleep(2)
    browser.get('http://old.reddit.com/login')

def main():
    ChromOptions = uc.ChromeOptions()
    # setting profile
    ChromOptions.user_data_dir ='./ghostdriver'

    proxyType = 'N'
    if(proxyType == 'T'):
        ChromOptions.add_argument(f"--proxy-server=socks5://127.0.0.1:9050") # Tor
    elif(proxyType == 'P'):
        ChromOptions.add_argument(f"--proxy-server=http://127.0.0.1:6662") # Proxy Server
        
    
    # just some options passing in to skip annoying popups
    ChromOptions.add_argument('--no-first-run --no-service-autorun ')
    browser = uc.Chrome(options=ChromOptions)
    # browser = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

    #comment out post or comment depending on what you'd like to upvote
    creds = [cred.strip() for cred in open(loginFile).readlines()]
    for cred in creds:
        username, password = cred.split(':')
        # upvote_comment(browser, username,password,commentPermaLink)
        upvote_post( browser, username, password, postLink)

main()
