#!/usr/bin/env python
from selenium import webdriver
from random import randint
import time 
import os
import shutil
import string
import random
import asyncio
import subprocess
from webdriver_manager.chrome import ChromeDriverManager #to download chrome driver
from webdriver_manager.firefox import GeckoDriverManager #to download firefox driver
import undetected_chromedriver.v2 as uc #undetectable chrome driver (fuckin badass)

from proxybroker import Broker
from subprocess import Popen

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

createdUserNamePasswordFile = 'RedditAccounts.txt'
# Create Browser Profile 
if(not os.path.isdir('./ghostdriver')):
    os.mkdir('./ghostdriver')
def create_account(username, password, proxyType):
    #set up profile for proxy

    ChromOptions = uc.ChromeOptions()
    # Clearing profile 


    # setting profile
    ChromOptions.user_data_dir ='./ghostdriver'

    if(proxyType == 'T'):
        print('[+] restarting tor for a new ip address...')
        # Stop al ltor instances
        subprocess.call(['sh', './tor.sh'])
        # Restart tor
        # os.system('service tor restart')
        # os.system('torbrowser-launcher')

        
        ChromOptions.add_argument(f"--proxy-server=socks5://127.0.0.1:9150") # Tor
    elif(proxyType == 'P'):
        # Start proxybroker server
        print('[+] Starting ProxyServer for a new ip address...')
        subprocess.call(['sh', './proxy.sh'])
        ChromOptions.add_argument(f"--proxy-server=http://127.0.0.1:6662") # Proxy Server
        

    
    # just some options passing in to skip annoying popups
    ChromOptions.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    # browser = uc.Chrome(options=ChromOptions)
    browser = uc.Chrome(options=ChromOptions)
    # browser = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

    #get reddit account creation page
    browser.set_window_size(683, 744)
    browser.get('http://old.reddit.com/login')
    #insert username
    time.sleep(randint(1,4))
    browser.find_element_by_id('user_reg').click()
    browser.find_element_by_id('user_reg').send_keys(username)
    #insert password
    time.sleep(randint(1,5))
    browser.find_element_by_id('passwd_reg').click()
    browser.find_element_by_id('passwd_reg').send_keys(password)
    time.sleep(randint(1,5))
    browser.find_element_by_id('passwd2_reg').click()
    browser.find_element_by_id('passwd2_reg').send_keys(password)
    #pause to manually enter captcha
    readytomove = False
    while not readytomove:
        captchaResponse = input("[*] Solve captcha, create account, then press Y... enter 'N' as input if captcha doesn't appear to skip username" + '\n')

        if (captchaResponse == 'N'):
            # os.system('clear')
            browser.quit()
            return False
        elif (captchaResponse == "Y"):
            browser.quit()
            return True
            readytomove = True





def main():
    # os.system('clear')
    #run account generator for each user in list
    created = open(createdUserNamePasswordFile, 'a')
    accNo = int(input("No of Accounts: "))

    proxytypeComplete = False
    proxyType = 'N'
    while not proxytypeComplete:
        proxytypeResponse = input("[*]T for Tor\n[*]P for proxy\n[*]N for neither " + '\n')

        if(proxytypeResponse == 'T'):
            # Restart tor
            proxyType = 'T'
            proxytypeComplete = True
        elif(proxytypeResponse == 'P'):
            proxyType = 'P'
            proxytypeComplete = True 
        elif(proxytypeResponse == 'N'):
            proxyType = 'N'
            proxytypeComplete = True 
            



    i = 0
    while accNo > i:
        first_name = (random.choice(open("Fnames.txt").read().split()))
        last_name =  (random.choice(open("Lnames.txt").read().split()))
        full_name = (first_name + ' ' + last_name)
        username = (first_name + last_name + str(random.randint(1, 100)) + str(random.randint(1, 1000)))
        password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        cred = password
        print('[+] creating account for %s with password %s' % (username,password))
        account_created = create_account(username, password, proxyType)
        # os.system('service tor restart')
        if account_created:
            print('[+] writing name:password to created names...')
            created.write(username + ':' + password + '\n')
            i = i+1
        else:
            print('[-] name not recorded due to captcha issue')
        time.sleep(2)
    created.close()

    

  
main()

