
import heapq

def main():
    
    t = int(input())
    for case in range(1, t + 1):
        n = int(input())
        a = readIntArr()
        
        # Solve by storing the maximum elements contributing to H-index.
        # Note that with each additional element, cnts increases and the
        # criterion for the smallest element in the stored elements is 
        # stricter (is increased). The stored maximum elements
        # are retained, or some of them are removed. There is never a need
        # to add back previous elements that were removed.
        
        h = []
        ans = []
        cnts = 0
        for x in a:
            cnts += 1
            heapq.heappush(h, x)
            while h and h[0] < cnts:
                heapq.heappop(h)
                cnts -= 1
            ans.append(cnts)
        print('Case #{}: {}'.format(case, ' '.join([str(x) for x in ans])))
    
    return



import sys
input=sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
# input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.
 
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