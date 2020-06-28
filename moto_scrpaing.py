from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup as soup
import requests

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.leboncoin.fr/equipement_moto/1804370012.htm/")



driver.find_element_by_xpath('//*[@id="aside"]/div[1]/div/div/div[2]/div/div[3]').click()

