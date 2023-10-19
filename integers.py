#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: October 19, 2023
# This program is used to display the type of integer entered by the user


def main():
    # get the user integer
    user_integer = int(input("What is your integer?"))

    # if the user integer is greater than zero, say it is positive
    if user_integer > 0:
        print("{} is positive.".format(user_integer))
    elif user_integer < 0:
        # otherwise if the user integer is less than zero, say it is negative
        print("{} is negative.".format(user_integer))
    else:
        # otherwise, say the number is zero
        print("The number is 0.")


if __name__ == "__main__":
    main()
