import random


def game(n1, n2):
    lim1 = n1
    lim2 = n2
    answer = bool()
    while answer:
            number = random.randint(lim1, lim2)
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


game(30, 230)
