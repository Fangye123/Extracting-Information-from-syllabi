#feature POS-Onehot


import re
from nltk import tag


def get_datafile_tags():

#filename
    with open("10013_Syllabus_for_HY_390_--_Hitler_&amp;_Nazi_Germany.txt","r") as fp:
        readfile = fp.read()
        text=re.sub(r'\s+', ' ',readfile)
        #print(text)
        #for word in text:
        str=text.split()
        #print(str)
        tagged_sent=tag.pos_tag(str)
    return (tagged_sent)
#print(get_datafile_tags())

def get_posList():
    pos_list=[]
    data=get_datafile_tags()
    #data = [('Syllabus', 'NNP'), ('for', 'IN'), ('HY', 'NNP'), ('390', 'CD')]
    for i in range(0,len(data)):
        pos_list.append(data[i][1])
        #print(data[i][1])
        i=i+1
    return pos_list

def get_wordList():
    word_list=[]
    #data = [('Syllabus', 'NNP'), ('for', 'IN'), ('HY', 'NNP'), ('390', 'CD')]
    data =get_datafile_tags()
    #print(data)
    for j in range(0,len(data)):
        word_list.append(data[j][0])
        #print(data[i][1])
        j=j+1
    return word_list

poslist=[]
wordlist=[]
poslist=get_posList()
wordlist=get_wordList()

#defind the order of POS_tag
POS_tags = ['CC','CD','DT','EX','FW','IN','JJ','JJR','JJS','LS','MD','NN','NNS','NNP','NNPS','PDT','POS','PRP','PRP$','RB','RBR','RBS','RP',
            'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN','VBP','VBZ','WDT','WP','WP$','WRB','$','#','"','"','(',')',',','.',':']

# define a mapping of chars to integers
char_to_int = dict((c, i) for i, c in enumerate(POS_tags))
int_to_char = dict((i, c) for i, c in enumerate(POS_tags))

# integer encode input data
integer_encoded = [char_to_int[char] for char in poslist]


#print(integer_encoded)

# one hot encode
onehot_encoded = []
for value in integer_encoded:
       tag = [0 for _ in range(len(POS_tags))]
       tag[value] = 1
       onehot_encoded.append(tag)
print(onehot_encoded)

#word+encoded
def word_encoded_pair():
    out = []
    for i in range(0, len(wordlist)):
        out.append((wordlist[i], onehot_encoded[i]))
    return out
print(word_encoded_pair())

#word+encoded
def word_encoded_pair():
    out = []
    for i in range(0, len(wordlist)):
        #print(i)
        out.append((wordlist[i], onehot_encoded[i]))
    return out

#print(word_encoded_pair())
#nltk.help.upenn_tagset()


with open('10013_Syllabus_for_HY_390_--_Hitler_&amp;_Nazi_Germany_POS.txt','wt') as f:
    print(word_encoded_pair(),file=f)




