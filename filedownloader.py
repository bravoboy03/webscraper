import random
from urllib import request
import matplotlib.pyplot as plt
import requests
# import urllib.request
from bs4 import BeautifulSoup


def downloadImage(url):
    name=str(random.randrange(1,100))+".jpg"
    request.urlretrieve(url,name)

downloadImage("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")

def downloadCSV(url):
    response=request.urlopen(url)
    csv=response.read()
    csv_str=str(csv)
    lines=csv_str.split("\\n")
    dest=r"sample.csv"
    file=open(dest,"w")
    for i in lines:
        file.write(i+"\n")
    file.close()

#downloadCSV("https://query1.finance.yahoo.com/v7/finance/download/AMZN?period1=1545196250&period2=1576732250&interval=1d&events=history&crumb=FO5QlkC0GZs")

def search(mp=2):
    page=1
    url="https://www.google.com/search?q="
    search="corona virus"
    s2=search.split(" ")
    for i in s2:
        url=url+r"+"+i
    print(url)
    sc=requests.get(url)
    sc=sc.text
    soup=BeautifulSoup(sc,features="html.parser")
    #print(soup)
    for link in soup.findAll("div",{"class":"r"}):

        print(link)
    #print(soup)

    #LC201b




x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]
scatter(x,y, label='skitscat', color='k', s=25, marker=“o”)
xlabel('x')
ylabel('y')
title('Scatter Plot')
legend()


search(3)
