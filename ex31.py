print(""" You enter a dark room with two doors.
So you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a gfaint bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Takea the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear =="2":
        print("The eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door =="2":
    print("Tou stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insaitly = input("> ")

    if insaitly == "1" or insaitly =="2":
        print("Your body survives powered ba a mind of jello.")
        print("Good job!")
    else:
        print("The insainty rots your eyes into a pool of muck.")

else:
    print("You stumble around and fall on a knife and die. Good job!")
