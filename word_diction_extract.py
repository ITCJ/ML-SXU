#!/usr/bin/python3


'''
1. 总词数
2. 不同词的个数
3. 词频与排序

4. 去除语料中的分词和词性标记，生成未加工语料
'''

def inputDict(inString, dict):
    if inString in dict:
        dict[inString] += 1
    else:
        dict[inString] = 1

text = open('199801.txt', mode='r',encoding="gbk")
resultDic = open('dicResult.txt', mode='w')
resultStr = open('dicStr.txt', mode='w')
dict = {}

while True:
    lineCache = text.readline()
    lineCache.encode("utf-8")

    j = ""
    newLine = ""
    for i in lineCache:
        # print(i)
        if '\u4e00' <= i <= '\u9fa5': 
            # print(i)
            j += i
            newLine += i
        if i == '/' and j != "":
            # print(j)
            inputDict(j ,dict)
            j = "" # refresh

    newLine += '\n'
    resultStr.write(newLine)
    if not lineCache:
        break

# print(dict)

sum = 0
for i in dict:
    sum += dict[i]

print("总键数：", len(dict))
print("总词数：", sum)

#排序
dict = sorted(dict.items(), key=lambda x:x[1], reverse=False)

for i in dict:
    print(i, file=resultDic)

text.close()
resultDic.close()
resultStr.close()