import math
#finds primes up to (and maybe one over)
GO = input('check max ')
count = 1
GO1 = 0
count1 = 0
if GO[0] == 'r':
    GO = GO[1:]
GO = (int)(GO)
while GO >= count:
        count += 1
        GO1 = ((2**count)-2)%count
        if GO1 == 0:
            print('',count)
while GO >= count:
    count1 += 1
    count = 6*count1
    count -= 1
    GO1 = ((2**count)-2)%count
    if GO1 == 0:
        print('',count)
    count += 2
    if not(count > GO):
        GO1 = ((2**count)-2)%count
        if GO1 == 0:
            print('',count)
print(' done')
