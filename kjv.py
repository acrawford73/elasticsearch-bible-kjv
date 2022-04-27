###
# Import CSV and Import into Elasticsearch
# Anthony Crawford
# December 2014
# Provided Free and Open Source
###

import os
import errno
#import datetime, time, calendar
import json
import hashlib

# Third Party Packages
from elasticsearch import Elasticsearch

# Set ES Parameters
index_name = 'bible'
doc_type_name = 'kjv'
es = Elasticsearch('sgc1')

# Import CSV
import csv
import sys

files = [
	'kjv-genesis.csv',
	'kjv-exodus.csv',
	'kjv-leviticus.csv',
	'kjv-numbers.csv',
	'kjv-deuteronomy.csv',
	'kjv-joshua.csv',
	'kjv-judges.csv',
	'kjv-ruth.csv',
	'kjv-1samuel.csv',
	'kjv-2samuel.csv',
	'kjv-1kings.csv',
	'kjv-2kings.csv',
	'kjv-1chronicles.csv',
	'kjv-2chronicles.csv',
	'kjv-ezra.csv',
	'kjv-nehemia.csv',
	'kjv-esther.csv',
	'kjv-job.csv',
	'kjv-psalms.csv',
	'kjv-proverbs.csv',
	'kjv-ecclesiastes.csv',
	'kjv-songofsolomon.csv',
	'kjv-isaiah.csv',
	'kjv-jeremiah.csv',
	'kjv-lamentations.csv',
	'kjv-ezekiel.csv',
	'kjv-daniel.csv',
	'kjv-hosea.csv',
	'kjv-joel.csv',
	'kjv-amos.csv',
	'kjv-obadiah.csv',
	'kjv-jonah.csv',
	'kjv-micah.csv',
	'kjv-nahum.csv',
	'kjv-habakkuk.csv',
	'kjv-zephaniah.csv',
	'kjv-haggai.csv',
	'kjv-zechariah.csv',
	'kjv-malachi.csv',
	'kjv-matthew.csv',
	'kjv-mark.csv',
	'kjv-luke.csv',
	'kjv-john.csv',
	'kjv-acts.csv',
	'kjv-romans.csv',
	'kjv-1corinthians.csv',
	'kjv-2corinthians.csv',
	'kjv-galatians.csv',
	'kjv-ephesians.csv',
	'kjv-philippians.csv',
	'kjv-colossians.csv',
	'kjv-1thessalonians.csv',
	'kjv-2thessalonians.csv',
	'kjv-1timothy.csv',
	'kjv-2timothy.csv',
	'kjv-titus.csv',
	'kjv-philemon.csv',
	'kjv-hebrews.csv',
	'kjv-james.csv',
	'kjv-1peter.csv',
	'kjv-2peter.csv',
	'kjv-1john.csv',
	'kjv-2john.csv',
	'kjv-3john.csv',
	'kjv-jude.csv',
	'kjv-revelation.csv'
]

print
print "Importing CSV files into Elasticsearch Index: \'Bible\'"
print

for file in files:
	print file
	f = open('csv/'+file, 'rb')
	try:
		reader = csv.reader(f)
		for row in reader:
			bible_testament = row[0]
			bible_book = row[1]
			bible_chapter = row[2]
			bible_verse = row[3]
			bible_text = row[5]
			hash_row = bible_testament + bible_book + bible_chapter + bible_verse + bible_text
			hashed = hashlib.sha256(''.join(hash_row)).hexdigest()

			json_es = {
				'testament':bible_testament,
				'book':bible_book,
				'chapter':bible_chapter,
				'verse':bible_verse,
				'text':bible_text,
				'hash':hashed,
			}

			res = es.index(index=index_name, doc_type=doc_type_name, body=json_es)
			if res['created'] == False:
				print
				print "!!!!!!!!!!!!!!!!!!!!!!!"
				print "!!! ES ENTRY FAILED !!!"
				print "!!!!!!!!!!!!!!!!!!!!!!!"
				print
				f.close()
				sys.exit()

	finally:
		f.close()

es.indices.refresh(index=index_name)

print
print "Refeshing Indexes..."
print
print "Import Completed."
print

sys.exit()