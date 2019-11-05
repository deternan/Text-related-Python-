# coding=utf8

'''
Jiaba function
created: November 11, 2019 01:56 PM
Last revision: November 11, 2019 02:04 PM
  
Author : Chao-Hsuan Ke
'''

import jieba
import jieba.posseg as pseg

seg_list = jieba.cut("據說那些不具備增長思維的人，早晚被淘汰")

print(" / ".join(seg_list))


def jieba_parse(original_sentense): 
 words = pseg.cut(original_sentense)
 for w in words:
     print(w)     
     

 
 
jieba_parse("柯文哲是台北市長")
