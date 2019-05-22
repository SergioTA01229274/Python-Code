import random
def game2():
    number = random.randint(1,100)
    answer = bool()
    tries = 1
    while answer == False or tries < 5:
        response = input("Number: ")
        try:
            response = int(response)
            if response == number:
                print("You've won")
                answer = True
                tries = 5
            elif tries == 5:
                print("You''re out of tries")
                print("The number was: ", number)
                answer = True
            else:
                if response < number:
                    print("You're wrong, the number is higher, try again")
                    tries += 1
                elif response > number:
                     print("You're wrong, the number is lower, try again")
                     tries += 1
        except ValueError:
            print("That is not an integer number, please try it again")

print("We're going to play a game")
print("I'm going to think a number and you're going to try to guess it")
print("You only have 5 tries to guess the number")
print("I'm going to tell you if the number I'm thinking is lower or higher")
game2()
