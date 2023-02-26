# python3

import sys
import threading
import numpy as np

def compute_height(n, parents, i = [-1], max_height = -1, height = 0):
    # Write this function
    # Your code here
    children = []
    for x in i:
        children.extend(parents.get(x, []))
    if len(children) > 0:
        return compute_height(n, parents, children, max_height+1)
    else:
        return max_height+1

def main():
    # implement input form keyboard and from files
    inputText = ""
    inputType = input()
    if inputType and inputType[0] == "F":
        # let user input file name to use, don't allow file names with letter a
        fileName = input()
        if "a" in fileName:
            return
        inputText = open("test/" + fileName, "r").readlines()
    elif inputType and inputType[0] == "I":
        inputText = [input(), input()]
    else:
        return
    
    # account for github input inprecision

    # input number of elements
    n = int(inputText[0])

    # input values in one variable, separate with space, split these values in an array
    # parents = [int(x) for x in inputText[1].split(" ")]
    parents = {}
    for x, y in zip(range(n), [int(x) for x in inputText[1].split(" ")]):
        if y in parents:
            parents[y].append(x)
        else:
            parents[y] = [x]
    # call the function and output it's result
    # print(len(parents))
    print(compute_height(n, parents))
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread01.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))