import random
computer_score = 0
player_score = 0
while True:

    player_choice = input("Your choice: [R,S,P]: ").lower()
    if player_choice not in ["r","s","p"]:
        print("Incorrect input.Try again")
        continue
    gen = {1:"r" , 2:"s" , 3:"p"}
    #r - scissors
    #s - stone
    #p - papper
    comp_choice = gen[random.randint(1,3)]
    winning_combinations = [("p","r"),("r","s"),("s","p")]
    if player_choice == comp_choice:
        print("no one won")
    elif (player_choice , comp_choice) in winning_combinations :
        print("player won")
        player_score+= 1
    else:
        print("Computer won")
        computer_score+=1
    if computer_score == 5 or player_score == 5:
        print(computer_score, player_score)
        if computer_score > player_score:
            print("Computer won ")
        else:
            print("player won")
        break
