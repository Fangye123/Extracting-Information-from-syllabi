#!/usr/bin/env python
from __future__ import print_function

import pymysql
import html2text
import re

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='syllabus')

cur = conn.cursor()

cur.execute("SELECT title, chnm_cache, syllabiID FROM syllabi")

print(cur.description)

print("-----------------------------------------------")
# row[0] is title, row[1] is html content
for row in cur:
    try:
      #print(str(row[2]) + ":" + str(row[0]))
    # new a file
      if (int(row[2])%1000== 0):
          print(row[2])

      f = open(str(row[2]) + "_" + row[0].replace(" ", "_").replace("/", "-") + ".md", "w+")

    # convert html to text
      content = html2text.html2text(row[1])

      f.write(content)
      f.close()
    except Exception as e:
        print(e)






cur.close()
conn.close()
