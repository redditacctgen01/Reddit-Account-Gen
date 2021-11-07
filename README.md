

<!-- If you get an error about chrome -->
# install manually all the missing libraries
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

# install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

<!-- curl -sSf "http://pubproxy.com/api/proxy?limit=50&format=txt&type=socks5" > proxy-list.txt -->

Undetectable Chrome Driver
    https://github.com/ultrafunkamsterdam/undetected-chromedriver
        - python3 -m pip install undetected-chromedriver


For Proxy generation 
    https://github.com/constverum/ProxyBroker


proxybroker grab -c US -l 100 -o ./proxy-list.txt 

<!-- Run a proxy server that automatically changes proxy per request -->
proxybroker serve --host 127.0.0.1 --port 6662 --types HTTP HTTPS --lvl High

<!-- How to edit tor to supply a control port -->
sudo nano /etc/tor/torrc

<!-- Adding and saving cookies -->

You can save the current cookies as a Python object using pickle. For example:

import pickle
import selenium.webdriver

driver = selenium.webdriver.Firefox()
driver.get("http://www.google.com")
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

And later to add them back:

import pickle
import selenium.webdriver

driver = selenium.webdriver.Firefox()
driver.get("http://www.google.com")
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
