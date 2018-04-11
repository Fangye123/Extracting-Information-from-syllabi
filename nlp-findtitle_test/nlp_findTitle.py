from gensim.models import word2vec
import nltk
import logging
import string
import re
import pandas as pd
import numpy as np
from keras.models import load_model
import os
import pdf2txt

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_datafile_tags(data,model):
    words=data.split()
    tagged_sent=nltk.tag.pos_tag(words)
    word_vector=[]
    title_position=[]
    a=[]
    count=0
    for i in range(0,32):
        a.append(0)
    for line in data.splitlines():
        count+=1
        words=line.split()
        for word in words:
            title_position.append(count)
            if not is_number(word):
                if word in model.wv.vocab:
                    word_vector.append(model[word])
                else:
                    word_vector.append(a)
            else:
                word_vector.append(a)
    return tagged_sent,word_vector,title_position,count

def get_posList(tagged_data):
    pos_list=[]
    for i in range(0,len(tagged_data)):
        pos_list.append(tagged_data[i][1])
        i=i+1
    return pos_list

def get_wordList(tagged_data):
    word_list=[]
    for j in range(0,len(tagged_data)):
        word_list.append(tagged_data[j][0])
        j=j+1
    return word_list

def word_encoded_pair(wordlist,onehot_encoded,word_vector,title_position,total):
    out = ""
    for i in range(0, len(wordlist)):
        a=list(word_vector[i])+onehot_encoded[i]
        a+=[title_position[i],title_position[i]/total]
        a=str(a)
        a=re.sub('[\[\]]','',a)
        out+=a
        out+="\n"
    return out

def convertTxtToMatric(data):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model=word2vec.Word2Vec.load("nlp.model")
    poslist = []
    wordlist = []
    tagged_data, word_vector, title_position, total = get_datafile_tags(data, model)
    poslist = get_posList(tagged_data)
    wordlist = get_wordList(tagged_data)
    POS_tags = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT',
                'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP',
                'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB', '$', '#', '"',
                '"', '(', ')', ',', '.', ':']
    # define a mapping of chars to integers
    char_to_int = dict((c, i) for i, c in enumerate(POS_tags))
    int_to_char = dict((i, c) for i, c in enumerate(POS_tags))
    integer_encoded = [char_to_int[char] for char in poslist]
    onehot_encoded = []
    for value in integer_encoded:
        tag = [0 for _ in range(len(POS_tags))]
        tag[value] = 1
        onehot_encoded.append(tag)

    with open('test_data.txt', "w")as f:
        print(word_encoded_pair(wordlist,onehot_encoded, word_vector, title_position, total), file=f)


def predict(trainedModelPath, testDataPath):
    """
        input:
        modelPath: Path of the trained model. E.g:
        testDataPath: Path of the test data file. This should be a matrix. e.g.:'./data_5.txt'
    """
    # get test data input
    test_data = pd.read_csv(testDataPath, sep=",", header=None, dtype="float").values
    # Load the trained Model
    model = load_model(trainedModelPath)
    # Use the model to predict
    prediction = np.where(model.predict(test_data) > 0.5, 1, 0)
    # Save to file
    np.savetxt(r'prediction.txt', prediction, fmt='%d')
    return prediction

def predictTitle(data,predictionPath):
    result=open(predictionPath,"r",encoding="utf-8").read()
    result = result.splitlines()
    data = data.splitlines()
    index = -1
    flag = False
    title = ""
    for line in data:
        count = 0
        for word in line.split():
            index += 1
            if (result[index] == '1'):
                count += 1
        if (count > 0.5 * len(line.split())):
            flag = True
            title = line

    if flag:
        print(title)
    else:
        print("cannot find title")


data=open("syllabus.txt","r",encoding="utf-8").read()
data = data.lower()
for punc in string.punctuation:
    data = data.replace(punc,' ')

convertTxtToMatric(data)
prediction = predict("TrainingData_Linear_Regression_10_epochs.h5","test_data.txt")
np.savetxt(r'test_data_prediction.txt', prediction, fmt='%d')
predictTitle(data,"test_data_prediction.txt")