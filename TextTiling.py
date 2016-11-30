# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import brown
import jieba


with open('flypaper_commentsOnly.txt', 'r') as file:
    comments = file.read()

#segment the word
seg_list = jieba.cut(comments)
tokenized_comments=(" ".join(seg_list))
#print(tokenized_comments)


ttt = nltk.tokenize.TextTilingTokenizer(demo_mode=True)
text = brown.raw()[:10000]
#print(text)
gap_scores, smooth_scores, depth_scores, segment_boundaries = ttt.tokenize(tokenized_comments)

print(gap_scores)
print(smooth_scores)
print(depth_scores)
print(segment_boundaries)

