from maxMatch import inputDict
import jieba as jb
import pynlpir as ic

# answerFile = open('/home/tcj_wsl/ML-SXU/hw_02/testAn.txt', mode='r') # , encoding="gbk"
# testFile = open('/home/tcj_wsl/ML-SXU/hw_02/testMa.txt', mode='r')

jiebaSource = open('/home/tcj_wsl/ML-SXU/hw_02/dicStr.txt', mode='r')
answerFile = open('/home/tcj_wsl/ML-SXU/hw_02/199801.txt', mode='r', encoding="gbk") 
testFile = open('/home/tcj_wsl/ML-SXU/hw_02/maxMatch.txt', mode='r')

# --------- counter ----------
totalWord = 0
findedWord = 0
successWord = 0

jiebaSuccessWord = 0

icTotalWord = 0
icSuccessWord = 0
# ----------------------------

while True:
    answerLine = answerFile.readline()
    answerLine.encode("utf-8")

    testLine = testFile.readline()
    jiebaLine = jiebaSource.readline()
    # print(answerLine)
    # print(testLine)

    answerWord = ""
    answerList = []
    
    testWord = ""
    testDict = {}

    answerLocation = 0
    for i in answerLine:
        if '\u4e00' <= i <= '\u9fa5':
            answerWord += i
            answerLocation += 1
            
        if i == '/' and answerWord != "":
            totalWord += 1
            answerList.append(answerWord + str(answerLocation))
            print(answerList)
            answerWord = ""
    
    testLocation = 0
    for i in testLine:
        if '\u4e00' <= i <= '\u9fa5':
            testWord += i
            testLocation += 1
            
        if i == '/' and testWord != "":
            findedWord += 1
            inputDict(testWord + str(testLocation), testDict)
            # print(testDict)
            testWord = ""
        
    while len(answerList):
        if( testDict.get(answerList.pop()) ):
            successWord += 1
    
    # jieba
    wordLocation = 0
    for i in jb.cut(jiebaLine, False, True, True):
        wordLocation = jiebaLine.index(i)
        wordLocation += len(i)
        print(i+str(wordLocation))
        if(testDict.get(i+str(wordLocation))):
            jiebaSuccessWord += 1
    
    # ictclas
    ic.open()
    icWord = ""
    icResult = ic.segment(jiebaLine)
    wordLocation = 0
    for i in icResult:
        if '\u4e00' <= i <= '\u9fa5':
            icWord += i
            wordLocation += 1
            
        if i == '\'' and icWord != "":
            icTotalWord += 1
            if(testDict.get(icWord + str(wordLocation))):
                icSuccessWord += 1
            icWord = ""


    break 
    if not (answerLine and testLine):
        break    

p = successWord/totalWord
jp = jiebaSuccessWord/totalWord
r = findedWord/totalWord
print("--------------------------")
print("Precision=", p)
print("jiebaPrecision=", jp)
print("Recall=", r)
print("F-measure=", (2*p*r)/(p+r))

print("--------------------------")
print("successWord=\t", successWord)
print("findedWord=\t", findedWord)
print("todtalWord=\t", totalWord)
    




