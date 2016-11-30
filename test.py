# -*- coding: utf-8 -*-
import codecs
import jieba
import re
import string

seg_list = jieba.cut("人家也许二刷啊   ")  # 默认是精确模式
print(", ".join(seg_list))

text='233333,太搞笑了，哈哈哈哈！'
nopunct_text=text.translate(None, string.punctuation)
#nopunct_text = ''.join(c for c in text if re.match("[a-z\-\' \n\t]", c))
print(nopunct_text)

#remove punctuations
nopunct_text = re.sub(ur"[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：；《）《》“”()»〔〕-]+", "", text.decode("utf8"))
print re.sub(ur"[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：；《）《》“”()»〔〕-]+", " ", text.decode("utf8"))