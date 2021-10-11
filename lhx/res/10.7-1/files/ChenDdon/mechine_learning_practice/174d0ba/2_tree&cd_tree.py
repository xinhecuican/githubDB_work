# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:00:32 2019

@author: ChenD

Introduction: classify list by using decision-making tree

Modify: 2019-3-8
"""


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#建造树的例子
import math
import operator

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#计算给定树数据的香农熵
'''
Parameter:
    dataSet: 数据集，数据结构为list
Return:
    shannonEnt: 香农熵，数值
'''
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet: #统计各个特征出现的次数
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * math.log(prob,2) #log函数底数为2
    return shannonEnt

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#按照给定特征划分数据集
'''
Parameter:
    dataSet:待划分的数据集
    axis: 划分数据集的特征
    value: 需要返回的的数据子集特征（划分之后会产生多个数据子集，因此这里选择一个返回）
Return:
    retDataSet：复合value这个特征的数据子集
'''
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]     #按照axis这个特征划分数据集
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#选择最好的划分方式来划分当前数据集
'''
Parameter:
    dataSet:待划分的数据集
Return:
    bestFeature：能给出最佳划分的特征
'''
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)   #原始数据集的香农熵
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):        #遍历所有特征
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)       #获取无重复的特征
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)     
        infoGain = baseEntropy - newEntropy     #计算熵增益
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain         #储存熵增益大的特征
            bestFeature = i
    return bestFeature                      #返回最佳特征

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#决定叶子节点的分类
'''
Parameter:
    classList:待划分的数据，是一个叶子节点
Return:
    sortedClassCount[0][0]：通过多数表决的方法决定出来的叶子节点的分类
'''
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), 
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#构建树
'''
Parameter:
    dataSet: 待划分的数据集
    labels: 特征
Return:
    myTree：树的信息，通过字典来储存
Introduction:
    这里用递归的方法将数据集拆解，构建树
'''
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList): 
        return classList[0]     #当所有实例都具有相同的分类则停止划分
    if len(dataSet[0]) == 1:    #当遍历完所有划分数据集的属性时停止划分
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])   #删除已经使用过的特征，这里的删除将会影响labels的特征数量
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]       #复制所有特征，因此不会打乱原有特征集
        myTree[bestFeatLabel][value] = createTree(
                splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#使用决策树的分类
'''
Parameter:
    inputTree: 已经构建好的树tree
    featLabels: 特征
    testVec: 要进行分类的数据list
Return:
    classLabel：分类的标签结果
Introduction:
    这里也用递归的方法将测试数据依次传递直到给出测试结果
'''
def classify(inputTree,featLabels,testVec):
    firstStr = next(iter(inputTree))    #获取已经构建的树的结点
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict):       #判断是不是字典
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else:
        classLabel = valueOfFeat
    return classLabel

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#将构建好的树储存到文件中
'''
Parameter:
    inputTree: 已经构建好的树tree
    filename: 储存树结构的文件名
Return: none
'''
def storeTree(inputTree,filename):
    import pickle
    with open(filename,'wb') as fw:     #这里用二进制写入文本
        pickle.dump(inputTree,fw)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#获取文件中的树结构
'''
Parameter:
    filename: 储存树结构的文件名
Return: 
    pickle.load(fr): 读取的树结构
'''
def grabTree(filename):
    import pickle
    with open(filename,'rb') as fr:     #这里用二进制读取文本
        return pickle.load(fr)



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#运行
if __name__ == '__main__':
    dataSet, labels = createDataSet()           #创建测试的数据集，特征
#    print(calcShannonEnt(dataSet))             #信息熵的计算
#    print(splitDataSet(dataSet, 0, 1))         #测试分类
#    print(chooseBestFeatureToSplit(dataSet))   #查看数据集最佳的分类特征
#    print(majorityCnt(classList))

    labels0 = labels[:]       #copy一下label，因为下一步建树的过程会使特征数量减少
    myTree = createTree(dataSet,labels0)        #构建决策树
#    print(classify(myTree,labels,[1,1]))       #测试用决策树判断数据[1,1]
    storeTree(myTree,'cd_Tree')                 #储存上面构建的决策树
    print(grabTree('cd_Tree'))                  #提取之前构建的决策树