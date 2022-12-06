#generates digits of pi
print("Hit enter to start generating pi")
pi = 3
n = (int)(0)
go = input('')
while go == '' or go != 10000:
    n += 1
    pi += 4/((2*n)*(2*n+1)*(2*n+2))
    print(pi)
    n += 1 
    pi -= 4/((2*n)*(2*n+1)*(2*n+2))
    print(pi)
    if go == '':
        go = (int)(0)
    go += 2
    if go == 9998:
        go = input("Hit enter to continue")
