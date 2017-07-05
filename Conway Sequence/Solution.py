#This is the third solution I have created for this puzzle.

import sys
import math

#My method to make debugging easier
def error(s):
    print >> sys.stderr, s

def solution_of_line(line):
    count = 0
    number_on = -1
    solution = ""
    for i in xrange(len(line)):
        if number_on == -1 or number_on != line[i]:
            number_on = line[i]
            count = 0;
            
        if number_on == line[i]:
            count+=1
            if (i==len(line)-1):
                base_string = solution+str(count)+" "+str(number_on)
                solution = base_string
            elif line[i+1] != number_on:
                base_string = solution+str(count)+" "+str(number_on)
                solution = base_string
                count = 0
        else:
            base_string = solution+str(count)+" "+str(number_on)
            solution = base_string if solution=="" or solution==None else " "+base_string
            count = 0
            number_on = line[i]
            
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(raw_input())
l = int(raw_input())
count = 0
current_solution = str(r)

while count!=l-1:
    string_on_line = current_solution
    splitted = map(int, string_on_line.split())
    sol = solution_of_line(splitted)
    count+=1

print current_solution
