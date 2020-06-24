import nltk
import os
import json
import config
from nltk.tokenize.casual import TweetTokenizer
from nltk.classify import NaiveBayesClassifier
import csv

dir = config.training_data
dir2 = config.testing_data


#Training
os.chdir(dir)

training_set = []  # [({word, word, word}, Positive)]
word_list = [] #all training words  [word, word, word]
input = [] #formatted for classifier [{word: true, word: false}]

tokenizer = TweetTokenizer(preserve_case=False)

#Training tokenizer
for file in os.listdir(dir):
        with open(file) as json_file:
                dict = json.load(json_file) #these are all of the tweets from one politician
                for key, value in dict.items():
                        tokens = tokenizer.tokenize(str(key))
                        
                        if value == "Positive":
                                training_set.append((tokens, "Positive"))
                        elif value == "Negative":
                                training_set.append((tokens, "Negative"))
#Training feature extraction
for key, value in training_set:
        word_list.extend(key)


frequencylist = nltk.FreqDist(word_list)
features = frequencylist.keys()                 #all are in it
#features = frequencylist.most_common(4000)     #none are in it

#Making the feature set
for key, value in training_set:
        intermediate_dict = {}
        for i in key:
                if i in features:
                        intermediate_dict[i] = True
                else:
                        intermediate_dict[i] = False
        
        input.append((intermediate_dict, value)) #[({word: True, word: False}, Positive)]


classifier = NaiveBayesClassifier.train(input)
print(classifier.show_most_informative_features(20))

#Testing
os.chdir(dir2)

testing_set = []
testing_list = []
tweet = ""
outputtxt = ""

#Tokenize
for file in os.listdir(dir2):
        with open(file) as json_file:
                dict = json.load(json_file)
                for key, value in dict.items():
                        tweet = (str(key))
                        tokens = tokenizer.tokenize(str(key))
                        for token in tokens:
                                testing_set.append(token)

                        #Features
                        output = {}
                        for i in testing_set:
                                if i in features:
                                        output[i] = True
                                else:
                                        output[i] = False

accuracy = nltk.classify.util.accuracy(classifier, outputtxt)
print(accuracy)
