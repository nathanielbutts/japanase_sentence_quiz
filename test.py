import csv
from datetime import datetime

list = []
lists = []

format = '%Y%m%d%H%M%S'

with open('Japanese Sentence Parser/wanikani_sentences.tsv', newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    sentencereader = csv.reader(csvfile, dialect)
    for row in sentencereader:
        list.extend(row[0])
        list.extend(row[1])
        list.extend('   ')
        list.extend(str(0))
        list.extend(' ')
        list.extend(datetime.now().strftime(format))
        list.extend('\n')
        # lists = list.append
    with open('Japanese Sentence Parser/wanikani_sentences2.tsv', 'w') as writefile:
        writefile.writelines(list)