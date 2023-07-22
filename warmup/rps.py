#aditya durbha
# 7/22/2023
# simple rock paper scissor game
import random

def main():
    print("hello world")
    select = input("rock paper or scissors? ")
    comp_input = random.randint(0,2)
    print("You selected: ", select)
    print("Computer selected: ", comp_input)
    if select == "rock":
        if comp_input == 0:
            print("tie!")
        elif comp_input == 1:
            print("you lost...")
        elif comp_input == 2:
            print("You won!!!")
    elif select == "paper":
        if comp_input == 1:
            print("tie!")
        elif comp_input == 2:
            print("you lost...")
        elif comp_input == 0:
            print("You won!!!")
    elif select == "scissors":
        if comp_input == 2:
            print("tie!")
        elif comp_input == 0:
            print("you lost...")
        elif comp_input == 1:
            print("You won!!!")
    else:
        print("Your answer was not an option.")
        
if __name__ == "__main__":
    main()