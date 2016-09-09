
import os, random

def pc_choice(game_mode):
    random.seed(version=2)
    rand = random.randint(0, game_mode)
    if rand == 0:
        pc_chc = "Rock"
    elif rand == 1:
        pc_chc = "Paper"
    elif rand == 2:
        pc_chc = "Scissors"
    elif rand == 3:
        pc_chc = "Lizard"
    elif rand == 4:
        pc_chc = "Spock"
    return pc_chc

def your_choice(game_mode):
    os.system('cls')
    print("Now choose your weapon: \n"
          "1) Rock \n"
          "2) Paper \n"
          "3) Scissors ")
    if game_mode == 4:
        print("4) Lizard \n"
              "5) Spock")
    choice = input(' Your Choice (1/Rock or 2/Paper etc. ): ')
    if choice.lower() == 'rock' or str(choice) == '1':
        your_chc = "Rock"
    elif choice.lower() == 'paper' or str(choice) == '2':
        your_chc = "Paper"
    elif choice.lower() == 'scissors' or str(choice) == '3':
        your_chc = "Scissors"
    elif (choice.lower() == 'lizard' or str(choice) == '4') and game_mode == 4:
        your_chc = "Lizard"
    elif (choice.lower() == 'spock' or str(choice) == '5') and game_mode == 4:
        your_chc = "Spock"
    else:
        return
    return your_chc

def play_game(number, game_mode):
    wins = loses = 0
    while number:
        pc_chc = pc_choice(game_mode)
        your_chc = your_choice(game_mode)
        os.system('cls')
        try:
            print("Your choice: " + your_chc)
            print("PC choice: " + pc_chc + "\n")
            if pc_chc == your_chc:
                print("It's a draw!")
            elif your_chc == 'Rock' and (pc_chc == 'Scissors' or pc_chc == 'Lizard'):
                wins += 1
                print("You win this match!\n")
            elif your_chc == 'Paper' and (pc_chc == 'Rock' or pc_chc == 'Spock'):
                wins += 1
                print("You win this match!\n")
            elif your_chc == 'Scissors' and (pc_chc == 'Paper' or pc_chc == 'Lizard'):
                wins += 1
                print("You win this match!\n")
            elif your_chc == 'Lizard' and (pc_chc == 'Spock' or pc_chc == 'Paper'):
                wins += 1
                print("You win this match!\n")
            elif your_chc == 'Spock' and (pc_chc == 'Scissors' or pc_chc == 'Rock'):
                wins += 1
                print("You win this match!\n")
            else:
                loses += 1
                print("You lose this match!\n")
            print("Matches wins: " + str(wins) + "\n"
                  "Matches lost: " + str(loses) + "\n")
            input()
            os.system('cls')
            if wins == number:
                print("Congratulations! You Win!")
                input()
                return
            if loses == number:
                print("Looks like, You lose this time!")
                input()
                return
        except:
            os.system('cls')
            print("I'm error. Try valid answer!")
            input()
            return

def play_menu(game_mode):
    os.system('cls')
    print("Now choose number of games: \n"
          "1) 1 out 1 \n"
          "2) 2 out 3 \n"
          "3) 3 out 5 \n")
    choice = input(' Your Choice (1 or 2 or 3): ')
    if str(choice) == '1':
        number = 1
    elif str(choice) == '2':
        number = 2
    elif str(choice) == '3':
        number = 3
    else:
        os.system('cls')
        print("I'm error. Try valid answer!")
        input()
        return
    play_game(number, game_mode)

def main():
    ans = 1
    while ans:
        os.system('cls')
        print ("Choose game mode: \n"
               "1) Normal: Rock - Paper - Scissors \n"
               "2) Hard: Rock - Paper - Scissors - Lizard - Spock \n"
               "3) Exit \n")
        choice = input(' Your Choice (1/Normal or 2/Hard or 3/Exit): ')
        if choice.lower() == 'normal' or str(choice) == '1':
            game_mode = 2
        elif choice.lower() == 'hard' or str(choice) == '2':
            game_mode = 4
        elif choice.lower() == 'exit' or str(choice) == '3':
            break
        else:
            os.system('cls')
            print("I'm error. Try valid answer!")
            input()
            continue
        play_menu(game_mode)

if __name__ == "__main__":
    try:
        main()
    except ValueError:
        os.system('cls')
        print("Oops!  We have an issue here! " + ValueError)
        input()