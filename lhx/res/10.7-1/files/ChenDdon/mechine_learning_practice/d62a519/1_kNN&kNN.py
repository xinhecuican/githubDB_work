# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:07:45 2019
@author: ChenD
"""

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#收集数据
#这里提供的datingTestSet2.txt文件就是收集到的数据

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#准备数据：将收集的到的数据转换成格式化的数据格式
import numpy as np
def file2matrix(filename):
    with open(filename) as fr:
        lines = fr.readlines()
        numberOfLines = len(lines)         #获取文件行数
        returnMat = np.zeros((numberOfLines,3))        #准备回传的矩阵-零矩阵
        classLabelVector = []                       #准备返回的结果数值-空list
        index = 0
        for line in lines:
            line = line.strip()
            listFromLine = line.split('\t')
            returnMat[index,:] = listFromLine[0:3]
            classLabelVector.append(int(listFromLine[-1]))
            index += 1
    
    #数据归一化的部分
    dataSet = returnMat
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m,1))
    normDataSet = normDataSet/np.tile(ranges, (m,1))   #element wise divide
    
#    return returnMat,classLabelVector
    return normDataSet,classLabelVector,ranges, minVals


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#分析数据，可以用matplotlib创建可视化的图形
def analyseShow(datingDataMat, datingLabels):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif']=['Microsoft YaHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    
    fig = plt.figure(figsize=[8,8],tight_layout=True)
    ax1 = fig.add_subplot(221)
    ax1.scatter(datingDataMat[:,1],datingDataMat[:,2],
                15*np.array(datingLabels),15*np.array(datingLabels),
                alpha=0.7)
    ax1.set_xlabel(r'玩视频游戏所耗时间百分比')
    ax1.set_ylabel(r'每周消费的冰淇淋公升数')
    
    ax2 = fig.add_subplot(222)
    ax2.scatter(datingDataMat[:,0],datingDataMat[:,1],
                15*np.array(datingLabels),15*np.array(datingLabels),
                alpha = 0.7)
    ax2.set_xlabel(r'每年获取的飞行常客里程数')
    ax2.set_ylabel(r'玩视频游戏所耗时间百分比')
    
    ax3 = fig.add_subplot(223)
    ax3.scatter(datingDataMat[:,2],datingDataMat[:,0],
                15*np.array(datingLabels),15*np.array(datingLabels),
                alpha = 0.7)
    ax3.set_xlabel(r'每周消费的冰淇淋公升数')
    ax3.set_ylabel(r'每年获取的飞行常客里程数')
    
    
    #画图legend,这里不是重点,不用细看,就是说明一下图例
    from matplotlib.legend_handler import HandlerLine2D
    ax4 = fig.add_subplot(224)
    dot1, = ax4.plot([3], marker='o', label='didntLike',color='purple')
    dot2, = ax4.plot([3], marker='o', label='smallDoses',color='c')
    dot3, = ax4.plot([3], marker='o', label='largeDoses',color='yellow')
    ax4.tick_params(axis='both',labelsize=0,length=0,width=0)
    ax4.spines['top'].set_color('none')    #设置颜色
    ax4.spines['bottom'].set_color('none')
    ax4.spines['left'].set_color('none')
    ax4.spines['right'].set_color('none')
    plt.legend(loc='center',handler_map={dot1: HandlerLine2D(numpoints=4),
                            dot2: HandlerLine2D(numpoints=4),
                            dot3: HandlerLine2D(numpoints=4)})
    
    plt.savefig('analyseShow.png')
    plt.show()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#分类器的构建
import operator
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()    #计算距离
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    #python3中用items()替换python2中的iteritems()
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#测试算法
def datingClassTest():
    hoRatio = 0.1      #抽取所有数据的百分之10
    
    #导入数据，并格式化，归一化
    normMat,datingLabels,ranges, minVals = file2matrix('datingTestSet2.txt')
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult =classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
#        print("分类结果: %d, 实际结果: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): 
            errorCount += 1.0
    print("总错误率: %f" % (errorCount/float(numTestVecs)))
    print("错误的样本数: %d"%errorCount)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#使用算法部分
def classifyPerson():
    resultList = ['didntLike','smallDoses','largeDoses']
    
    #获取输入的数据：
    percentTats = float(input("玩视频游戏所耗时间百分比："))
    ffMiles = float(input("每年获取的飞行常客里程数："))
    iceCream = float(input("每周消费的冰淇淋公升数："))
    
    normMat,datingLabels,ranges, minVals = file2matrix('datingTestSet2.txt')
    inArr = np.array([percentTats,ffMiles,iceCream])
    
    #这里用到了范围minVals和ranges
    classifierResult =classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    
    #给出分类结果
    print("你将会对这个人产生感觉是：",resultList[classifierResult-1])


if __name__ == '__main__':
    classifyPerson()