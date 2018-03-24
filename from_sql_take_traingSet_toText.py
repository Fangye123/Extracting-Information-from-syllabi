#!/usr/bin/env python
from __future__ import print_function

import pymysql
import html2text
import re
import nltk
from bs4 import BeautifulSoup


with open('traingSetPathID.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
targetIDList = [x.strip() for x in content]



# print(targetIDList)
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='syllabus')

cur = conn.cursor()

for id in targetIDList:
    cur.execute("SELECT title, chnm_cache  FROM syllabi WHERE syllabiID = " + id)
    for row in cur:
        try:
            f = open("new/" + str(id) + "_" + row[0].replace(" ", "_").replace("/", "-") + ".txt", "w+")
            # convert html to txt
            soup = BeautifulSoup(row[1], 'html.parser')
            content = BeautifulSoup.get_text(soup)
            f.write(content)
            f.close()
        except Exception as e:
            print(e)



# print(cur.description)
# print("-----------------------------------------------")
# # row[0] is title, row[1] is html content
# for row in cur:
#     try:
#       #print(str(row[2]) + ":" + str(row[0]))
#     # new a file
#       if (int(row[2])%1000== 0):
#           print(row[2])
#
#       f = open(str(row[2]) + "_" + row[0].replace(" ", "_").replace("/", "-") + ".md", "w+")
#
#     # convert html to text
#       content = html2text.html2text(row[1])
#
#       f.write(content)
#       f.close()
#     except Exception as e:
#         print(e)






cur.close()
conn.close()
