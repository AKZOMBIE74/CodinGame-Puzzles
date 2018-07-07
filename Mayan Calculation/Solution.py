import sys
import math

def error(s):
    print >> sys.stderr, str(s)
def splitRow(row):
    sol = ""
    for i in xrange(h):
        sol+=row[i*l:i*l+l]
        if i!=h-1:
            sol+="\n"
    return sol
def calculateNumber(mayan, height):
    splitted = [values.index(mayan[i*l*h:(i*l*h)+(l*h)])for i in xrange(height/h)]
    number = 0
    for x,num in enumerate(splitted[::-1]):
        number+=num*pow(20,x)
    return number

#returns [ [number,exponent], [number,exponent], ...]
def getMayanRep(numeric, ans):
    answers=ans
    if numeric > 19:
        number = numeric/20
        maxExponent = int(math.log(numeric, 20))
        if number > 19:
            number = 1
        if len(answers)>0 and maxExponent==answers[-1][1]:
            answers[-1][0]+=1
        else:
            if len(answers) > 0 and (answers[-1][1]-maxExponent)>1:
                add0 = answers[-1][1]-maxExponent
                for i in xrange(add0-1):
                    answers.append([0,0]) #Add 0 as placeholder
            answers.append([number,maxExponent])
        numeric-=(pow(20,maxExponent)*number)
    else:
        answers.append([numeric,0])
        return answers
    return getMayanRep(numeric, answers)

values = ["" for i in xrange(20)]
l, h = [int(i) for i in raw_input().split()]

for i in xrange(h):
    numeral = raw_input()
    for num in xrange(20):
        values[num] += numeral[num*l:num*l+l]

n1=""
n2=""
s1 = int(raw_input())
for i in xrange(s1):
    num_1line = raw_input()
    n1+=num_1line
s2 = int(raw_input())
for i in xrange(s2):
    num_2line = raw_input()
    n2+=num_2line
operation = raw_input()
n1 = calculateNumber(n1, s1)
n2 = calculateNumber(n2, s2)
numericAnswer=eval(str(n1) + operation + str(n2))
mayanRep = getMayanRep(numericAnswer,[])

error("Width: " + str(l) + "    Height: " + str(h))
error("Number 1: " + str(n1))
error("Number 2: " + str(n2))
error("Operation: " + operation)
error("Numeric Answer: " + str(numericAnswer))
error("Mayan Rep: " + str(mayanRep))
error("=========================================")

for i in mayanRep:
    answer = values[i[0]]
    print splitRow(answer)
