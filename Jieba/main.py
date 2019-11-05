# coding=utf8

'''
Jiaba function
created: November 11, 2019 01:56 PM
Last revision: November 11, 2019 01:56 PM
  
Author : Chao-Hsuan Ke
'''

import jieba

seg_list = jieba.cut("據說那些不具備增長思維的人，早晚被淘汰")

print(" / ".join(seg_list))

