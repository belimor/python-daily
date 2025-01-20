#!/bin/python3

#
# Complete the 'numCells' function below.
#

def numCells(grid):
    mg = grid
    count = 0
    for i in range(len(mg)):
        for j in range(len(mg[i])):
            if i == 0: a = 0 
            else: a = -1
            if j == 0: b = 0
            else: b = -1
            if i == (len(mg)-1): c = 0
            else: c = 1
            if j == (len(mg[i])-1): d = 0
            else: d = 1
            bcount = True
            for x in range(a,c+1):
                for y in range(b,d+1):
                    if y == 0 and x == 0:
                        pass
                    else:
                        if mg[i][j] > mg[i+x][j+y]:
                            bcount = bcount and True
                        else:
                            bcount = bcount and False
            if bcount: 
                count += 1
                print("YES:",mg[i][j],i+1,j+1)
    return count

if __name__ == '__main__':

    grid = [[9,2,3,4],[1,2,8,4],[3,4,5,6]]

    for i in range(len(grid)):
        print(grid[i])
    result = numCells(grid)
    print(result)

