from sys import argv
import math
import os

import numpy as np

#fileOP  = open("a_example.txt", "r")
#fileToArr = fileOP.readlines()
def readFile(file):
    rfile = open(file, "r")
    fileToArr = rfile.readlines()
    pArr = []
    for dell in fileToArr:
        pArr.append(dell.strip('\n'))
    rfile.close()
    return pArr

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

def processArrFile(arr):
    treatedArr = []
    intTreat = []
    for i in arr:
        treatedArr.append(i.split(" "))
    return treatedArr

def getLibsBySignup(trArr):
    libsNum = int(trArr[0][1])
    valLibs = []
    for i in range(2,len(trArr),2):
        valLibs.append(int(trArr[i][1]))
    return  valLibs

def getLibsByScores(trArr):
    libsNum = int(trArr[0][1])
    valLibs = []
    for i in range(3 ,len(trArr),2):
        for j in range(len(trArr[i])):
            valLibs.append(trArr[1][j])
    vall = [valLibs[0:5], valLibs[5:8]]
    return set(valLibs)

def getLibsByScanner(trArr):
    libsNum = int(trArr[0][2])
    valLibs = []
    for i in range(2,len(trArr),2):
        valLibs.append(int(trArr[i][-1]))
    return  valLibs

def delRepeatedBooks(trArr):
    mainArr = []
    for i in range(3,len(trArr),2):
        for j in trArr[i]:
            mainArr.append(int(j))
    return  list(set(mainArr))

def outPut():
    file = open("newFile.txr","w+")
    file.write(str(len(getLibsBySignup(processArrFile(readFile("a_example.txt"))))))
    file.write(str(len(getLibsBySignup(processArrFile(readFile("a_example.txt"))))))


#print(readFile("a_example.txt"))
print(delRepeatedBooks(processArrFile(readFile("a_example.txt"))))
#print(getLibsByScores(processArrFile(readFile("a_example.txt"))))
print(getLibsBySignup(processArrFile(readFile("a_example.txt"))))
outPut()