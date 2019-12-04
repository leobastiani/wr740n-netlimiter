#!python3
#encoding=utf-8

"""Usage:
  netlimiter (start|stop) [options]

Options:
  -h --help   Show this screen.
  -d --debug  Show version.
"""
from __future__ import print_function, division, absolute_import
from docopt import docopt
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

arguments = docopt(__doc__)
DEBUG = arguments['--debug'] or sys.flags.debug
def debug(*args):
    if DEBUG:
        print(*args)

options = Options()
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
if not DEBUG:
    options.add_argument("--headless")

driver = None
try:
    debug("arguments:", arguments)
    driver = webdriver.Chrome(options=options)
    driver.get("http://admin:admin@192.168.0.1")

    driver.switch_to.frame('bottomLeftFrame')
    driver.find_elements_by_css_selector('#a36')[0].click()
    driver.switch_to.default_content()

    driver.switch_to.frame('mainFrame')
    time.sleep(1)
    checkbox = driver.find_elements_by_css_selector('input[name=QoSCtrl]')[0]
    if arguments['start'] != checkbox.is_selected():
        checkbox.click()
        driver.find_elements_by_css_selector('input[type=submit]')[0].click()
        time.sleep(3)
    driver.switch_to.default_content()
finally:
    driver.quit()
