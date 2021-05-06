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


# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before
# If 'yes', show instructions


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
        heading = "Continuous Mode: Rounds {}".format(rounds_played + 1)
    else:
        heading = "Rounds {} of {}".format(rounds_played + 1, rounds)

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
        feedback = "It's a tie"
    else:
        feedback = "{} vs {} - You {}".format(user_choice, comp_choice, result)

    # End game if exit code is typed
    if user_choice == "xxx":
        break

    # **** rest of loop / game ****

    # Output W/L statements and results
    print(feedback)
   

    rounds_played += 1

    # End game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Ask user if they want to see their game history
# If 'yes' show game history

    if result == "lost" or result == "won":
        outcome = "Round: {}: {} vs {} - You {}".format(rounds_played, user_choice, comp_choice, result)
    else:
        outcome = "Round: {}: {} vs {} - It's a tie".format(rounds_played, user_choice, comp_choice)

    game_summary.append(outcome)

# Show game statistics 
rounds_won = rounds_played - rounds_lost - rounds_drawn

# Calculate Game Stats  as a %
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

print()
print("**** Game History****")
for game in game_summary:
    print(game)

print()

# Displays game state with % values to the nearest whole number
print("******* Game Statistics *******")
print("Win: {}, ({:.0f}%)\nLoss: {}, ({:.0f}%)\nTie: {}, ({:.0f}%:)".format(rounds_won, percent_win, rounds_lost, percent_lose, rounds_drawn, percent_tie))

# End of Game Statements
print()
print("Thanks for playing")
