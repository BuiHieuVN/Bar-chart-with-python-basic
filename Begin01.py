#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

    # Load file
f = csv.reader(open("/home/hieu/Desktop/browser.csv"))
    
    # Doc noi dung file
contents = []
for x in f:
    contents.append((x))
    
    # Lay hang dau tien ra ngoai
subject = contents.pop(0)
    
    # chuyen doi string thanh float va moi phan tu cua contents la 1 tuple
for x in range(len(contents)):
    for y in range(len(contents[x])):
        contents[x][y] = float(contents[x][y])
    contents[x] = tuple(contents[x])    
    
    
ind_Browsers = range(len(subject))
    
    # Ve bieu do cho moi so lieu
for x in range(len(contents)):
    plt.bar(ind_Browsers, contents[x], align='center', color=['yellow', 'blue', 'green', 'red', 'cyan'])
    plt.xticks(ind_Browsers, subject)
    
    for a, b in zip(ind_Browsers, contents[x]):
        plt.text(a, b, b, ha='center', va='bottom')
        
    plt.ylim(0, 100)
    plt.xlabel('Web browsers')
    plt.ylabel('Percentage of Usage')
    plt.title("RANK OF BROWSERS USED")
    
    plt.axis()
    plt.show()

