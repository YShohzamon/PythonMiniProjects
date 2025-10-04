import random

user_wins = 0
computer_wins = 0
conbinations = ["rock", "paper", "scissors"]
print("Let's play Rock/Paper/Scissors until 3!")
while True:
    user_input = input("Please type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        quit()

    if user_input not in conbinations:
        print("Invalid input. Please try again.")
        continue

    computer_choice = random.randint(0,2)
    if user_input == "rock":
        if computer_choice == 0:
            print("user: 👊" , "compyuter: 👊")
            print("Draw!")
            print(f"user: {user_wins}, computer: {computer_wins}")
        elif computer_choice == 1:
            print("user: 👊", "compyuter: ✋")
            print("Compyuter wins!")
            computer_wins += 1
            print(f"user: {user_wins}, computer: {computer_wins}")

        else:
            print("user: 👊", "compyuter: ✌️")
            print("User wins!")
            user_wins += 1
            print(f"user: {user_wins}, computer: {computer_wins}")

    elif user_input == "paper":
        if computer_choice == 0:
            print("user: ✋" , "compyuter: 👊")
            print("User wins!")
            user_wins += 1
            print(f"user: {user_wins}, computer: {computer_wins}")

        elif computer_choice == 1:
            print("user: ✋", "compyuter: ✋")
            print("Draw!")
            print(f"user: {user_wins}, computer: {computer_wins}")

        else:
            print("user: ✋", "compyuter: ✌️")
            print("Compyuter wins!")
            computer_wins += 1
            print(f"user: {user_wins}, computer: {computer_wins}")

    else:
        if computer_choice == 0:
            print("user: ✌️" , "compyuter: 👊")
            print("Compyuter wins!")
            computer_wins += 1
            print(f"user: {user_wins}, computer: {computer_wins}")

        elif computer_choice == 1:
            print("user: ✌️", "compyuter: ✋")
            print("User wins!")
            user_wins += 1
            print(f"user: {user_wins}, computer: {computer_wins}")

        else:
            print("user: ✌️", "compyuter: ✌️")
            print("Draw!")
            print(f"user: {user_wins}, computer: {computer_wins}")


    if computer_wins == 3:
        print("Compyuter wins game!!!")
        break
    if user_wins == 3:
        print("User wins game!!!")
        break


print("Goodbye. Thank you for playing!")
