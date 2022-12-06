import random
#the card game WAR
Tlist = []
Alist = []
Blist = []
Nlist = [2,3,4,5,6,7,8,9,10,11,12,13,14]
for x in Nlist:
    Tlist.append(x)
for x in Nlist:
    Tlist.append(x)
for x in Nlist:
    Tlist.append(x)
for x in Nlist:
    Tlist.append(x)
c = 23
while c != 0:
    current = (int)(random.randint(0,len(Tlist)-1))
    Alist.append(Tlist[current])
    c -= 1
c = 23
while c != 0:
    current = (int)(random.randint(0,len(Tlist)-1))
    Blist.append(Tlist[current])
    c -= 1
go = input('hit any button to start ')
while len(Alist) != 0 and len(Blist) != 0:
    go = input('put card down p1 ')
    current = random.randint(0,len(Alist)-1)
    A = Alist[current]
    if A == 11:
        print('Jack')
    elif A == 12:
        print('Queen')
    elif A == 13:
        print('King')
    elif A == 14:
        print('Ace')
    else:
        print(A)
    go = input('put card down p2 ')
    current1 = random.randint(0,len(Blist)-1)
    B = Blist[current1]
    if B == 11:
        print('Jack')
    elif B == 12:
        print('Queen')
    elif B == 13:
        print('King')
    elif B == 14:
        print('Ace')
    else:
        print(B)
    if A > B:
        Alist.append(B)
        Blist.remove(B)
        go = print('player 1 wins,',len(Alist),'remaining for player 1,',len(Blist),'remiaining for player 2')
        go = input('press any button to continue')
    elif A == B:
        if len(Alist) <= 2 or len(Blist) <= 2:
            break
        Blist.remove(B)
        Alist.remove(A)
        current = random.randint(0,len(Alist)-1)
        C = Alist[current]
        Alist.remove(C)
        current = random.randint(0,len(Alist)-1)
        c = Alist[current]
        Alist.remove(c)
        current = random.randint(0,len(Blist)-1)
        D = Blist[current]
        Blist.remove(D)
        current = random.randint(0,len(Blist)-1)
        d = Blist[current]
        Blist.remove(d)
        if C > D:
            Alist.append(A)
            Alist.append(C)
            Alist.append(c)
            Alist.append(B)
            Alist.append(D)
            Alist.append(d)
        elif D > C:
            Blist.append(A)
            Blist.append(C)
            Blist.append(c)
            Blist.append(B)
            Blist.append(D)
            Blist.append(d)
    else:
        Blist.append(A)
        Alist.remove(A)
        print('player 2 wins,',len(Blist),'remaining for player 2,',len(Alist),'remiaining for player 1')
        go = input('press any button to continue')
if len(Alist) > len(Blist):
    print('player 1 wins!')
if len(Blist) > len(Alist):
    print('player 2 wins!')
