import logging
import string
import io
import random
import urllib.request

import time
import selenium.webdriver
import selenium.common
from selenium.webdriver import Firefox, FirefoxProfile
from selenium.webdriver.firefox.options import Options

from PIL import Image
from proto_downloader import *

class instance(proto_downloader):
    def get(self, source, parameters=None):
        """
        run a headless firefox, wait for X seconds, take a screenshot and convert it to the PIL Image
        """
        logging.debug('Module "%s" activated.', __name__)

        try:
            profile = FirefoxProfile()
            profile.set_preference("media.autoplay.default", 0)
            profile.set_preference("dom.webnotifications.enabled", False)
            profile.set_preference("media.volume_scale", "0.0")

            options = selenium.webdriver.firefox.options.Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
            options.profile = profile
        except:
            logging.warning('Module "%s": error during FF init', __name__)
            return None

        random_len = source.get('random_len',13)
        random_part = ''.join(random.choice(string.digits) for _ in range(random_len))
        url = source['url'].replace('#random#',random_part)

        waiting_time = source.get('waiting_time',7)

        try:
            with selenium.webdriver.Firefox(options=options) as driver:
                driver.get(url)
                time.sleep(waiting_time)

                data = driver.get_screenshot_as_png()
                # TBD: here it's possible to analyze the screen and decide if we want to sleep some more time. But... who cares
                image = Image.open(io.BytesIO(data))

                rgb_image = Image.new("RGB", image.size, (255, 255, 255))
                rgb_image.paste(image, mask=image.split()[3]) # 3 is the alpha channel
                image = rgb_image
                driver.quit()

                return image
        except Exception as e:
            logging.warning('Module "%s": error while taking screenshot from url %s. Message: %s', __name__,url, str(e))
            return None
