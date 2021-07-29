# -*- coding: utf-8 -*-

# App name:  Japanese Sentence Parser
# Version:  V0.1
# Author:  Nathan Butts

# App to take the 'WaniKani 4500 Japanese Sentences' and display them
# one-by-one in original Japanese, have operator input english translation
# then score them and keep the results for later

# Definitions of input file items
# Each line in CSV will have J_Sent, E_Trans, Last_Input, Score, Reason, Date_Stamp
# J-Sent = Original japanese sentence
# E-Trans = English auto translation through google translate
# Last_input = Last translation typed in by user
# Score = Self score, starts at 0, increments by:
#   |-> -1 = not known
#   |->  1 = known but difficult
#   |->  5 = easy
# Reason = reason not known
#   |-> v = vocabulary
#   |-> k = kanji
#   |-> g = grammar
# Date_Stamp = Date and time item last seen

# Basic flow of first iteration:
#
# Sort by date_stamp⇑, score⇓
# Show sentence to user
# User inputs english translation
# Google translation shown
# Ask to self score
#   |-> 1 for unknown
#   |-> 2 for known
#   |-> 3 for easy
# if 1, ask for why:
#   |-> v
#   |-> k
#   |-> g
# Update scores
# Update Last_input
# Update reason
# Update date_stamp
# go to next
# q alone at any time will close the app

import csv

sentences = []
sentencelist = []
i=0
with open('wanikani_sentences4.csv', encoding = 'utf-8') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    sentencereader = csv.reader(csvfile, dialect)
    for row in sentencereader:
        sentences = [
            row[0], # Japanese sentence
            row[1], # Google english translation
            row[2], # Last input
            row[3], # Score
            row[4], # Reason
            ]
        sentencelist.append(sentences)
    #sorted_list = sorted(sentencelist, key=lambda x: x[5])
    for item in sentencelist:
        print(item[4])
