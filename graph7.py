import re
import os
import numpy as np
import collections
import matplotlib.pyplot as plt
#intialize global variables 
fig=plt.figure()
ax=fig.add_subplot(111)1
normalizer=1
findMatches=[]
uidData=[]
seenData=set()
countHashmap={}

#uses matplotlib to plot data in a histogram
def visualize(dateData):
    N=len(ordereduidcount)
    ind=np.arange(N)
    width =1
    # the histogram of the data
    rects = ax.bar(ind,ordereduidcount.values(),width,color="red")
    ax.set_xlim(0,len(ind)+width)
    ax.set_ylim(0,2000)
    ax.set_ylabel("Frequency(Requests)")
    ax.set_xlabel("Segments's of MID:wasu_1289359")
    ax.set_title("Segment Histogram for MID:wasu_1289359")
    plt.show()
def getData(line):
    findSegment=re.findall(r'(?<=wasu_1991939)(.*)(?=.*.ts)',line)
    if len(findSegment)!=0:
        findMatches.append(findSegment)
    #find all movie segments
    for match in findMatches:
        start = match[0].find("video/")+26
        uidData.append(match[0][start:])
    print len(uidData)
    #store all movie segments in a hashmap
    for uid in uidData:
        if uid not in seenData:
            nomalized=int((uidData.count(uid))/normalizer)
            countHashmap.update({uid:nomalized})
            seenData.add(uid)
    #sort the hash map by ascending movie segments, thus also ordering the count values
    ordereduidcount=collections.OrderedDict(sorted(countHashmap.items()))
    
    print len(ordereduidcount)
    print len(countHashmap)
    print len(ordereduidcount.values())


    
###MAIN FUNCTION###
#traverse the directory to go through all .log files
for root, dirs, files in os.walk("C:/Users/R3421NOP-131SN2/Documents/4thyearproject/access_log"):
    for file in files:
        with open(os.path.join(root, file)) as infile:
                  for line in infile:
                          getData(line)
visualize()
