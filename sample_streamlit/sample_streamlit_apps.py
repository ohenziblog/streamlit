import streamlit as st
import os, sys

@st.experimental_singleton
def installff():
  os.system('sbase install geckodriver')
  os.system('ln -s /home/appuser/venv/lib/python3.9/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')
  # os.system('ln -s /home/appuser/venv/lib/python3.9/site-packages/seleniumbase/drivers/geckodriver')
  sys.path.append('/home/appuser/venv/lib/python3.9/site-packages/selenium/webdriver/firefox.exe')
  sys.path.append('/home/appuser/venv/lib/python3.9/site-packages/seleniumbase/drivers/geckodriver')
  sys.path.append('/home/appuser/venv/bin/geckodriver')

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'/home/appuser/venv/lib/python3.9/site-packages/selenium/webdriver/firefox.exe'
driver = webdriver.Firefox(executable_path=r'/home/appuser/venv/bin/geckodriver', options=options)
driver.get('http://google.com/')

# memo----------------------------------------------
# from selenium import webdriver
# from selenium.webdriver import FirefoxOptions
# _ = installff()
# opts = FirefoxOptions()
# opts.add_argument("--headless")
# browser = webdriver.Firefox(options=opts)
#
# browser.get('http://example.com')
# st.write(browser.page_source)
# memo----------------------------------------------