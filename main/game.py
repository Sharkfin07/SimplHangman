import random

topic = {
    'Transportation': ("car", "truck", "bicycle", "unicycle", "train", "airplane"
    , "helicopter", 'tricycle', 'motorcycle', 'bus'),
    'Car Brands': ("honda", 'toyota', 'nissan', 'ford', 'tesla', 'chevrolet', 'bentley', 'mclaren',
    'bmw', 'dodge', 'seat', 'dmc', 'lotus', 'bugatti', 'suzuki', 'audi'),
    'Music Instruments': ('guitar', 'piano', 'angklung', 'bass', 'gong', 'keyboard',
    'drums', 'bongo', 'mandolin', 'ukelele', 'triangle', 'violin', 'cello')
}

class Player:
    def player_turn(self):
        quiz_topic = random.choice(list(topic))
        print(f"Today's Hangman topic is {quiz_topic}!")
        quiz_ans = random.choice(topic[str(quiz_topic)])
        corr_input = []
        for input_ans in quiz_ans:
            corr_input.append(input_ans)
        blank = []
        for word in corr_input:
            blank.append("_")
        chances = 10
        while chances > 0:
            print(f"Guesses left: {chances}")
            print(blank)
            player_guess = input("> ").lower()
            if len(player_guess) > 1:
                print("Please input one letter.")
            else:
                if player_guess in corr_input:
                    num_corr_letter = corr_input.count(player_guess)
                    if num_corr_letter > 1:
                        print("You got two correct letters at once!")
                        for c_in in range(2):
                            placement = corr_input.index(player_guess)
                            blank.pop(placement)
                            corr_input.pop(placement)
                            corr_input.insert(placement, "done")
                            blank.insert(placement, player_guess)
                    else:
                        placement = corr_input.index(player_guess)
                        blank.pop(placement)
                        corr_input.pop(placement)
                        corr_input.insert(placement, "done")
                        blank.insert(placement, player_guess)

                else:
                    print("Your guess is incorrect!")
                    chances -= 1
                if blank.count('_') == 0:
                    print("You have won!")
                    break
    
    def twop_game(self):
        print("Welcome to 2 player hangman. Enter 'r' to show rules, enter 's' to begin.")
        twop_on = True
        while twop_on:
            cmd_2p = input("> ")
            if cmd_2p == 'r':
                print("""Player 1's role is to define a topic and the answer, and Player 2 is going to guess the answer.""")
            if cmd_2p == 's':
                print("It's Player 1's turn! Player 2 would you kindly turn around or close your eyes.")
                topic_2p = input ("> Input the topic: ").title()
                ans_2p = input("> Input the answer: ").lower()
                corr_input = []
                blank = []
                for answer_2p in ans_2p:
                    corr_input.append(answer_2p)
                    blank.append('_')
                print("Ready? Press Enter to continue.")
                input("> ")
                print("""
                 
                """*20)
                print("="*120)
                print("Player 2 open your eyes.")
                print(f"Today's Hangman topic is {topic_2p}")
                chances_2p = 10
                while chances_2p > 0:
                    print(f"Guesses left: {chances_2p}")
                    print(blank)
                    player_guess = input("> ")
                    if len(player_guess) > 1:
                        print("Please input one letter.")
                    else:
                        if player_guess in corr_input:
                            num_corr_letter = corr_input.count(player_guess)
                            if num_corr_letter > 1:
                                print("You got two correct letters at once!")
                                for c_in in range(2):
                                    placement = corr_input.index(player_guess)
                                    blank.pop(placement)
                                    corr_input.pop(placement)
                                    corr_input.insert(placement, "done")
                                    blank.insert(placement, player_guess)
                            else:
                                placement = corr_input.index(player_guess)
                                blank.pop(placement)
                                corr_input.pop(placement)
                                corr_input.insert(placement, "done")
                                blank.insert(placement, player_guess)

                        else:
                            print("Your guess is incorrect!")
                            chances_2p -= 1
                        if blank.count('_') == 0:
                            print("You have won!")
                            break
                break

    def game_over(self, x):
        if x.lower() == 'y':
            return True
        elif x.lower() == 'n':
            return False
        return None
        

player = Player()
game_rand = False
game_2p = False
prog_on = True
while prog_on:
    print("Welcome to Simple Hangman by Sharkfin! Please enter a command.")
    print("""(1) Random Generated
(2) 2 Player Hangman
(3) Quit""")
    cmd_main = input("> ")
    if cmd_main == '1':
        game_rand = True
    elif cmd_main == '2':
        game_2p = True
    elif cmd_main == '3':
        break
    else:
        print('Please enter a valid command.')
    
    while game_rand:
        player.player_turn()
        print("Do you want to play again? (y/n)")
        cmd_go = input("> ")
        btdd = player.game_over(cmd_go)
        if not btdd:
            game_rand = False
            break
        if btdd:
            continue
    
    while game_2p:
        player.twop_game()
        print("Do you want to play again? (y/n)")
        cmd_go = input("> ")
        btdd = player.game_over(cmd_go)
        if not btdd:
            game_2p = False
            break
        if btdd:
            continue
        





