import random


# Functions go here

# Asks user how many rounds to be played
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # is an integer that is more
        if response != "":
            try:
                response = int(response)

                # If the response is to low, go back to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            # If response is not an integer, go back to
            # start of loop
            except ValueError:
                print(round_error)
                continue

        return response

#  Check if response to question is valid
def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list ( or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item is not in list
        print(error)
        print()

# Displays instuctions if asked
def instructions():
    print()
    print("**** How to Play ****\n\nChoose either a number of rounds or press <enter> for infinite mode\n\nThen for each round, choose from rock / paper / scissors (or xxx to quit)\nYou can type r / p / s / x if you don't want to type the entire word.\n\nThe rules are...\n- Rock beats scissor\n- Scissor beats paper\n- Paper beats rock\n\n*** Have fun ***\n")
    return ""

# Confirms yes / no response
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


# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before
# If 'yes', show instructions
played_before = yes_no("Have you played the "
                           "game before? ")

if played_before == "no":
    instructions()

# Ask user for # of rounds then loop...
game_summary = []

rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "========== Continuous Mode: Round {} ===========".format(rounds_played + 1)
    else:
        heading = "========== Rounds {} of {} ==========".format(rounds_played + 1, rounds)

    print(heading)
    choose_instruction = "Please choose rock, paper or scissors or 'xxx' to exit: "
    choose_error = "Please choose from rock, paper or scissors or 'xxx' to exit: "

    # Ask user for choice and check it's valid
    user_choice = choice_checker(choose_instruction, rps_list, choose_error)

    # Randomly generate computer choice
    comp_choice = random.choice(rps_list[:-1])

    # Compare user to comp choice and give result
    if comp_choice == user_choice:
        result = "tie"
        rounds_drawn +=1
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "won"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "won"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "won"
    else:
        result = "lost"
        rounds_lost += 1

    if result == "tie":
        feedback = "{} vs {} - It's a tie".format(user_choice, comp_choice)
    else:
        feedback = "{} vs {} - You {}".format(user_choice, comp_choice, result)

    # End game if exit code is typed after 1 round
    if user_choice == "xxx" and rounds_played > 0:
        break

    # If exit code is entered before 1 round, prompt user to play at least one round
    elif user_choice == "xxx" and rounds_played == 0:
        print("You need to play at least one round")
        continue

    # Output W/L statements and results
    print(feedback)
    rounds_played += 1

    # Calculate game history
    if result == "lost" or result == "won":
        outcome = "Round: {}: {} vs {} - You {}".format(rounds_played, user_choice, comp_choice, result)
    else:
        outcome = "Round: {}: {} vs {} - It's a tie".format(rounds_played, user_choice, comp_choice)

    game_summary.append(outcome)

    # End game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Rest of the code 

# Show game statistics 
rounds_won = rounds_played - rounds_lost - rounds_drawn

# Calculate Game Stats as a %
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

# Ask user if they want to see their game history
print()
game_history = yes_no("Do you want to see game history? ")

if game_history == "yes":
    print()
    print("**** Game History ****\n")
    for game in game_summary:
        print(game)

# Displays game state with % values to the nearest whole number
print()
print("******* Game Statistics *******")
print("Win: {}, ({:.0f}%)\nLoss: {}, ({:.0f}%)\nTie: {}, ({:.0f}%:)\n".format(rounds_won, percent_win, rounds_lost, percent_lose, rounds_drawn, percent_tie))

# End of Game Statements
print()
print("Thanks for playing")
