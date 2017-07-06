import sys
import math
import random

#My method for simplifying debugging
def error(s):
    print >> sys.stderr, s

# Don't let the machines win. You are humanity's last hope...

width = int(raw_input())  # the number of cells on the X axis
height = int(raw_input())  # the number of cells on the Y axis
grid = []
for i in xrange(height): #Get grid
    line = raw_input()  # width characters, each either 0 or .
    grid.insert(i, line)

nodes= []

for y in xrange(len(grid)): #Sort grid by putting in nodes a list a set of sublists ordered by their y-axis
    count = 0
    row = []
    for i in grid[y]:
        if i=='.':
            row.append(".")
            count+=1
            continue
        x = count
        row.append(str(x)+" "+str(y))
        count+=1
    nodes.append(row)

# Three coordinates: a node, its right neighbor, its bottom neighbor

nodes = [x for x in nodes if x != []] #Remove empty rows

toprint = [] #List where I store my answers

for y, line in enumerate(nodes):#Get lines and y point of each line
    if line!=[]: #Is line empty?
        for x, node in enumerate(line): #Get each node and the x point of the node
            if node != ".":
                string = str(x)+" "+str(y) #Starts the first part of the solution
                xcounter = 0 #Variable for how much I need to go over to find the next node horizontally
                ycounter = 0 #Variable for how much I need to go over to find the next node vertically
                
                while len(nodes[y])-1>x+xcounter and (nodes[y][x+xcounter]=="."or nodes[y][x+xcounter]==node):
                    #If we are not on the last x of the row and (the node where the xcounter points at is a dot or its my current node
                    #Then add 1 to xcounter
                    xcounter+=1
                xcounter = xcounter if nodes[y][x+xcounter]!="." else 0 #If the point the xcounter points at is a dot then set it to 0
                if xcounter==0: #Check if xcounter is 0, if it is...
                    string+=" -1 -1" #Add to our solution that there is no node to the right of the current node in the loop
                else: #If xcounter is not 0...
                    #Add to our solution the node where xcounter points at
                    string+=" "+str(nodes[y][x+xcounter][0])+" "+str(nodes[y][x+xcounter][2])
                
                while len(nodes)-1>y+ycounter and (nodes[y+ycounter][x]=="." or nodes[y+ycounter][x]==node):
                    #If we are not on the last row and (the node where the ycounter points at is a dot or its my current node)
                    #Then add 1 to ycounter
                    ycounter+=1
                ycounter = ycounter if nodes[y+ycounter][x]!="." else 0 #If the point the ycounter points at is a dot then set it to 0
                
                if ycounter==0: #Check if ycounter is 0, if it is...
                    string+=" -1 -1" #Add to our solution there is no node to the bottom of the current node in the loop
                else: #If ycounter is not 0
                    #Add to our solution the node where ycounter points at
                    string+=" "+str(nodes[y+ycounter][x][0])+" "+str(nodes[y+ycounter][x][2])
                toprint.append(string) #Add our solution to my list of answers
for i in toprint: #Loop through every answer
    print i #Print each answer
