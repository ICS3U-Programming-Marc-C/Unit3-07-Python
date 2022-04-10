#!/usr/bin/env python3
# Created by Marc Coffi
# Created in April 2022
# This is a game made to find out if you can date the grandchild


def main():
    while True:
        # Ask user for input
        user_input = input("Are you rich? (y/n):")

        user_input2 = input("Are you good looking? (y/n):")

        if user_input == "y" and user_input2 == "y":
            dating = True
        elif user_input == "n" and user_input2 == "y":
            dating = True
        elif user_input == "y" and user_input2 == "n":
            dating = True
        elif user_input == "n" and user_input2 == "n":
            dating = False
        else:
            dating = "invalid"
            print("Invalid input.")

        if dating == True:
            print("You can date my grandchild.")
        elif dating == False:
            print("You cannot date my grandchild.")
        else:
            print("")
        break


if __name__ == "__main__":
    main()
