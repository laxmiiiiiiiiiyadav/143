from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome(r"C:\Users\HP\Desktop\python\C141-student-boilerplate-main\chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

soup = BeautifulSoup(browser.page_source, "html.parser")
table=soup.find("table")
tem_list=[]
table_rows=table[7].find_all("tr")

for x in table_rows:
    td = x.find_all("td")

    row = [i.text.rstrip() for i in td]
    tem_list.append(row)

star_name=[]
distance = []
mass = []
radius = []

for i in range(1,len(tem_list)):
    star_name.append(tem_list[i][0])
    distance.append(tem_list[i][5])
    mass.append(tem_list[i][7])
    radius.append(tem_list[i][8])
   

df2 = pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns=['star_name','distance','mass','radius'])
df2.to_csv("star2.csv")