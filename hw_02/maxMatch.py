'''
1. 正向最大匹配
    输入：未分词文本
    输出：分词结果
2. 评价程序
    准确率
    召回率
    F测度
3.  结巴、ICTCLAS、LTP 分词
    评价

4.基于上一个实验的词表和词频 一元统计语言模型的分词
    输入字串S, 取出全部候选词
    动态规划最大词串概率

'''
#词典
def inputDict(inString, dict):
    if inString in dict:
        dict[inString] += 1
    else:
        dict[inString] = 1
text = open("/home/tcj_wsl/ML-SXU/hw_01/199801.txt", mode='r',encoding="gbk")
dict = {}

while True:
    lineCache = text.readline()
    lineCache.encode("utf-8")

    j = ""
    newLine = ""
    for i in lineCache:
        if '\u4e00' <= i <= '\u9fa5' or '\uff10' <= i <= '\uff19': 
            j += i
            newLine += i
        if i == '/' and j != "":
            inputDict(j ,dict)
            j = "" # refresh

    if not lineCache:
        break

#########################
# 最大匹配
cutLenth = 7
resultStr = open('/home/tcj_wsl/ML-SXU/hw_02/dicStr.txt', mode='r')
maxMatchResult = open('/home/tcj_wsl/ML-SXU/hw_02/maxMatch.txt', mode='w')
while True:
    lineCache = resultStr.readline()
    j = ""
    newLine = ""
    jLen = 0
    for i in lineCache:
        j += i
        jLen += 1
        if(dict.get((j))):      # 这里不匹配可能出现的更长串
            continue
        else:
            newLine += j[0:jLen-1] + "/"
            j = i
            jLen = 1
    newLine += '\n'
    
    maxMatchResult.write(newLine)
    # print(newLine)
    # break

    if not lineCache:
        break
        
maxMatchResult.close()