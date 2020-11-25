N = 2**8*3**4;
p = "455/33,11/13,1/11,3/7,11/2,1/3"
step = False

import math as m
import os;import platform as pf
clear = lambda: os.system((pf.system() == "Darwin") * 'clear' + (pf.system() != "Darwin") * 'cls')
clear()
from collections import Counter as c
def primeFactors(n):
    pf = []
    while n % 2 == 0:
        pf.append(2)
        n /= 2
    for i in range(3,int(m.sqrt(n))+1,2):
        while n % i == 0:
            pf.append(int(i))
            n /= i
    if n > 2:
        pf.append(int(n))
    return pf
def countDup(n):
    return [[k,v] for k,v in dict(c(n)).items()]
def printVar(n):
    for a in n:
        print("v"+str(a[0])+":\t"+str(a[1]))
pl = [list(map(int, f.split('/'))) for f in p.replace(' ', '').split(',')]
i,s,sN = 0,0,N
if step: print("input:"); printVar(countDup(primeFactors(sN)))
while i < len(pl):
    dn = pl[i][0]/pl[i][1]
    if step:
        input()
        print("step: "+str(s))
        print("index:"+str(i)+"\n")
        s+=1
        printVar(countDup(primeFactors(N)))
    if N * dn % 1 == 0:
        N *= dn
        N = int(N)
        i = -1
    i += 1
print("\nProgram executed with starting variables: "+str(sN))
printVar(countDup(primeFactors(sN)))
print("Program terminated with exiting variables: "+str(N))
printVar(countDup(primeFactors(N)))
