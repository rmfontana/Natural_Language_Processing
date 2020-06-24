import os
import json
import config

counter = 1
dict = {}
sentiment = ""
text = ""

with open("output.txt") as file:
        for line in file:
                if (counter % 2) == 0:
                        sentiment = line.rstrip()
                        counter = counter + 1
                else:
                        text = line.rstrip()
                        counter = counter + 1
                dict[text] = sentiment

#print(dict.keys())

dir2 = config.testing_data

os.chdir(dir2)

dict2 = {}
new_dict = {}
for file in os.listdir(dir2):
        with open(file) as json_file:
                dict2 = json.load(json_file)

        for key, value in dict2.items():
                new_dict[str(key)] = str(value)

print(len(dict))
print(len(new_dict))
right = 0
wrong = 0
total = 0
missed_keys = 0
for key, value in dict.items():
        if key in new_dict:
                if  new_dict[key] == value:
                        right = right + 1
                else:
                        wrong = wrong + 1
        else:
                missed_keys = missed_keys + 1
        total = total + 1

print("Right: " + str(right))
print("Wrong: " + str(wrong))
print("Total: " + str(total))
print("Missed keys: " + str(missed_keys))
