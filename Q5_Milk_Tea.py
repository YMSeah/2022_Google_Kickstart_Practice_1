
def getComplaintCounts(order, friends, p):
    cnt = 0
    for f in friends:
        for i in range(p):
            if order[i] != f[i]:
                cnt += 1
    return cnt

import heapq

def main():
    
    t = int(input())
    for case in range(1, t + 1):
        n, m, p = readIntArr()
        friends = []
        exclude = set()
        for _ in range(n):
            friends.append(input())
        for _ in range(m):
            exclude.add(input())
        
        oneCnts = [0] * p
        zeroCnts = [0] * p
        for f in friends:
            for i in range(p):
                if f[i] == '0': zeroCnts[i] += 1
                else: oneCnts[i] += 1
        bestArr = []
        for i in range(p):
            if oneCnts[i] > zeroCnts[i]:
                bestArr.append('1')
            else:
                bestArr.append('0')
        bestString = ''.join(bestArr)
        
        # Changing each order individually incurs an additional cost.
        # Re-imagine the problem as taking a subset of costs in
        # increasing total cost of subset.
        # Since the minCost for subset of size 2 must come from minCost of
        # subset of size 1, I can bfs from smallest cost by taking 1 more
        # item each time (i.e. flip 1 bit). Use a heap/priority queue like
        # Dijkstra.
        
        h = [(getComplaintCounts(bestString, friends, p), bestString)]
        vi = {bestString}
        while True:
            cnts, s = heapq.heappop(h)
            if s not in exclude:
                print('Case #{}: {}'.format(case, cnts))
                break
            for i in range(p):
                left = s[:i]
                right = s[i + 1:]
                if s[i] == '0': mid = '1'
                else: mid = '0'
                s2 = left + mid + right
                if s2 not in vi:
                    vi.add(s2)
                    heapq.heappush(h, (getComplaintCounts(s2, friends, p), s2))
    
    return



import sys
# input=sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.
 
def oneLineArrayPrint(arr):
    print(' '.join([str(x) for x in arr]))
def multiLineArrayPrint(arr):
    print('\n'.join([str(x) for x in arr]))
def multiLineArrayOfArraysPrint(arr):
    print('\n'.join([' '.join([str(x) for x in y]) for y in arr]))
 
def readIntArr():
    return [int(x) for x in input().split()]
# def readFloatArr():
#     return [float(x) for x in input().split()]
 
def makeArr(defaultValFactory,dimensionArr): # eg. makeArr(lambda:0,[n,m])
    dv=defaultValFactory;da=dimensionArr
    if len(da)==1:return [dv() for _ in range(da[0])]
    else:return [makeArr(dv,da[1:]) for _ in range(da[0])]
 
def queryInteractive(a, b, c):
    print('? {} {} {}'.format(a, b, c))
    sys.stdout.flush()
    return int(input())
 
def answerInteractive(ansArr):
    print('! {}'.format(' '.join([str(x) for x in ansArr])))
    sys.stdout.flush()
 
inf=float('inf')
# MOD=10**9+7
# MOD=998244353
 
from math import gcd,floor,ceil
import math
# from math import floor,ceil # for Python2
 
for _abc in range(1):
    main()