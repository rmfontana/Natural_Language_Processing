import os
import json
import ast
import config

dir = config.clean
os.chdir(dir)

for file in os.listdir(dir):
        with open(file, 'r') as f:
                reading_dict = json.load(f)
                cutoff = len(reading_dict)*1/4
                print(cutoff)
                training_set = [value for value in reading_dict.values()[:cutoff]]
                testing_set = [value for value in reading_dict.values()[cutoff:]]
                print("There are %d training instances and %d testing instances", (len(training_set), len(testing_set)))
                with open(file + ".TRAIN", "w") as f2:
                        f2.write(json.dumps(training_set))
                with open(file + ".TEST", "w") as f3:
                        f3.write(json.dumps(testing_set))
