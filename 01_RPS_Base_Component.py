import random


# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
            "or an integer that is more than 0"

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


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
            "or an integer that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before
# If 'yes', show instructions


# Ask user for $ of rounds then loop...
rounds_played = 0
choose_instruction = "Please choose rock (r), paper " \
     "(p) or scissors (s)"

# Ask user for # of rounds, <enter> for infinite mode
rounds_played = 0
choose_instruction = "Please choose rock (r), paper " \
     "(p) or scissors (s)"

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
        heading = "Rounds {} of " \
                "{}".format(rounds_played + 1, rounds)

    print(heading)

    choose = input("{} or 'xxx' to end: ".format(choose_instruction))
    # End game if exit code is typed
    if choose == "xxx":
        break

    # **** rest of loop / game ****
    print("You chose {}".format(choose))

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Ask user if they want to see their game history
# If 'yes' show game history

# Show game statistics
