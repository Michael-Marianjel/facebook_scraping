from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import random
import xlsxwriter
import datetime
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.youtube.com/watch?v=vGmQ-sIdFEI")

# time.sleep(40)
time.sleep(10)
message = "Mampir juga ke channel youtube saya ya.."
# wait = WebDriverWait(self.driver, 10)
# driver.get("http:// enter your URL.") 
myDynamicElement = driver.find_element_by_id("input[id*='search']")
print(myDynamicElement)
myDynamicElement.send_keys(message)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="test"]')))
# element.click()
# wait = WebDriverWait(driver, 10)
# wait = WebDriverWait(self.driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@id="search"]')))
# element.click()
# workbook = xlsxwriter.Workbook('results.csv')
# worksheet = workbook.add_worksheet("urls")

# row = 0
# column = 0

# time.sleep(3)
# try:
#     for i in range(4):
#         time.sleep(4)
#         driver.execute_script(
#             "window.scrollTo("+str(i*1000)+","+str((i+1)*1000)+");")

# time.sleep(3)
# elems = driver.find_elements_by_css_selector("#author-text")
# links = [elem.get_attribute('href') for elem in elems]
# # print(links)

# time.sleep(3)
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# urls = soup.find_all(
#     "a", class_='yt-simple-endpoint style-scope ytd-comment-renderer')

# for url in urls:
#     time.sleep(1)
#     driver.get("https://www.youtube.com" + url['href'])

#     time.sleep(3)
#     soup1 = BeautifulSoup(driver.page_source, 'html.parser')
#     e_urls = soup1.find_all(
#         "a", class_='yt-simple-endpoint style-scope ytd-grid-video-renderer')
#     for e_url in e_urls:
#         time.sleep(3)
#         driver.get("https://www.youtube.com" + e_url['href'])

#         print(e_url['href'])

#         time.sleep(5)
#         driver.execute_script("window.scrollTo(0, 500)")

#         time.sleep(10)
#         driver.find_element_by_xpath(
#             '//*[@id="search"]').send_keys(message)
#         driver.find_element_by_xpath('//*[@id="button"]').click()

#         time.sleep(5)
#         worksheet.write(row, 0, "https://www.youtube.com" + e_url['href'])
#         row += 1

# result1 = soup.find_all(
#     'span', {'class': 'style-scope ytd-comment-renderer'})
# result2 = soup.find_all('yt-formatted-string',
#                         {'class': 'style-scope ytd-comment-renderer'})
# title = []
# comment = []
# total = []
# for i in range(len(result1)):
#     if(re.sub("\s\s+", " ", result1[i].text).count('•') > 0):
#         continue
#     elif(re.sub("\s\s+", " ", result1[i].text) != ""):
#         title.append(re.sub("\s\s+", " ", result1[i].text))
# for i in range(len(result2)):
#     comment.append(re.sub("\s\s+", " ", result2[i].text))
# total.append(title)
# total.append(comment)
# for i in range(len(title)):
#     print(total[0])
#     worksheet.write(row, 0, re.sub("\s\s+", " ", total[0][i]))
#     worksheet.write(row, 1, re.sub("\s\s+", " ", total[1][i]))
#     row += 1
# workbook.close()
# except:
#     pass
