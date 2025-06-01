# sudo apt-get install firefox
# sudo apt-get install firefox-geckodriver
# pip install selenium
# pip install geckodriver


import time
import selenium.webdriver
import selenium.common

from selenium.webdriver import Firefox, DesiredCapabilities, FirefoxProfile
from selenium.webdriver.firefox.options import Options

profile = FirefoxProfile()
profile.set_preference("media.autoplay.default", 0)
cap = DesiredCapabilities.FIREFOX

options = selenium.webdriver.firefox.options.Options()
options.add_argument('--headless')

# options.headless = True

if 0:
    with selenium.webdriver.Firefox(firefox_profile=profile, capabilities=cap, options=options) as driver:
        driver.get('https://www.youtube-nocookie.com/embed/ve1RSR-x1BU?autoplay=1')
        time.sleep(2)
        driver.save_screenshot("viewport-1.png")


if 0:
    with selenium.webdriver.Firefox(firefox_profile=profile, capabilities=cap, options=options) as driver:
        driver.get('https://www.youtube-nocookie.com/embed/2vBSKsPhRb8?autoplay=1')
        time.sleep(2)
        driver.save_screenshot("viewport-2.png")


with selenium.webdriver.Firefox(firefox_profile=profile, capabilities=cap, options=options) as driver:
    driver.get('https://open.ivideon.com/embed/v2/?server=100-f23bb709a7cb48fd8a46879da0ec6c9f&camera=0&width=&height=&lang=ru&ap=&noibw=')
    time.sleep(4)
    driver.save_screenshot("viewport-3.png")


if 0:
    profile = FirefoxProfile()
    profile.set_preference("media.autoplay.default", 0)
    cap = DesiredCapabilities.FIREFOX

    options = selenium.webdriver.firefox.options.Options()
    options.add_argument('--headless')



    with selenium.webdriver.Firefox(firefox_profile=profile, capabilities=cap, options=options) as driver:
        driver.get('https://live.katun24.ru:8082/port_ptz/embed.html')
        time.sleep(2)
        driver.save_screenshot("viewport-4.png")


