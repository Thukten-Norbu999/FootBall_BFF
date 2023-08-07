import os
from .main import app
from custom import Data

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
path = 'C:/driver/chromedriver.exe'


def run(path):
    driver = webdriver.Chrome(path)
    driver.get('https://www.facebook.com/BhutanFootballAcademy')

    posts = driver.find_elements(By.XPATH, )
