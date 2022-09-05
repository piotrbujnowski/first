import random

play = True
while play:
    
    
    # initial variables
    lifes = 7

    user_name = input('Enter your name, to play the game: ').capitalize()
    print('\nHello ' + user_name + ', try to guess capital city, randomly choosen for you.\n' )
    
 

    # preparation
    f = open('countries-and-capitals.txt')
    lines = f.readlines()
    f.close
    country_capital = random.choice(lines)
    words = country_capital.strip().split(' | ')

    # print(country_capital)

    country = words[0].upper()
    print(country)
    capital = words[1].upper()
    print(capital)

    board = []
    missed_letters = []
    already_tried_letters = []
    is_winner = False
    
    for letter in capital:
        if(letter == " "):
            board.append(" ")
        else:
            board.append("_")

    while lifes > 0 and not is_winner:
        print(" ".join(board))  # glue letters from board array with space char
        print('')
        if lifes == 1:
                print('\nHint: the capital of ' + words[0] + "\n")  # gives a hint
        print("Lifes: " + str(lifes))
        print("Missed letters: "+", ".join(set(missed_letters)))
        print("Hit letters: "+", ".join(set(already_tried_letters)))
        guess = input('Enter a letter or full word: ').upper()
        
             
        letter_occurencies = 0
        if len(guess) > 1:  # for whole word
            if guess == capital:
                is_winner = True
            else:
                print('Wrong answear!')
                lifes -= 2

        else:   # for the letter
            i = 0
            for letter in capital:
                if letter == guess:
                    board[i] = letter
                    if letter not in already_tried_letters:
                        already_tried_letters.append(guess)
                        letter_occurencies += 1  # occurency in word (capital)
                i += 1
            if "".join(board) == capital:  # glue letters from board array with empty char
                is_winner = True
            if letter_occurencies == 0:
                missed_letters.append(guess)
                lifes -= 1
                print('\nWrong letter!\n')
                print('')
    if lifes == 0:
        print('Game over!')

    if is_winner:
        print('You won ! ' + user_name + ' that capital city is: ' + capital + '\n')
        

        

        f.close()

    replay_game = input('\nPlay again? (Y/n): ')
    if replay_game == "n":
        play = False