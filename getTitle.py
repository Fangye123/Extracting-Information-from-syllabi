import re
import os
from fuzzywuzzy import fuzz
from shutil import copyfile

def checkFont(line):
    line=re.sub(' ','',line)
    line = re.sub('\n', '', line)
    if(line.startswith("**")):
        return True
    if(line.startswith("#")):
        return True
    return False


def getTitle(path, title):
    num_lines = sum(1 for line in open(path))
    # print("line number", num_lines)
    count = 0
    with open(path, "r") as ins:
        for line in ins:
            count += 1
            font = checkFont(line)
            if count/num_lines < 0.1 and font == True:
                # line=line.decode("utf-8")
                line=line.lower()

                # print("ratio: ", fuzz.token_set_ratio(title,line))
                # print(line)
                if fuzz.token_set_ratio(title,line) > 90:
                    # print(count,"-------------")
                    # print(title, "-------------title-------")
                    # print(line)
                    # print(path)
                    try:
                        new_path = 'training_dataSet' + path.replace('/Users/ziyunzhong/nlpProject/larger5kb_Md_File','')
                        copyfile(path, new_path)
                    except:
                        pass




listing = os.listdir("/Users/ziyunzhong/nlpProject/larger5kb_Md_File")
dirpath = "/Users/ziyunzhong/nlpProject/larger5kb_Md_File/"

for i in listing:
    title = i.lower()
    title = re.sub('\d+\_','', title)
    title = re.sub('\_*syllabus\_*','',title)
    title = re.sub('\_',' ', title)
    title = re.sub('\-',' ',title)
    title = re.sub('\.',' ', title)
    title = re.sub('\,',' ', title)
    title = re.sub('\s\s+',' ',title)
    title = re.sub('md','',title)
    title = re.sub('\d','',title)
    title = re.sub('^\s','',title)
    title = re.sub('\s+\w\s+','',title)
    title = re.sub('^\w\s+','',title)
    title = re.sub('\s*$','',title)

    if len(title.split(' ')) > 2:
        path = dirpath + i
        try:
            getTitle(path, title)
        except Exception as e:
            print(e)
