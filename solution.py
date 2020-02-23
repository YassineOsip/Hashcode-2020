import sys
import math
 
class Lib(): 
    totB = 0
    initDelay = 1
    blimit = 2
    books = 3
    score = 4
    priority = 5
    lId = 6

sys.stdin = open("./f_libraries_of_the_world.txt", "r")
sys.stdout = open("./Foutput.txt", 'w')
b,l,d = map(int, input().split())
linfo = list()
bDone = [False for i in range(b)]
scores = list(map(int, input().split()))

for i in range(l):
    linfo.append(list(map(int, input().split())))
    linfo[i].append(list(map(int, input().split())))
    linfo[i][Lib.books].sort(key = lambda bok: scores[bok], reverse=True)
    linfo[i].append(sum(list(map(lambda a: scores[a], linfo[i][Lib.books]))))
    if linfo[i][Lib.initDelay] < d:
        linfo[i].append(linfo[i][Lib.score]*linfo[i][Lib.blimit]/math.pow(linfo[i][Lib.initDelay], 2))
    else:
        linfo[i].append(0)
    linfo[i].append(i)
    
linfo.sort(key=lambda lib:lib[Lib.priority], reverse=True)

for i in range(l):
    for j in range(len(linfo[i][Lib.books])):
        if bDone[ linfo[i][Lib.books][j] ]:
            linfo[i][Lib.books][j] = -1
            continue
        bDone[ linfo[i][Lib.books][j] ] = True
    linfo[i][Lib.books] = list(filter(lambda bk: not(bk == -1), linfo[i][Lib.books]))
    linfo[i][Lib.score] = sum(list(map(lambda a: scores[a], linfo[i][Lib.books])))
    linfo[i][Lib.priority] = linfo[i][Lib.score]*linfo[i][Lib.blimit]/math.pow(linfo[i][Lib.initDelay], 2)

linfo.sort(key=lambda lib:lib[Lib.priority], reverse=True)
bDone = [False for i in range(b)]
totDays = 0
finalLibs = list()

for i in range(l):
    totDays += linfo[i][Lib.initDelay]
    if totDays >= d:
        break
    finalLibs.append(list())
    finalLibs[i].append(linfo[i][Lib.lId])
    booksLimit = (d - totDays)*linfo[i][Lib.blimit]
    finalLibs[i].append(list())
    bCount = 0
    for j in range(len(linfo[i][Lib.books])):
        if bDone[ linfo[i][Lib.books][j] ]:
            continue
        bDone[ linfo[i][Lib.books][j] ] = True
        bCount += 1
        finalLibs[i][1].append(linfo[i][Lib.books][j])
        if bCount == booksLimit:
            break
    if bCount == 0:
        totDays -= linfo[i][Lib.initDelay]   
    

finalLibs = list(filter(lambda lib: len(lib[1]), finalLibs))

print(len(finalLibs))
for lib in finalLibs:
    print(lib[0], len(lib[1]))
    print(*lib[1])
sys.stdout.flush()