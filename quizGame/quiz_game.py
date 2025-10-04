print("Welcome to my Quiz Game!")

playing = input("Would you like to play? (y/n) ")

if playing != "y":
    quit()

count_t = 0
answer = input("What daes CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    count_t += 1
else:
    print("Incorrect!")

answer = input("What daes GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    count_t += 1
else:
    print("Incorrect!")

answer = input("What daes RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    count_t += 1
else:
    print("Incorrect!")

print("you got " + str(count_t))


