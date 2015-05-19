#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Fei'

import urllib3
from bs4 import BeautifulSoup
import re
import codecs

f = open("searchcoverage.txt")
stock = []
for line in f: # get universe
    l = line.split("|")
    if l[3] != "": #get coverage
        ticker = l[1]
        name = l[2]
        link = l[3]
        stock.append([ticker, name, link])
f.close()

def choose_market(suffix):
    market = []
    for i in range(len(stock)):
        if suffix in (stock[i][0]):
            market.append(stock[i])
    return market

def analyst(link):
    u = "http://publicresearch.barclays.com/eq/" + link + ".htm"
    http = urllib3.PoolManager()
    #print (u)
    url = http.request('GET', u)
    soup = BeautifulSoup(url.data) #get html
    b = soup.find_all("b") #get all in bold
    a = b[3].text.split(" - ")
    analyst = (b[1].text,a[0],a[1])
    #currency = soup.find(text=re.compile("^Currency"))
   # c = currency.split("=")
   # currency = c[1]
    return analyst



def gettarget(link):
    u = "http://publicresearch.barclays.com/priceTable/" + link + ".htm"
    url = http.request('GET', u)
    soup = BeautifulSoup(url.data)
    target = [] # initiate price target
    rows = soup.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        target.append([ele for ele in cols])

hk = choose_market("HK")
hk_n = len(hk)

def save_to_file(market):
    m = choose_market(market) # inside m: 0 = ticker, 1 = stock name, 2 = link
    f = open('output.txt','w')
    for i in range(len(m)):
        a = analyst(m[i][2])
        f.write(a[0]+"|"+a[1]+"|"+a[2]+"\n")
    f.close()
    print ("OK!")

save_to_file("HK")


'''
for i in range(len(hk)):
    a = analyst(hk[i][2])
    print (a)
#print (target)

print(stock[5])
print (len(stock))
#print(url.data)
'''

