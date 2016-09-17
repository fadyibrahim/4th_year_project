#import libraries needed
import re
import os
import numpy as np
import matplotlib.pyplot as plt

#uses matplotlib to plot data in a histogram
def visualize(dateData):
# the histogram of the data
    n, bins, patches = plt.hist(dateData,31, normed=1, facecolor='r', alpha=1)
    plt.xlabel('Day of Feburary')
    plt.ylabel('Frequency(Requests)')
    plt.title('Histogram of MID:2719292')
#ranges in both the x and y axis
    plt.axis([1,21, 0,13000])
    plt.grid(True)
    plt.show()
    return

#Extracts data from files
#Param - rootDir, allData 
def getData(nextline):
    #regex to extract all the dates that are proceeded by the video id  
    findMatches=re.findall(r'(\d./\w../....)(?=.*2719292)',nextline)
    #For each match extract 
    for match in findMatches:
        dayData.append(int(match[:2]))
    return 


###MAIN FUNCTION###
dayData=[]
#traverse the directory to go through all .log files
for root, dirs, files in os.walk("C:/Users/R3421NOP-131SN2/Documents/4thyearproject/month_access_logs/CC/"):
    for file in files:
        with open(os.path.join(root, file)) as infile:
            for line in infile:
                getData(line)
visualize(dayData)


