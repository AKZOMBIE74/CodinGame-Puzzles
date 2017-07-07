import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())
c = int(raw_input())
ogCost = c
t=0
sols = []
myBs = []
for i in xrange(n):
    b = int(raw_input())
    myBs.append(b)
myBs.sort(key=lambda x: x)
myBSum = sum(myBs)

for i,b in enumerate(myBs):
    howMuch = c/(len(myBs)-i)
    if i==len(myBs)-1 and b>=c:
        t+=c
        sols.append(c)
        c=0
    else:
        if b<howMuch:
            sols.append(b)
            c-=b
            t+=b
        else:
            sols.append(howMuch)
            c-=(howMuch)
            t+=(howMuch)
if t<ogCost: print "IMPOSSIBLE"
else:
    for i in sols:
        print i
