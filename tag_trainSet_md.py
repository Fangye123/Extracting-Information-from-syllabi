import os
path = '/Users/ziyunzhong/nlpProject/training_dataSet_md/'

for filename in os.listdir(path):
    filename = path + filename
    # print(filename)
    with open(filename) as fp:
       line = fp.readline()
       cnt = 1
       while line:
           # print("Line {}: {}".format(cnt, line.strip()))
           line = fp.readline()
           cnt += 1
