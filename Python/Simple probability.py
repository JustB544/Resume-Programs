import random
#rolls the dice d amount of times, counts how many times each number showed up
Dice = [0, 0, 0, 0, 0, 0]
a = 0
b = 0
c = 0
d = 10000
e = 0
for x in range(d):
    random.seed(a=str(random.random()), version=2)
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    if (a%2 + b%2 + c%2 > 1):
        e += 3
    e += (a+b+c)%3
    Dice[e] += 1
    e = 0

for x in Dice:
    e += 1
    print("Number of " + str(e) + "'s: " + str(Dice[e-1]))
