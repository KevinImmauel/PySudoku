mainMatrix = [[[[0,8,2],
                [0,0,1],
                [6,0,3]],[[0,0,0],
                          [4,0,6],
                          [0,1,8]],[[1,0,6],
                                    [8,0,2],
                                    [7,0,0]]],[[
            [9,4,0],
            [0,0,6],
            [0,0,0]],[[8,0,7],
                      [5,0,1],
                      [0,4,0]],[[6,0,0],
                                [0,0,0],
                                [2,5,7]]],[[
            [0,1,0],
            [3,6,0],
            [0,0,9]],[[9,0,0],
                      [0,8,0],
                      [3,0,4]],[[0,7,0],
                                [4,2,0],
                                [5,0,0]
        ]
    ]
]

emptyMatrix = []

def printCol(a,b,c,d):
    colList = []
    for i in range(0,3):
        for j in range(0,3):
            colList.append(mainMatrix[i][b][j][d])
    return colList

def printRow(a,b,c,d):
    rowList = []
    for i in range(0,3):
        for j in range(0,3):
            rowList.append(mainMatrix[a][i][c][j])
    return rowList

def printMatrix(a,b,c,d):
    matList = []
    for i in range(3):
        for j in range(3):
            matList.append(mainMatrix[a][b][i][j])
    return matList

def matrixComplete():
    b = True
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if mainMatrix[i][j][k][l] == 0:
                        b = False
                        break
    return b

while matrixComplete() == False:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if mainMatrix[i][j][k][l] == 0:
                        posList = []
                        for m in range(1,10):
                            if m not in printCol(i,j,k,l) and m not in printMatrix(i,j,k,l) and m not in printRow(i,j,k,l):
                                posList.append(m)
                        emptyMatrix.append([[i,j,k,l],posList])
    for i in emptyMatrix:
        if len(i[1]) == 1:
            mainMatrix[i[0][0]][i[0][1]][i[0][2]][i[0][3]] = i[1][0]

print(mainMatrix)

#[[[[4, 8, 2], 
# [7, 5, 1], 
# [6, 9, 3]], [[7, 5, 3], 
#               [4, 9, 6], 
#               [2, 1, 8]], [[1, 9, 6], 
#                           [8, 3, 2], 
#                           [7, 4, 5]]], 
# [[[9, 4, 5], 
# [2, 7, 6], 
# [1, 3, 8]], [[8, 2, 7], 
#               [5, 3, 1], 
#               [6, 4, 9]], [[6, 1, 3], 
#                           [9, 8, 4], 
#                           [2, 5, 7]]], 
# [[[5, 1, 4], 
# [3, 6, 7], 
# [8, 2, 9]], [[9, 6, 2], 
#               [1, 8, 5], 
#               [3, 7, 4]], [[3, 7, 8], 
#                           [4, 2, 9], 
#                           [5, 6, 1]]]]
