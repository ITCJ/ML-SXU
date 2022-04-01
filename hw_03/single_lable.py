#!/usr/bin/python3

import re

def neighborhood(iterable):
    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield (prev_item, current_item, next_item)
        prev_item = current_item
        current_item = next_item
    yield (prev_item, current_item, None)

'''
# target 
    /B begin
    /M middle
    /E end
    /S single
'''

text = open("/home/tcj_wsl/ML-SXU/hw_03/199801.txt", mode='r',encoding="gbk")
resultStr = open('/home/tcj_wsl/ML-SXU/hw_03/dicStr.txt', mode='w')

while True:
    lineCache = text.readline()
    lineCache.encode('utf-8')
    
    if not lineCache:
        break
    
    newLine = ""
    lineCache = re.sub("/[A-z]+", "", lineCache)
    for i, j, k in neighborhood(lineCache):
        if i == None:
            newLine += j
        elif k == None:
            newLine += '\n'
        elif (i == " ") \
                    and ('\u4e00' <= j <= '\u9fa5' or '\uff10' <= j <= '\uff19') \
                    and ('\u4e00' <= k <= '\u9fa5' or '\uff10' <= k <= '\uff19') :
            newLine += j+"\B"
        elif ('\u4e00' <= i <= '\u9fa5' or '\uff10' <= i <= '\uff19') \
                    and ('\u4e00' <= j <= '\u9fa5' or '\uff10' <= j <= '\uff19') \
                    and ('\u4e00' <= k <= '\u9fa5' or '\uff10' <= k <= '\uff19'):
            newLine += j+"\M"
        elif ('\u4e00' <= i <= '\u9fa5' or '\uff10' <= i <= '\uff19') \
                    and ('\u4e00' <= j <= '\u9fa5' or '\uff10' <= j <= '\uff19') \
                    and (k == ' '):
            newLine += j+"\E"
        elif (i == " ") \
                    and ('\u4e00' <= j <= '\u9fa5' or '\uff10' <= j <= '\uff19') \
                    and (k == ' '):
            newLine += j + "\S"
        else:
            newLine += j
    
    # print(newLine)
    resultStr.write(newLine)

    
