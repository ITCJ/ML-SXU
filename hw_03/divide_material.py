#!/usr/bin/python3

'''
# target
划分训练集4
测试集1
'''

text = open("/home/tcj_wsl/ML-SXU/hw_03/dicStr.txt", mode='r')
resultTrain = open("/home/tcj_wsl/ML-SXU/hw_03/retTrain.txt", mode='w')
resultValidation = open("/home/tcj_wsl/ML-SXU/hw_03/retValidation.txt", mode='w')

lineNum = 0
while True:    
    lineCache = text.readline()
    
    if not lineCache:
        break

    if (lineNum % 5) == 0:
        resultValidation.write( lineCache )
    else: 
        resultTrain.write( lineCache )

    lineNum += 1

resultTrain.close()
resultValidation.close()
text.close()




