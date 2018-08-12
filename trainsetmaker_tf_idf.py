# produces training set for TF-IDF
import os
import glob
import math
import operator

files = []

input_path = "words/"
os.chdir(input_path)

for file_ in glob.glob("*"):
    files.append(file_)

os.chdir('..')

tf_idf_file = open('tf_idf.txt', encoding="utf-8").readlines()
tf_idf = {}
for line in tf_idf_file:
    tokens = line.replace("\n", "").split(",")
    key = tokens[0]
    value = float(tokens[1])
    tf_idf[key] = value

feature_count = 3000
features_file = open('featureVec.txt', encoding="utf-8").readlines()
features = []

for i in range(feature_count):
    features.append(features_file[i].split(",")[0])

trainset_file = open('trainset.csv', 'w', encoding="utf-8")

for file_ in files:
    print(file_)
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
    freq_file = open(input_path + file_, encoding="utf-8").readlines()
    words = []
    for line in freq_file:
        tokens = line.replace("\n", "").split(",")
        key = tokens[0]
        words.append(key)
    featureVec = []
    for feature in features:
        if feature in words:
            featureVec.append(tf_idf[feature])
        else:
            featureVec.append(0.0)
    trainset_file.write(str(category))
    for item in featureVec:
        trainset_file.write(',')
        trainset_file.write(str(item))
    trainset_file.write('\n')
trainset_file.close()
