import os
from bs4 import BeautifulSoup
import requests
import os.path
import json
from task1 import adventure_movie
import pprint
def final(text):
    return "".join(text.split())
def scrop_movise_detaile(movise_url):
    dic={}
    page=requests.get(movise_url)
    soup=BeautifulSoup(page.text,"html.parser")
    container=soup.find("ul",class_="content-meta info")
    all=container.find_all("li",class_="meta-row clearfix")
    for i in range(len(all)):
        if i ==1:
            dic[final((all[i].find("div",class_="meta-label subtle")).text)]=final((all[i].find("div",class_="meta-value genre").text))
        else:
            dic[final((all[i].find("div",class_="meta-label subtle")).text)]=final((all[i].find("div",class_="meta-value").text))
    with open("4_task","w")as file:
        json.dump(dic,file,indent=3)
    print(dic)
scrop_movise_detaile("https://www.rottentomatoes.com/m/black_panther_2018")