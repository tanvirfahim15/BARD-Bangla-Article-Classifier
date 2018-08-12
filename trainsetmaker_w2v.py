# produces training set for Word2Vec
import os
import glob
import math
import operator
import numpy as np
files=[]

input_path= "words/"
os.chdir(input_path)


for file_ in glob.glob("*"):
    files.append(file_)

os.chdir('..')

trainset_file= open('trainset_w2v.csv', 'w', encoding="utf-8")
w2v_file=open('w2v.csv', encoding="utf-8").readlines()
w2v = {}
for line in w2v_file:
    if len(line.split(' ')) == 302:
        word = line.split(' ')[0]
        vector=[]
        for item in line.split(' ')[1:len(line.split(' '))-1]:
            vector.append(float(item))
        w2v[word]=vector

print('loaded ')
i=0
for file_ in files:
    category = 0
    if 'bangladesh' in file_:
        category = 0
    if 'international' in file_:
        category = 1
    if 'economy' in file_:
        category = 2
    if 'entertainment' in file_:
        category = 3
    if 'sports' in file_:
        category = 4
    vector=[0.0 for i in range(300)]
    vector=np.asarray(vector)
    freq_file = open(input_path+file_, encoding="utf-8").readlines()
    for line in freq_file:
        tokens = line.replace("\n","").split(",")
        key = tokens[0]
        value = int(tokens[1])
        if key not in w2v.keys():
            continue
        else:
            vector=vector+w2v[key]
    trainset_file.write(str(category))
    for item in vector:
        trainset_file.write(',')
        trainset_file.write(str(item))
    trainset_file.write('\n')
    i=i+1
    print(str(i)+'/'+str(len(files)))

