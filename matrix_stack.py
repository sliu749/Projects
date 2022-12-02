# Your Matrix Stack Library

# you should modify the provided empty routines to complete the assignment

# Songxuan Liu
# sliu749@gatech.edu


stack = []

def gtInitialize():
    identityMatrix = [[1,0,0,0],
                      [0,1,0,0],
                      [0,0,1,0],
                      [0,0,0,1]]
    stack.append(identityMatrix)

def gtPopMatrix():
    if (len(stack) <= 2):
        print "cannot pop the matrix stack"
    stack.pop()

def gtPushMatrix():
    stack.append(stack[-1])

def gtScale(x,y,z):
    s = [[x,0,0,0],
         [0,y,0,0],
         [0,0,z,0],
         [0,0,0,1]]
    stack[-1] = gtMultiplication(stack[-1], s)

def gtTranslate(x,y,z):
    t = [[1,0,0,x],
         [0,1,0,y],
         [0,0,1,z],
         [0,0,0,1]]
    stack[-1] = gtMultiplication(stack[-1], t)

def gtRotateX(theta):
    theta = theta * PI / 180
    r = [[1,0,0,0],
         [0,cos(theta),-sin(theta),0],
         [0,sin(theta),cos(theta),0],
         [0,0,0,1]]
    stack[-1] = gtMultiplication(stack[-1], r)

def gtRotateY(theta):
    theta = theta * PI / 180
    r = [[cos(theta),0,sin(theta),0],
         [0,1,0,0],
         [-sin(theta),0,cos(theta),0],
         [0,0,0,1]]
    stack[-1] = gtMultiplication(stack[-1], r)

def gtRotateZ(theta):
    theta = theta * PI / 180
    r = [[cos(theta),-sin(theta),0,0],
         [sin(theta),cos(theta),0,0],
         [0,0,1,0],
         [0,0,0,1]]
    stack[-1] = gtMultiplication(stack[-1], r)

def print_ctm():
    for i in stack[-1]:
        print i
    print "\n"
def gtMultiplication(matrix1, matrix2):
    empty = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                empty[i][j] += matrix1[i][k] * matrix2[k][j]
    return empty
