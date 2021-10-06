# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:20:20 2019

@author: ChenD
"""


import numpy as np

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#词表到向量的转换函数

#创建了本次实验的样本
'''
Introduction:   创建了本次的实验样本
Parameters:     none
Return:         postingList, 已经经过词条切片分好之后的文档集合
                classVec, 各个词条由人工标注的文本类别
'''
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe','not','take','him','to','dog','park','stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr','licks','ate','my','steak','how','to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1表示辱骂性词汇，0表示正常言论
    return postingList,classVec

'''
Introduction:   创建不重复的单词列表
Parameters:     dataSet, 经过词条切片之后的文档集合
Return:         list(vocabSet), 不重复的单词列表list
'''
def createVocabList(dataSet):
    vocabSet = set([])  #创建空集
    for document in dataSet:
#        vocabSet = vocabSet | set(document) #两个集合的并集
        vocabSet = vocabSet.union(document) #两个集合的并集
    return list(vocabSet)

'''
Introduction:   用词汇表（即想要检查的单词）作为输入，检查输入的文档有没有相应的词汇
Parameters:     vocabList, 词汇表
                inputSet, 输入需要检查文档
Return:         returnVec, 文档向量，只包含0和1，表示词汇表中单词在输入文档中是否出现
'''
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#训练算法
'''
Introduction:   构建朴素贝叶斯分类器训练函数。
Parameters:     trainMatrix, 输入的文档矩阵，每一行都和单词表维度一样，内容为0/1，表示有无
                                相应的单词。
                trainCategory, 每篇文档类别标签所构成的向量，一维向量，维度和trainMatrix
                                的行数一致，内容为0/1，表示对应的句子是否为侮辱句子。
Return:         p0Vect, 一维向量，表示非侮辱性类别中，各个词汇的出现概率。
                p1Vect, 一维向量，表示侮辱性类别中，各个词汇的出现概率。
                pAbusive, 概率，表示整个文档中属于侮辱性的句子的概率。
Attention:      这个是分类器是基于已经分类好的文档进行构建的。此外，这里只求出了“属于侮辱性”
                的句子的概率（pAbusive），对于二分类的问题，另一个概率只需用（1-pAbusive）
                如果，遇到多分类问题。以下程序需要更改，需要求出各个分类的概率。
'''
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = np.ones(numWords); p1Num = np.ones(numWords) #创建全为1的矩阵，保证条件
                                                        #概率计算时，各项连乘不为0
    p0Denom = 2.0; p1Denom = 2.0                        #由于上述改为1，此处分母为2
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = np.log(p1Num/p1Denom)          #用log函数，是希望将连续相乘改为相加
    p0Vect = np.log(p0Num/p0Denom)
    return p0Vect,p1Vect,pAbusive


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#朴素贝叶斯分类函数
'''
Introduction:   利用构造好的朴素贝叶斯分类函数进行分类。
Parameters:     vec2Classify, 需要进行分类的文档，数据结构为一维list，内容为词表中的词，
                        例如：['love', 'my', 'dalmation']
                p0Vec, 为trainNB0输出的p0Vect
                p1Vec, 为trainNB0输出的p1Vect
                pClass1, trainNB0输出的pAbusive
Return:         1/0，1表示侮辱性文档；0表示非侮辱性
'''
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + np.log(pClass1)    #条件概率计算公式，因为用
                                                        #log函数，所以形式变成了加
    p0 = sum(vec2Classify * p0Vec) + np.log(1.0 - pClass1) #二分类问题，所以1-p
    if p1 > p0:
        return 1
    else: 
        return 0

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#测试算法
'''
Introduction:   汇总前述函数，并利用构造好的朴素贝叶斯分类函数进行分类，测试。
Parameters:     none
Return:         1/0，1表示侮辱性文档；0表示非侮辱性
                结果直接print出来
'''
def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(np.array(trainMat),np.array(listClasses))
    testEntry = ['love', 'my', 'dalmation'] #第一个测视例子
    thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid', 'garbage'] # #第二个测视例子
    thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


if __name__ == '__main__':
    testingNB()