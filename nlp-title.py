import re
from fuzzywuzzy import fuzz

def getTitle(path,title):
    text=""
    title = title.lower()
    title = re.sub(' syllabus', '', title)
    total=0
    with open(path, 'rb') as myFile:
        for line in myFile:
            total+=1
            line=line.decode("utf-8")
            line=line.lower()
            text+=line
            print(fuzz.token_set_ratio(title,line))
    myFile.close()

getTitle('./syllabusMarkdown/2_History_331_Syllabus,_Roman_Imperial_History_2002.md',"History 331 Syllabus, Roman Imperial History 2002")
