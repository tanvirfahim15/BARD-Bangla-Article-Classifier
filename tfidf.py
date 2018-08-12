#Computes TF-IDF scores for tokens

import os
import glob
import math
import operator
files=[]
        
input_path= "words/"
os.chdir(input_path)


for file_ in glob.glob("*"):
    files.append(file_)
    
os.chdir('..')

doc_count={}
freq_count={}
word_count=0


for file_ in files:
	doc = open(input_path+file_, encoding="utf-8").readlines()
	for line in doc:
		tokens = line.replace("\n","").split(",")
		key = tokens[0]
		value = int(tokens[1])
		if key not in doc_count.keys():
			doc_count[key] = 1
		else:
			doc_count[key] = doc_count[key]+1

		if key not in freq_count.keys():
			freq_count[key] = 1
		else:
			freq_count[key] = freq_count[key]+value
		word_count= word_count+value


out_file = open('tfidf.txt', 'w', encoding="utf-8")
tfidf={}
for key in freq_count.keys():
	tf = freq_count[key]/word_count
	idf=math.log(len(files)/doc_count[key])
	tfidf[key]=tf*idf

sorted_tfidf= sorted(tfidf.items(), key=operator.itemgetter(1))	
for item in sorted_tfidf:
    		out_file.write(item[0]+","+str(item[1])+"\n")
out_file.close()
