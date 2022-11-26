from weightedAStar import *
from priorityQueue import *

## Read Input File
def readInputFile(filename):
    w = ''
    initial_state = []
    goal_state = []
    input_file = open(filename)

    line_count = 0
    # read and handle each line of input
    for line in input_file:
        # if line ISN'T empty, handle
        if line != "\n":
            # determines where to store lines
            if line_count == 0: # w
                w = float(line.strip())
            elif line_count >= 2 and line_count <= 5: # initial
                initial_state.append(line.split())
            elif line_count >= 7 and line_count <= 10: # goal
                goal_state.append(line.split())
        line_count += 1
    input_file.close() # must close file!
    return w, initial_state, goal_state

## Create Output File
def createOutputFile(w, initial_state, goal_state, d, N, A, f, file_num):
    filename = "Output" + str(file_num) + ".txt"
    output_file = open(filename, 'w')

    # format and paste input info
    for row in initial_state:
        output_file.write(' '.join(row))
        output_file.write("\n")

    output_file.write("\n")
    
    for row in goal_state:
        output_file.write(' '.join(row))
        output_file.write("\n")

    output_file.write("\n")
    output_file.write("w: " + w + "\n")
    output_file.write("d: " + d + "\n")
    output_file.write("N: " + N + "\n")
    
    output_file.write("A: ")
    for elem in A:
        output_file.write(str(elem) + " ")
    
    output_file.write("\n")
    output_file.write("f: ")
    for elem in f:
        output_file.write(str(elem) + " ")
        
    output_file.close() # must close file!

## MAIN FUNC
def main():
    # variables
    A = []    # moves made
    d = 0     # depth of the shallowest goal node (# of moves made)
    N = 1     # total nodes generated (including root node)
    f = []    # f(n) values of nodes along solution path from root to goal

    filename = input("Enter name of file: ")
    w, initial_state, goal_state = readInputFile(filename)

    A, d, N, f = weightedAStarSearch(w, initial_state, goal_state)

    file_num = filename[5] # number from input filename
    createOutputFile(str(w), initial_state, goal_state, str(d), str(N), A, f, file_num)

## Call main()
main()    
    
