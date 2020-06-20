"""The purpose of this script is just to convert the 'final' csv to a 'final'
json file for the app. I didn't want to use pandas or anything ourside of the
standard library.
"""
import csv
import json

with open('languages_final.csv', newline='') as fin:
    reader = csv.reader(fin)
    rawdata = list(reader)

rawdata.pop(0) # pop the headers from the csv

# the final json structure is
# { status: { language: [codes...] } }
languages = {}
for row in rawdata:
    status = row[3]
    if status not in languages:
        languages[row[3]] = {}
    language = row[1]
    if language not in languages[status]:
        languages[status][language] = []
    code = row[-1]
    if code not in languages[status][language]:
        languages[status][language].append(code)

with open('languages.json', 'wt') as fout:
    json.dump(languages, fout)
