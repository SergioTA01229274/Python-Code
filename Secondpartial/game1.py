import random
def game(n1, n2):
    lim1 = n1
    lim2 = n2
    answer = bool()
    while answer == False:
            number = random.randint(lim1,lim2)
            print("The number I'm thinking is: ", number)
            feedback = input("The number you're thinking is: ")
            feedback = feedback.lower()
            try:
                if feedback == "equal":
                    print("Thanks for playing with me")
                    answer = True
                else:
                    if feedback == "higher":
                        lim1 = number
                    elif feedback == "lower":
                        lim2 = number
            except ValueError:
                print("That is not a word, try it again")
print("Lets play a game")
print("You're going to think a number between two limits and I will guess it")
print("First you have to stipulate those limits")
print("After I generate the number you have to say if the number you're")
print("thinking is: higher, lower or equal")

while True:
    a = input("Limit 1: ")
    b = input("Limit 2: ")
    try:
        a = int(a)
        b = int(b)
        game(a,b)
        break
    except ValueError:
        print("One of the limits is not an integer, please insert them again")
