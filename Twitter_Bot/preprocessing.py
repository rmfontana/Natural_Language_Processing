from nltk.tokenize import word_tokenize
import config
import ast
import os
import re
import json

dir = config.dir
os.chdir(dir)

for file in os.listdir(dir):
        with open(file, 'r') as f:
                open_file = f.read()
                new_dict = {}
                newer_dict = {}
                counter = 0
                new_dict = ast.literal_eval(open_file)
           
                for text in new_dict:
                        text = re.sub(r'RT @[\w)]+:', '', text) #remove RT retweet garbage
                        text = re.sub(r'https?:\/\/.*[\r\n]*', '', text) #remove hyperlinks
                        text = (text.decode("ascii", errors="ignore").encode()) #thanks donaldtrump
                        text = re.sub(r'#', '', text) #remove pound signs
                        text = re.sub(r'\\', '', text) #remove backslashes
                        text = re.sub(r'\/', '', text) #remove forwardslashes
                        text = re.sub(r'\"', '', text) #remove double quotes
                        text = re.sub(r'\'', '', text) #remove single quotes
                        newer_dict[counter] = text
                        counter = counter + 1
                with open(file + ".CLEAN", "w") as f2:
                        f2.write(json.dumps(new_dict))
