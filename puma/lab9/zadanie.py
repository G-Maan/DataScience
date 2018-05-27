from scipy import stats
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

def loadData():
    dt = []
    strData='regions_pl_uro_20'+'_00_2p.csv'
    years=['02','03','04','05','06','07','08','09','10','11','12','13','14','15','16']
    year = []
    for i in years:

        region=[]
        data = []
        strData = 'regions_pl_uro_20'+i + '_00_2p.csv'
        file = open(strData,encoding="utf8")
        for lines in file:
            l=lines.split(',')
            if(l[1] !='region'):
                data = []
                for i in range(len(l)):
                    if( i > 0):
                        data.append(l[i].replace('\n',''))
                region.append(data)
        year.append(region)
    return year

def oneVsMoreThanOne(data):
    one=[]
    more=[]
    oneSum=0
    otherSum=0
    for i in data:
        for j in i:
            oneSum+=float(j[2])
            for x in range(3,len(j)):
                if(j[x] !='-'):
                    otherSum+=float(j[x])
        one.append(oneSum)
        more.append(otherSum)
        otherSum=0
        oneSum=0
    return one,more

def forEachRegion(data):
    one = []
    more = []
    oneInYear=[]
    moreInEar=[]
    oneSum = 0
    otherSum = 0
    for i in data:
        oneInYear = []
        moreInEar = []
        for j in i:
            oneInYear.append( float(j[2]))
            for x in range(3, len(j)):
                if (j[x] != '-'):
                    otherSum+=( float(j[2]))
            moreInEar.append(otherSum)
        one.append(oneInYear)
        more.append(moreInEar)
    return one, more

def plot(list):
    l1=[]
    l2=[]
    for i in list:
        l1.append(i[0])
        l2.append(i[1])
    fig, ax = plt.subplots()
    ind =np.arange(15)
    width = 0.35
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(['02','03','04','05','06','07','08','09','10','11','12','13','14','15','16'])
    rects1 = ax.bar(ind, l1, width, color='r')
    rects2 = ax.bar(ind + width, l2, width, color='y')

    plt.show()





def colerationForEachYear(data):
    x,y=forEachRegion(data)
    corrs=[]
    for i in range(len(x)):
        corrs.append(stats.pearsonr(x[i],y[i]))
    return corrs



plot(colerationForEachYear(loadData()))