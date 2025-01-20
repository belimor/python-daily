#!/bin/python3


#
# Complete the 'numCells' function below.
#
#

def numCells(grid):
    mg = grid
    count = 0
    for i in range(len(mg)):
        for j in range(len(mg[i])):
            print(mg[i][j])
            if i == 0 and j == 0:
                if mg[i][j] > mg[i][j+1] and mg[i][j] > mg[i+1][j+1] and mg[i][j] > mg[i+1][j]:
                    count += 1
            if i == (len(mg)-1) and j == (len(mg[i])-1):
                if mg[i][j] > mg[i][j-1] and mg[i][j] > mg[i-1][j-1] and mg[i][j] > mg[i-1][j]:
                    count += 1
    print(mg)
    return count

if __name__ == '__main__':

    grid = [[9,2,3,4],[1,2,3,4],[3,4,5,6]]

    print(grid)
    result = numCells(grid)
    print(result)

