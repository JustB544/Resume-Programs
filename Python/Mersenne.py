import math
#tests if a number is a mersenne prime
#if you type p before a number it tests 2^p - 1
p = input('What prime would you like to test?\n')
r = (int)(0)
i = (int)(4)
p1 = 0
if p[0] == 'p':
    p = p[1:]
    p1 = 1
if p[0] == 'p':
    p = (int)(p[1:])
    while r != p-2:
        i = ((i**2)-2)%((2**p)-1)
        r += 1
    if i == 0 or p == 2:
        print('2 raised to the power of',p,'minus 1 is a mersenne prime')
        if p1 == 1:
            print((2**p)-1)
    else:
        print('2 raised to the power of',p,'minus 1 is not a mersenne prime')
else:
    p = (int)(p)
    while r != (round(math.log2(p+1)))-2:
        i = ((i**2)-2)%p
        r += 1
    if i == 0  or p == 3:
        print(p,'is a mersenne prime')
    else:
        print(p,'is not a mersenne prime')

