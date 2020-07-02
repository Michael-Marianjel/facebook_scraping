from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import os
import re
import csv 

import xlsxwriter

login_mail = input("Please input your facebook email: ")
login_pass = input("Please input your facebook password: ")
limitation = input("Please input limitation for scraping: ")
output_filename = input("Please input the name of output file: ")

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(output_filename +'.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

titles=['Profile Link', "Group Name", 'Profile Name', 'Address', 'State', "Zip Code", "E-mail Address", 'Phone']

# Start from the first cell below the headers.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for title in titles:
  worksheet.write(row, col, title, bold)
  col += 1

lk = os.path.join(os.getcwd(), "chromedriver",)
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(lk, options=chrome_options)

def hasNumbers(inputString):
  return bool(re.search(r'\d', inputString))
def get_member(link, group_name):
  global row
  col = 0
  row += 1
  contact_detail = ['','','','','','','','']
  contact_detail[0] = link
  contact_detail[1] = group_name
  driver.get(link)
  time.sleep(3)
  member_content = soup(driver.page_source, 'html.parser')
  if(member_content.find(id = "fb-timeline-cover-name") != None ):
    try:
      contact_info = member_content.findAll('li',{"class":"_1zw6 _md0 _5h-n _5vb9"})
      for i in range(len(contact_info)):
        index = len(contact_info[i].div.i['class'])
        if(contact_info[i].div.div.text.count("Lives in") > 0):
          contact_detail[3] = contact_info[i].div.find('a').text
    except:
      pass

    member_name = member_content.find(id = "fb-timeline-cover-name").text
    contact_detail[2] = member_name
    driver.find_element_by_xpath("//ul[contains(@class, '_6_7 clearfix')]/li[2]/a").click()

    time.sleep(3)
    member_content = soup(driver.page_source, 'html.parser')
    if ( member_content.find(id = "collection_wrapper_2327158227").div.ul.li.text.count("send her a friend request") > 0 ):
      driver.find_element_by_xpath('//*[@id="collection_wrapper_2327158227"]/div//ul/li[2]/div/div[1]/div/div/div/a[4]').click()
    else:
      driver.find_element_by_xpath('//*[@id="collection_wrapper_2327158227"]/div//ul/li/div/div[1]/div/div/div/a[4]').click()

    time.sleep(3)
    member_content = soup(driver.page_source, 'html.parser')
    time.sleep(2)
    total_detail = member_content.find(id = "pagelet_contact").find('ul').findAll("li")

    for j in range(len(total_detail)):
      if (total_detail[j].div != None):
        detail_content = total_detail[j].div.findAll("div")
        index = len(detail_content)
        if(detail_content[0].text == "Email" ):
          contact_detail[6] = detail_content[index-1].text
        elif(detail_content[0].span.text  == "Mobile Phones"):
          contact_detail[7] = detail_content[index-1].text
        elif(detail_content[0].span.text  == "Address"):
          total_address = detail_content[index-1].findAll("li")
          if(len(total_address) == 1):
            if(hasNumbers(total_address[0].text) == True):
              address_detail = total_address[0].text.split(",")
              try:
                contact_detail[5] = re.search(r'\d+', address_detail[0]).group(0)
                contact_detail[3] = address_detail[0].replace( contact_detail[5],"")
                contact_detail[4] = address_detail[1]
              except:
                pass
            else:
              contact_detail[3] = total_address[0].text
          else:
            contact_detail[3] = total_address[0].text
            address_detail = total_address[1].text.split(",")
            contact_detail[5] = re.search(r'\d+', address_detail[0]).group(0)
            if (type(int(address_detail[0])) == int):
              contact_detail[4] = ""
            else:
              contact_detail[4] = address_detail[1]

  time.sleep(2)
  if(contact_detail[2]):
    print(contact_detail)
    for contact_detail in contact_detail:
      worksheet.write(row, col, contact_detail)
      col += 1
def main():

  driver.get("https://www.facebook.com/")

  time.sleep(2)

  driver.find_element_by_xpath('//*[@id="email"]').send_keys(login_mail)
  driver.find_element_by_xpath('//*[@id="pass"]').send_keys(login_pass)
  driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

  time.sleep(30)

  # Get scroll height
  last_height = driver.execute_script("return document.body.scrollHeight")
  k = 1
  while True:
      # Scroll down to bottom
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

      # Wait to load page
      time.sleep(5)

      # Calculate new scroll height and compare with last scroll height
      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          # If heights are the same it will exit the function
          break
      if k == 1:
        break
      k +=1
      last_height = new_height

  time.sleep(3)
  memebers_content = soup(driver.page_source, 'html.parser')
  members = memebers_content.findAll("div",{"class":"clearfix _60rh _gse"})
  group_name = memebers_content.find(id = 'seo_h1_tag').text
  
  for i in range(len(members)):
    if (limitation != ""):
      if i > 0 and i < int(limitation)+1:
        get_member(members[i].a['href'], group_name)
    else:
      if i > 0:
        get_member(members[i].a['href'], group_name)
  workbook.close()
  driver.close()
main()
