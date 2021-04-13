# RPS Component 3 - Compare user choice and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # Compare options...
        if comp_choice == "rock" and user_choice == "rock":
            result = "tie"
        if comp_choice == "rock" and user_choice == "paper":
            result = "win"
        if comp_choice == "rock" and user_choice == "scissors":
            result = "lose"
        if comp_choice == "paper" and user_choice == "rock":
            result = "lose"
        if comp_choice == "paper" and user_choice == "paper":
            result = "tie"
        if comp_choice == "paper" and user_choice == "scissors":
            result = "win"
        if comp_choice == "scissors" and user_choice == "rock":
            result = "win"
        if comp_choice == "scissors" and user_choice == "paper":
            result = "lose"
        if comp_choice == "scissors" and user_choice == "scissors":
            result = "tie"

        print("You chose {}, the computer chose {}.\nResult: {}".format(user_choice, comp_choice, result))

    comp_index += 1
    print()
