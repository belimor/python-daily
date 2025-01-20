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
            print("= = = =")
            print(mg[i][j],i,j)
            if i == 0 and j == 0:
                if mg[i][j] > mg[i][j+1] and mg[i][j] > mg[i+1][j+1] and mg[i][j] > mg[i+1][j]:
                    count += 1
            if i == (len(mg)-1) and j == (len(mg[i])-1):
                if mg[i][j] > mg[i][j-1] and mg[i][j] > mg[i-1][j-1] and mg[i][j] > mg[i-1][j]:
                    count += 1
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
                    if y != 0 or x != 0:
                        print("x:",x,"y:",y)
                        if mg[i][j] > mg[i+x][i+y]:
                            bcount = bcount and True
                        else:
                            bcount = bcount and False
            print(bcount)

    print(mg)
    return count

if __name__ == '__main__':

    grid = [[9,2,3,4],[1,2,3,4],[3,4,5,6]]

    print(grid)
    result = numCells(grid)
    print(result)

