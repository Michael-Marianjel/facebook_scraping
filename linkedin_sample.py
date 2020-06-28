from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup as soup
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import requests
import time
import random
import csv 
import urllib.request
# import pymysql

last_name = input("Enter last_name : ")

# define csv file
# titles=['Name', 'Image_url']
# with open('linkedin_profile.csv', mode='a', encoding="utf8", newline='') as student_file:
#     student_writer = csv.writer(student_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     student_writer.writerow(titles)

#Connection to MYSQL DB
# conn=pymysql.connect(host="localhost",user="root",password="",db="linkedin")
# c=conn.cursor()

# run chrome driver 
driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.linkedin.com")

driver.delete_all_cookies()
time.sleep(3)
try:
  driver.find_element_by_xpath('/html/body/nav/a[3]').click()
except NoSuchElementException:
  pass

access_mail="darkbomb1234@outlook.com"
password="125kgs&&%JHJ"

time.sleep(2)
driver.find_element_by_xpath('//*[@id="username"]').send_keys(access_mail)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
time.sleep(random.randint(2,5))

driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="ember42"]/input').send_keys(last_name, Keys.ENTER)

driver.execute_script("window.scrollTo(0, 200);")
time.sleep(2)
driver.execute_script("window.scrollTo(200, 400);")
time.sleep(2)
driver.execute_script("window.scrollTo(400, 600);")
time.sleep(2)
driver.execute_script("window.scrollTo(600, 800);")
time.sleep(2)
driver.execute_script("window.scrollTo(800, 1000);")
time.sleep(2)
driver.execute_script("window.scrollTo(1000, 1200);")
time.sleep(5)
profile_content = soup(driver.page_source, 'html.parser')
profile_lists = profile_content.findAll('li', {'class':'search-result search-result__occluded-item ember-view'})

profile_info = ['','']
for profile_list in profile_lists:

  if (profile_list.find('div', {'class':'presence-entity presence-entity--size-4 ember-view'}) != None):
    profile_name = profile_list.find('span', {'class':'name actor-name'}).text
    last_name_len = len(last_name)
    if (profile_name[0:last_name_len] != last_name):
      profile_info[0]=profile_name
      profile_info[1] = profile_list.find('div', {'class':'presence-entity presence-entity--size-4 ember-view'}).img['src']
      urllib.request.urlretrieve(profile_info[1], "./profile_images/"+profile_info[0]+".jpg")

      # c.execute("""INSERT into profiles(name,image_url) VALUES (%s,%s)""",(profile_info[0],profile_info[1]))
      # conn.commit()
for x in range(100):
  if(x>1):
    driver.get("https://www.linkedin.com/search/results/all/?keywords="+last_name+"&origin=GLOBAL_SEARCH_HEADER&page="+str(x))
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 200);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(200, 400);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(400, 600);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(600, 800);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(800, 1000);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(1000, 1200);")
    time.sleep(5)
    profile_cont = soup(driver.page_source, 'html.parser')
    profile_li = profile_cont.findAll('li', {'class':'search-result search-result__occluded-item ember-view'})

    profile_infos = ['','']
    for profile in profile_li:

      if (profile.find('div', {'class':'presence-entity presence-entity--size-4 ember-view'}) != None):
        profile_name = profile.find('span', {'class':'name actor-name'}).text
        last_name_len = len(last_name)
        # if (profile_name[0:last_name_len] != last_name):
      

        #   c.execute("""INSERT into profiles(name,image_url) VALUES (%s,%s)""",(profile_infos[0],profile_infos[1]))
        #   conn.commit()
  # with open('linkedin_profile.csv', mode='a', encoding="utf8", newline='') as student_file:
  #   student_writer = csv.writer(student_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  #   student_writer.writerow(profile_info)