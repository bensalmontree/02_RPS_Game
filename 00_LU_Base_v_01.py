import random

# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
    statement_generator("How to Play", "*")
    print()
    print("Choose a starting amount (minimum $1, maximum $10).\n")
    print("Then press <enter> to play. You will either get a horse, "
          "a zebra, a donkey or a unicorn.\n")
    print("It costs $1 per round. Depending on your prize you might "
          "win some money back. Here's the payout amounts...\n")
    print("Unicorn: Balance increases by $4.00")
    print("Horse: Balance decreases by $0.50")
    print("Zebra: Balance decreases by $0.50")
    print("Donkey: Balance decreases by $1.00\n")
    print("Can you avoid the donkeys, and get the unicorns"
          " and walk home with the money??\n")
    print("Hint: To quit while you're ahead, type in 'xxx' instead of <enter>\n")
    return ""


def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n "

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)

def statement_generator(statement, decoration):
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""

# Main Routine goes here...
# Ask user if they have played before...
statement_generator("Welcome to the Lucky Unicorn Game!", "*")
print()

played_before = yes_no("Have you played the game before?")
print()

if played_before == "no":
    instructions()

# Ask how much they want to play with...
statement_generator("Let's get Started...","-")
print()

how_much = num_check("How much would you"
                     " like to play with? ", 0, 10)

balance = how_much 

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print()
    statement_generator("Round #{}".format(rounds_played),".")
    print()

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
        prize_decoration = "!"

    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
        prize_decoration = "D"

    # The token is either a horse or zebra...
    # in both cases, subtract $0.50 from the balance
    else:
        # if the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    # output
    outcome = "You got a {}. Your balance is  ${:.2f}".format(chosen,balance)

    statement_generator(outcome, prize_decoration)
    print()

    if balance < 1:
        play_again = "xxx"
        statement_generator("Sorry you have run out of money", "V")
    else:
        play_again = input("Press Enter to play again "
                           "or 'xxx' to quit")


print()
statement_generator("Results", "=")
print()
print("Final Balance: ${:.2f}".format(balance))
print("Thank you for playing!")
