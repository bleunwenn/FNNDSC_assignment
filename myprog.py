
#---------- Created by Bleunwenn ALLAIR ------- March 2nd, 2018
#---------- for the FNNDSC lab - Boston -------

#python myprog.py story.txt result.json home/student/internship/in home/student/internship/out

import re
import argparse
import sys
import os

#creating an empty dictionary
dictionary = {}

#list of the four arguments needed to run the program
parser = argparse.ArgumentParser()
parser.add_argument('file_to_read', type=str)
parser.add_argument('file_to_write', type=str)
parser.add_argument('input_dir', type=str)
parser.add_argument('output_dir', type=str)

#opening input_dir/file_to_read (given in argument) in reading mode
input_doc = open(os.path.join(sys.argv[3], sys.argv[1]),'r')

#storing the content in a string, and lowering the letters so Caps won't count twice
text = input_doc.read().lower()

#in that string, recognize the words (blocks of letters separated by spaces)
pattern = re.findall(r'\b[a-z]{1,20}\b', text)

#for each word, count the number of times it appears
for word in pattern :
    count = dictionary.get(word,0)
    dictionary[word] = count +1

#counting the total of words used : this helps to normalize the frequency later
total = 0;
for element in dictionary.keys() :
    total += dictionary[element]
    
#opening output_dir/file_to_write (given in argument) in writing mode
output_doc = open(os.path.join(sys.argv[4],sys.argv[2]),'w')

#writing so it matches the JSON format
output_doc.write("{\n")

#find the normalized frequency associated to each word
#then write the words and their frequency in JSON format in the file
for words in dictionary.keys() :

    norm_freq=float(dictionary[words]/total)
    dictionary[words]=str(dictionary[words])

    output_doc.write("\t\""+words+"\": \""+str(norm_freq)+"\",\n")

output_doc.write("}")

#remembering to close the files I opened in the program
input_doc.close()
output_doc.close()
