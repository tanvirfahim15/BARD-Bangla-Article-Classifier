# Tokenizes documents and save in sorted order on frequency
import os
import glob
import codecs
from bs4 import BeautifulSoup
import operator

# Returns words from a text
def get_vector(text):
    ret = ""
    stp=["!", "@",'–', "#", "|", "%", "(", ")", "।", "—", ".", "-", "", ",", "’", "•", "‘", ":", "*", "?",
          "০", "১", "২", "৩", "৪", "৫", "৬", "৭", "৮", "৯"]
    for x in text:
        if x in stp:
            ret = ret + " "
        else:
            ret = ret + x
    ret = ret.replace("  ", " ")
    ret = ret.replace("  ", " ")
    ret = ret.split()
    return ret
    
files=[]

output_path= "words/"
if not os.path.exists(output_path):
        os.makedirs(output_path)
        
input_path= "pages/"
os.chdir(input_path)


for file_ in glob.glob("*"):
    files.append(file_)
    
os.chdir('..')

for file_ in files:
	print(file_)
	page = open(input_path+file_).read()
	soup = BeautifulSoup(page, 'html.parser')
	name_box = soup.find('div', attrs={'itemprop': 'articleBody'})
	out_file = codecs.open(output_path+file_, 'w', encoding="utf-8")
	col = {}
	if name_box is None:
		continue
	vec = get_vector(name_box.text)
	for item in vec:
		if item in col.keys():
			col[item] = col[item]+1
		else:
			col[item] = 1
	sorted_col = sorted(col.items(), key=operator.itemgetter(1))
	sorted_col = reversed(sorted_col)
	for item in sorted_col:
    		out_file.write(item[0]+","+str(item[1])+"\n")
	out_file.close()
    

