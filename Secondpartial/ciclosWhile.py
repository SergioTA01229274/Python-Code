import os


def sum1(n):
    result = 0
    cont = 0
    while cont < n + 1:
        result += cont
        cont += 1
    return result


def multiply(n):
    cont = 1
    result = 1
    while cont < n + 1:
        c = cont * 2
        result *= c
        cont += 1
    return result


def H1(n):
    cont = 0
    result = 0
    while cont < n + 1:
        if cont % 2 == 0:
            result -= cont
        else:
            result += cont
        cont += 1
    return result


def H2(n):
    cont = 0
    result = 0
    while cont < n + 1:
        result += (2 * cont + 2)
        cont += 1
    return result


def triangularNumbers(n):
    cont = 1
    while cont <= n:
        number = (cont * (cont + 1)

                  ) // 2
        print("T", cont, "=", number)
        cont += 1


def numDig(n):
    cont = 1
    digits = 0
    condition = bool()
    while condition:
        if n / cont >= 1:

            digits += 1
            cont *= 10
        else:
            condition = True
    return digits


def menu():
    print("This program can do different different things:")
    print("1. Calculate the sum of a series of numbers")
    print("2. Calculate the multipication other of a series of numbers")
    print("3. Calculate an operation which adds the odd numbers of a series")
    print("   and substracts the even ones")
    print("4. Calculate the sum of a series of numbers that its terms has the")
    print("   form (2*n +2)")
    print("5. Show the first n triangular numbers")
    print("6. Count the digits of a number")
    print("7. Finish the program")
    print("Please insert the number of the option you want to do")


menu()
while True:
    option = input("Option number:")
    try:
        option = int(option)
        if option == 1:
            os.system("cls")
            print("Insert how much numbers you want to add")
            while True:
                a = input("x: ")
                try:
                    a = int(a)
                    print("The answer is:", sum1(a))
                    print("Want to go back to the menu?")
                    b = input("Answer: ")
                    if b == "yes":
                        os.system("cls")
                        menu()
                        break
                except ValueError:
                    print("You have to insert an integer number")
        elif option == 2:
            os.system("cls")
            print("Insert how much terms do you want to multiply")
            while True:
                a = input("Answer: ")
                try:
                    a = int(a)
                    print("The answer is:", multiply(a))
                    print("Want to go back to menu?")
                    b = input("Answer: ")
                    if b == "yes":
                        os.system("cls")
                        menu()
                        break
                except ValueError:
                    print("That is not an integer value")
        elif option == 3:
            os.system("cls")
            print("Insert the number of terms you want to calculate")
            while True:
                a = input("Anuser: ")
                try:
                    a = int(a)
                    print("The answer is:", H1(a))
                    print("Want to go back to menu")
                    b = input("Answer: ")
                    if b == "yes":
                        os.system("cls")
                        menu()
                        break
                except ValueError:
                    print("That is not an integer number")
        elif option == 4:
            os.system("cls")
            print("Insert the number of terms you want to calculate")
            while True:
                a = input("Anuser: ")
                try:
                    a = int(a)
                    print("The answer is:", H2(a))
                    print("Want to go back to menu")
                    b = input("Answer: ")
                    if b == "yes":
                        os.system("cls")
                        menu()
                        break
                except ValueError:
                    print("That is not an integer number")
        elif option == 5:
            os.system("cls")
            print("Insert how much triangular numbers you want to obtain:")
            while True:
                a = input("Anuser: ")
                try:
                    a = int(a)
                    print("The answer is:", triangularNumbers(a
                                                              ))
                    print("Want to go back to menu")
                    b = input("Answer: ")
                    if b == "yes":
                        os.system("cls")
                        menu()
                        break
                except ValueError:
                    print("That is not an integer number")
        elif option == 6:
            os.system("cls")
            print("Insert the number you want to know the digits of")
            while True:
                a = input("Anuser: ")
                try:
                    a = int(a)
                    print("The answer is:", numDig(a))
                    print("Want to go back to menu")
                    b = input("Answer: ")
                    if b == "yes":
                        os.system("cls")
                        menu()
                        break
                except ValueError:
                    print("That is not an integer number")
        elif option == 7:
            os.system("cls")
            print("Bye")
            break
    except ValueError:
        print("You have to insert an integer value")
