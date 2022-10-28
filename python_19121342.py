#CSC1024 Programming Principles Master Mind Computer Game

#User-defined function for the correct colour in correct place and correct colour in wrong place
def feedback(correct_colour_in_correct_place, correct_colour_in_wrong_place):
    feedback1 = 'Correct colour in the correct place: '+ str(correct_colour_in_correct_place)
    feedback2 = 'Correct colour in the wrong place: '+ str(correct_colour_in_wrong_place)
    
    feedback = feedback1 + '\n' + feedback2 
    return print(feedback)

#Introduction for a Master Mind Computer Game
print('--------------WELCOME---------------')
print('This is a Master Mind Computer Game.')
print('The rule for this game is to guess four colours correctly in the right positions and you will be a Master Mind.')
print('You will only have 10 guesses. Try your best!')
print('Please enter four colour code.')
print('Here are the colour codes that you can pick.')
print('Colour codes = blue[B], green[G], pink[P], yellow[Y], red[R], white[W]')

#List of colour codes
colours = ['B', 'G', 'P', 'Y', 'R', 'W']

#Random choice 
import random

play = 'Y'


# Game has start and player starts to guess the codes
while play == 'Y' or play == 'y':
    
    #Computer randomize four colour codes
    actual_code = random.choices(colours, k=4)
    print(actual_code) #This will not be shown during the actual game
    count = 1

    game = False
    for t in range(10):
        check_again = False
        while check_again == False:
            check_again = True
            
            #Player's guess
            player_code = input('Enter your guess: ').upper()
            
            
            # To have a validation check on the user's input is correct  
            if len(player_code) > len(actual_code):
                print('You have entered more than four colour codes. Re-enter again!')
                check_again = False
            elif len(player_code) < len(actual_code):
                print('You have entered less than four colour codes. Re-enter again!')
                check_again = False
                
            else:
                for i in range(4):
                    if player_code[i] not in colours:
                        print('You have enter the wrong colour code. Try again.')
                        check_again = False
                        break
            
        #List of the player code
        player_code = list(player_code)

        #Hints about the colour code's place to the players 
        correct_colour_in_correct_place = 0
        correct_colour_in_wrong_place = 0
        
        for i in range(4):
            if player_code[i] == actual_code[i]:
                correct_colour_in_correct_place += 1
                player_code[i] += 'place' 
                actual_code[i] += 'place' 
                
        for i in range(4):
            if player_code[i] in actual_code and player_code[i] != actual_code[i]:
                correct_colour_in_wrong_place += 1
                actual_code[actual_code.index(player_code[i])] += 'place' 
                
        for i in range (4):
            if len(actual_code[i]) > 1:
                actual_code[i] = (actual_code[i])[0]
                
        if correct_colour_in_correct_place == 4:
            game = True
            break
            
        else:
            if t < 9:
                feedback(correct_colour_in_correct_place, correct_colour_in_wrong_place)
    
                
        #Calculate the attempts of guessing 
        count = count + 1
    
    #Display results
    if game == True:
        if count == 1:
            print('You have guessed correctly at the first attempt! Great job!')
        else:
            if count > 1:
                print('You won!! You are a mastermind!! The colour code is ', actual_code , 'You have took ' , str(count) , 'attempts')
    else:
        print('You have guess wrongly! The colour code is' , actual_code)
        

    
    
    #To ask the player whether to continue the game or not
    play = input('Do you wish to play again? (Y/N): ').upper()
    if play != 'Y' and play != 'N':
        print('You have enter a wrong choice!')
        play = input('Please enter again. (Y/N): ').upper()
        
print('Thanks for playing!')
        

