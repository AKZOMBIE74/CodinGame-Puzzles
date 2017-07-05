#This is the third solution I have created for this puzzle.

import sys
import math

#My method to make debugging easier
def error(s):
    print >> sys.stderr, s

#Returns solution of a given line of the conway sequence
def solution_of_line(line):
    count = 0 #Default value
    number_on = -1 #Default value
    solution = "" #Solution to each line
    for i in xrange(len(line)): #Loop through each integer of line
        if number_on == -1 or number_on != line[i]: #Are we on the current number that is going through the loop?, if not...
            number_on = line[i] #Put us on that number
            count = 0 #Set count to 0
            
        if number_on == line[i]: #Is the number we are on equal to the number the loop is on?
            count+=1 #If so add 1 to count.
            if (i==len(line)-1): #Is the loop on the last number on the line?
                base_string = solution+str(count)+" "+str(number_on) #Make base solution
                solution = base_string #Set solution to baseString
            elif line[i+1] != number_on: #Is the next integer on the line the same as the current number? If not...
                base_string = solution+str(count)+" "+str(number_on) #Make base solution
                solution = base_string+" " #Add space to baseString and set solution to that
                count = 0 #Set count to 0
        else:
            base_string = solution+str(count)+" "+str(number_on) #Make base solution
            solution = base_string if solution=="" else " "+base_string #If solution is not empty, add space, else don't.
            count = 0 #Set count to 0
            number_on = line[i] #We are on a new number
    return solution #Give us back the solution.

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(raw_input())
l = int(raw_input())
count = 0 #Default Value
current_solution = str(r) #This is always the first line of the sequence.

while count!=l-1: #Are we on the line that the puzzle wants us to print? If not...
    string_on_line = current_solution #Get our input
    splitted = map(int, string_on_line.split()) #Split the integer from the input
    sol = solution_of_line(splitted) #Get the solution
    current_solution = sol #Change our current solution to the one given
    count+=1 #Get ready for a new line.

print current_solution #Print solution.
