import random
#program that gives you a randomized list of numbers from min to max
rnM = (int)(input("Max Number? "))
rnm = (int)(input("Minimimum Number? "))
test = 0
again = rnM
List = [rnM]
while test < rnM-1:
    List.append(rnM-test-1)
    test += 1
while again != 0:
    Rand = random.randint(1,len(List))
    print("The Next Number is",List[Rand])
    List.remove(List[Rand])
    again -= 1
    print(len(List),"remaining")
    test = input("Next number (hit enter)")
