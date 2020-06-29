from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import os
import re
import csv 

titles=['Profile Link', "Group Name", 'Profile Name', 'Address', 'State', "Zip Code", "E-mail Address", 'Phone']
with open('Facebook_group_memeber_scraping.csv', mode='a', encoding="utf8", newline='') as header_title:
    student_writer = csv.writer(header_title, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    student_writer.writerow(titles)

lk = os.path.join(os.getcwd(), "chromedriver",)
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(lk, options=chrome_options)

# def element_identify():
#     if variable==None: return 'None'
#     else: return variable.text
def hasNumbers(inputString):
  return bool(re.search(r'\d', inputString))
def get_member(link, group_name):
  try:
    contact_detail = ['','','','','','','','']
    contact_detail[0] = link
    contact_detail[1] = group_name
    driver.get(link)
    time.sleep(3)
    member_content = soup(driver.page_source, 'html.parser')
    try:
      contact_info = member_content.findAll('li',{"class":"_1zw6 _md0 _5h-n _5vb9"})
      for i in range(len(contact_info)):
        index = len(contact_info[i].div.i['class'])
        if(contact_info[i].div.i['class'][index-1] == "sx_1112e7"):
          contact_detail[3] = contact_info[i].div.find('a').text
    except:
      pass

    member_name = member_content.find(id = "fb-timeline-cover-name").text
    contact_detail[2] = member_name
    driver.find_element_by_xpath("//ul[contains(@class, '_6_7 clearfix')]/li[2]/a").click()
    
    time.sleep(3)
    member_content = soup(driver.page_source, 'html.parser')
    time.sleep(2)
    total_detail = member_content.find("ul",{"class":"uiList _5yql _4kg"}).findAll("li")
    for j in range(len(total_detail)):
      if (total_detail[j].div != None):
        detail_content = total_detail[j].div.findAll("div")
        index = len(detail_content)
        if(detail_content[0].div.i['class'][2] == "sx_896b3a"):
          contact_detail[6] = detail_content[index-1].text
        elif(detail_content[0].div.i['class'][2] == "sx_1be44d"):
          phone_number = detail_content[index-1].text
        elif(detail_content[0].div.i['class'][2] == "sx_6c0b45"):
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
            contact_detail[4] = address_detail[1]
  except:
    pass
  # contact_detail[7] = "+56 9 8293 7832"
  time.sleep(2)
  print(contact_detail)
  with open('Facebook_group_memeber_scraping.csv', mode='a', encoding="utf8", newline='') as contact_details:
      student_writer = csv.writer(contact_details, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      student_writer.writerow(contact_detail)
def main():
  driver.get("https://www.facebook.com/")

  login_mail = "ckjaner2@gmail.com"
  login_pass = "Helloworld1"

  time.sleep(2)

  driver.find_element_by_xpath('//*[@id="email"]').send_keys(login_mail)
  driver.find_element_by_xpath('//*[@id="pass"]').send_keys(login_pass)
  driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
  
  driver.get("https://www.facebook.com/groups/1310022065801315/members/")
  # Get scroll height
  last_height = driver.execute_script("return document.body.scrollHeight")

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
      last_height = new_height

  time.sleep(5)
  memebers_content = soup(driver.page_source, 'html.parser')
  members = memebers_content.findAll("div",{"class":"clearfix _60rh _gse"})
  group_name = memebers_content.find(id = 'seo_h1_tag').text
  for i in range(len(members)):
    if i > 6:
      get_member(members[i].a['href'], group_name)

main()