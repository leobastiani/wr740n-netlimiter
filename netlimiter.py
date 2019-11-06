#!python3
#encoding=utf-8
from __future__ import print_function, division, absolute_import

import argparse
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

parser = argparse.ArgumentParser(description='Enable Bandwith Control on WR740N')
parser.add_argument('--yes', '-y', action='store_true', help='Enable Bandwith Control')
parser.add_argument('--debug', '-d', action='store_true', help='Debug mode')
args = parser.parse_args()

DEBUG = args.debug

def debug(*args):
    if not DEBUG:
        return ;
    print(*args)

options = Options()
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
if not DEBUG:
    options.add_argument("--headless")

driver = None
try:
    driver = webdriver.Chrome(options=options)
    driver.get("http://admin:admin@192.168.0.1")

    driver.switch_to.frame('bottomLeftFrame')
    driver.find_elements_by_css_selector('#a36')[0].click()
    driver.switch_to.default_content()

    driver.switch_to.frame('mainFrame')
    time.sleep(1)
    checkbox = driver.find_elements_by_css_selector('input[name=QoSCtrl]')[0]
    if args.yes != checkbox.is_selected():
        checkbox.click()
        driver.find_elements_by_css_selector('input[type=submit]')[0].click()
        time.sleep(3)
        driver.switch_to.default_content()
finally:
    driver.quit()
