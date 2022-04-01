#!/usr/bin/python3

# -----------------------------词统计
'''
各个词性的个数
word+词性的个数
词性在句首个数
句子个数
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
    strNum += 1
        
    property = lineCache.split("/", -1)
    words = lineCache.split(" ", -1)

    property.pop(0)
    words.pop(0)
    
    first = True
    for i in property:
        i = i.split(" ")
        if first:
            inputDict(i[0], firstDict)
            first = False 
        inputDict(i[0], propertyDict)

    for i in words:
        if i == '': continue
        inputDict(i, wordsDict)

    # break

print(propertyDict)
# print(wordsDict)
# print(firstDict)
# print(strNum)
