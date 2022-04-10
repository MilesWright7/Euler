import sys

#pass euler11.txt into funcion on command line
file = open(sys.argv[1])
matrix = []
for line in file:
    epic = line.split()
    temp = []
    for item in epic:
        temp.append(int(item))
    matrix.append(temp)


#matrix is a 20x20 list of numbers
#im looking for the max value of a * b * c * d in a row up down left right or diagonal
max = 0
#up and down
for i in range(20-3):
    for j in range(20):
        a = matrix[i][j]
        b = matrix[i+1][j]
        c = matrix[i+2][j]
        d = matrix[i+3][j]
        abcd = a*b*c*d
        if abcd > max:
            max = abcd


#right and left
for i in range(20):
    for j in range(20-3):
        a = matrix[i][j]
        b = matrix[i][j+1]
        c = matrix[i][j+2]
        d = matrix[i][j+3]
        abcd = a*b*c*d
        if abcd > max:
            max = abcd

#up left to down right diagonal
for i in range(20-3):
    for j in range(20-3):
        a = matrix[i][j]
        b = matrix[i+1][j+1]
        c = matrix[i+2][j+2]
        d = matrix[i+3][j+3]
        abcd = a*b*c*d
        if abcd > max:
            max = abcd

#down left to up right
for i in range(0, 20-3):
    for j in range(3, 20):
        a = matrix[i][j]
        b = matrix[i+1][j-1]
        c = matrix[i+2][j-2]
        d = matrix[i+3][j-3]
        abcd = a*b*c*d
        if abcd > max:
            max = abcd
#done
print(max)
