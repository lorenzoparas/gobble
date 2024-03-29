from abc import abstractmethod
import json
import requests
from bs4 import BeautifulSoup
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Scraper:

    def __init__(self):
        self.driver = self.__setupDriver()

    @abstractmethod
    def run(self):
        pass

    def getSoup(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    def getPerformanceLog(self):
        return self.driver.get_log('performance')

    def getPerformanceLogEvents(self):
        performanceLog = self.getPerformanceLog()
        performanceLogEvents = [
            self.__processBrowserPerformanceLogEntry(performanceLogEntry) for performanceLogEntry in performanceLog
        ]
        return performanceLogEvents

    def resetDriver(self):
        if not self.driver: return NameError('driver is not defined')
        self.__stopDriver()
        sleep(2)
        self.driver = self.__setupDriver()

    def gotoPrevPage(self):
        self.driver.back()

    def __processBrowserPerformanceLogEntry(self, entry):
        response = json.loads(entry['message'])['message']
        return response

    def __stopDriver(self):
        self.driver.close()
        self.driver.quit()

    def __setupDriver(self):

        # add ChromeDriver for selenium usage
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        # chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--disable-dev-shm-usage')
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument("start-maximized")
        chromeOptions.add_argument("disable-infobars")
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--disable-application-cache')
        chromeOptions.add_argument('--disable-gpu')
        chromeOptions.add_argument("--disable-dev-shm-usage")
        chromeOptions.add_argument('--disable-blink-features=AutomationControlled')

        driver = webdriver.Chrome(
            options=chromeOptions,
            service=Service()
        )

        return driver
    