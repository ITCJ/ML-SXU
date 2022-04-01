#!/usr/bin/python3

import re

# -----------------------------词统计
'''
各个词性的个数
word+词性的个数
词性在句首个数
句子个数

19980101-01-001-001  迈\B向\E  充\B满\E  希\B望\E  的\S  新\S  世\B纪\E  ——  一\B九\M九\M八\M年\E  新\B年\E  讲\B话\E  （  附\S  图\B片\E  １\S  张\S  ）  
'''

def inputDict(inString, dict):
    if inString in dict:
        dict[inString] += 1
    else:
        dict[inString] = 1

text = open("/home/tcj_wsl/ML-SXU/hw_03/retTrain.txt", mode='r')

propertyDict = {}
wordsDict = {}
firstDict = {}
strNum = 0

while True:
    lineCache = text.readline()
    if not lineCache:
        break
        
    pattern = re.compile(r'.\\[B,M,E,S]')   #字\标注
    pattern2 = re.compile(r"\\[B,M,E,S]")   #标注
    words = pattern.findall(lineCache)
    propertys = pattern2.findall(lineCache)
    # print(lineCache)
    # print(words)
    # print(propertys)

    if len(propertys) == 0:
        continue
    strNum += 1
    
    # print(propertys[0],strNum)

    inputDict(propertys[0], firstDict)
    for i in words:
        inputDict(i, wordsDict)
    for i in propertys:
        inputDict(i, propertyDict)

    # break

print(propertyDict)
print(wordsDict)
print(firstDict)
print(strNum)
