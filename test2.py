# -*- coding: utf-8 -*-
import re
import sys
import jieba

reload(sys)
sys.setdefaultencoding('utf-8')

with open('flypaper_tokens.txt', 'r') as file:
    text = file.read()

sentences = text.splitlines()
count = 0
block = ''
for sentence in sentences:
    tokens = sentence.split()
    for token in tokens:
        count += 1
        block = block + token + ' '
        if count==10:
            count = 0
            print(block)
            block = ''
    block = block +'|'
