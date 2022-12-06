import random
#rolls 2 dice and displays the faces
Play_Again = "yes"
while Play_Again == "yes" or Play_Again == "y" or Play_Again == "":
    Rand = random.randint(1,6)
    Rand1 = random.randint(1,6)
    if Rand == 1:
        print(" ____________\n|            |\n|            |\n|     *      |\n|            |\n|____________|")
    if Rand == 2:
        print(" ____________\n|            |\n|            |\n|   *   *    |\n|            |\n|____________|")
    if Rand == 3:
        print(" ____________\n|            |\n|       *    |\n|     *      |\n|   *        |\n|____________|")
    if Rand == 4:
        print(" ____________\n|            |\n|   *   *    |\n|            |\n|   *   *    |\n|____________|")
    if Rand == 5:
        print(" ____________\n|            |\n|   *   *    |\n|     *      |\n|   *   *    |\n|____________|")
    if Rand == 6:
        print(" ____________\n|            |\n|   *   *    |\n|   *   *    |\n|   *   *    |\n|____________|")
    if Rand1 == 1:
        print(" ____________\n|            |\n|            |\n|     *      |\n|            |\n|____________|")
    if Rand1 == 2:
        print(" ____________\n|            |\n|            |\n|   *   *    |\n|            |\n|____________|")
    if Rand1 == 3:
        print(" ____________\n|            |\n|       *    |\n|     *      |\n|   *        |\n|____________|")
    if Rand1 == 4:
        print(" ____________\n|            |\n|   *   *    |\n|            |\n|   *   *    |\n|____________|")
    if Rand1 == 5:
        print(" ____________\n|            |\n|   *   *    |\n|     *      |\n|   *   *    |\n|____________|")
    if Rand1 == 6:
        print(" ____________\n|            |\n|   *   *    |\n|   *   *    |\n|   *   *    |\n|____________|")
    Play_Again = input("Roll Again? ")
    Play_Again = Play_Again.lower()
print("Have a nice day")
