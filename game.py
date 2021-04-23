# -*- coding: utf-8 -*-
"""
@author: Vivian
"""

from hangman import Hangman

"""
Game() is the entrance and contains different games for users to play(currently only hangman)
Based on user's choice, the Game class will start the game and generate a new round
"""
class Games:
    
    # game ids for hangman
    HANGMAN_GAME_ID = 1
    OTHER_GAME_ID = 2
    
    
    def main(self):
        # enter the game and start playing
        game_id = self.get_game_choice()
        self.play_game(game_id)
        
        # leave game
        print('Bye!')
    
    
    def __init__(self):
        pass
    
    
    # return the choice of game the user chooses
    def get_game_choice(self):
        not_valid_ans = True
        while not_valid_ans:
            # print game menu
            print('Let\'s play games!')
            print('--------------------')
            print('1. Hangman\n2. Other\n3. Exit')
            print('--------------------')
        
            # get user's choice
            game_id = input()
            if game_id.isdigit():
                if 1 <= int(game_id) <= 3:
                    not_valid_ans = False
                else:
                    print('Invalid input!\n')
            else:
                print('Invalid input!\n')
        
        return int(game_id)
    
    
    # play the selected game based on user's choice
    def play_game(self, id):
        if id == self.HANGMAN_GAME_ID:
            print('Play Hangman!\n')
            self.hm = Hangman()
            self.hm.start_game()
        elif id == self.OTHER_GAME_ID:
            print('Other games coming soon!')
        else:
            print('Exiting game')
    

if __name__=="__main__":
    games = Games()
    games.main()