# -*- coding: utf-8 -*-
"""
@author: Vivian Chang
"""

import random as rd
import string as st
from hangman_round import HangmanRound 


"""
Hangman() is one type of games
Each time the user enters the game, it will start a new hangman round and initialize the puzzle word and clue word
The user has a maximun the number of trials defined by the constant HANGMAN_TRIALS,
and appropriate messages will be displayed depending on user's guesses
"""
class Hangman:
    
    # declare constant vatiables
    # word length limits for hangman game
    MIN_WORD_LENGTH = 5
    MAX_WORD_LENGTH = 10
    # maximum guesses before game over
    HANGMAN_TRIALS = 10

    # message index and messages to be displayed after each trial
    RIGHT_MESSAGE_INDEX = 0
    WRONG_MESSAGE_INDEX = 1
    ALREADY_ENTERED_MESSAGE_INDEX = 2
    PART_OF_CLUE_MESSAGE_INDEX = 3
    CONGRATULATIONS_MESSAGE_INDEX = 4
    LOST_MESSAGE_INDEX = 5

    messages_array = [":-) You got that right!", #RIGHT_MESSAGE_INDEX
    ":-( Sorry! Got it wrong!", #WRONG_MESSAGE_INDEX
    ":-o You already entered that!", #ALREADY_ENTERED_MESSAGE_INDEX
    ":-\\ Part of the clue!", #PART_OF_CLUE_MESSAGE_INDEX
    ":-D Congratulations! You won!", #CONGRATULATIONS_MESSAGE_INDEX
    ":-( Sorry! You lost this one!"] #LOST_MESSAGE_INDEX
    
    def __init__(self):
        self.word_list = self.read_file()
        self.hangman_round = HangmanRound()
        self.user_inputs = ''
    
    # reads the file that contains a list of words for the game
    def read_file(self):
        with open('wordsFile.txt', 'rt', encoding = 'utf-8') as f:
            word_list = [line[:-1] for line in f]
        return word_list
    
    
    # starts a new round of game
    def start_game(self):
        # set up a new round of a game
        self.hangman_round.set_puzzle(self.find_puzzle());
        puzzle_w = self.hangman_round.get_puzzle()
        self.hangman_round.set_clue(self.make_a_clue(puzzle_w))
        # print(puzzle_w)
        
        # start playing the round
        self.play_round()
        
        # print final result
        print('Your score is: ', self.get_score())
        
    
    # generate the puzzle word using candidate words in the file,
    # the candidate word length should be between MIN_WORD_LENGTH and MAX_WORD_LENGTH
    def find_puzzle(self):
        random_index = rd.randint(0, len(self.word_list)-1)
        
        while len(self.word_list[random_index]) < self.MIN_WORD_LENGTH or len(self.word_list[random_index]) > self.MAX_WORD_LENGTH:
            random_index = rd.randint(0, len(self.word_list)-1)
        
        return self.word_list[random_index]
    
    
    # generate clue word: replace some letters in the selected puzzle word with '-'
    def make_a_clue(self, puzzleword):
        max_replace = len(puzzleword)//2
        not_over_max = True
        
        while not_over_max:
            random_char = rd.choice(st.ascii_lowercase)
            if random_char in puzzleword:
                puzzleword = puzzleword.replace(random_char, '-')
                if(self.count_dashes(puzzleword) > max_replace):
                    not_over_max = False
        return puzzleword
    
    
    # counts the number of dashes a word contains
    def count_dashes(self, word):
        count = 0
        for char in word:
            if char == '-':
                count += 1
        return count
    
    
    # start to play and guess the puzzle word using clueword
    def play_round(self):
        trial_num = 1
        puzzle_w = self.hangman_round.get_puzzle()
        
        # 1. Take user input, validate input
        while not self.hangman_round.get_is_round_complete():
            is_not_valid = True
            while is_not_valid:
                print('The clue word is: ', self.hangman_round.get_clue())
                print('***Trial#', trial_num, 'Enter your guess: ')
                guess = input()
                if guess.isalpha() and len(guess) == 1:
                    is_not_valid = False
                    guess = guess.lower()
                else:
                    print('Invalid input!\n')
            
            # 2. Check if input is guessed/ in the clue/ correct /incorrect
            result = self.next_try(guess)
            print(self.messages_array[result])
            
            # Scenario a: The player guessed out the word before out of guesses
            if self.hangman_round.get_clue() == puzzle_w:
                self.hangman_round.set_is_round_complete(True)
                print('The word is: ', puzzle_w)
                print(self.messages_array[self.CONGRATULATIONS_MESSAGE_INDEX])
                break
            
            # Scenario b: The player guessed correct/ incorrect, and hasn't guessed out the word
            if result == self.RIGHT_MESSAGE_INDEX or result == self.WRONG_MESSAGE_INDEX:
                trial_num += 1
            if trial_num > self.HANGMAN_TRIALS:
                self.hangman_round.set_is_round_complete(True)
            
            # Scenario c: The player failed to guess out the word within the limited guesses
            if trial_num > self.HANGMAN_TRIALS:
                print('The word is: ', puzzle_w)
                print(self.messages_array[self.LOST_MESSAGE_INDEX])
    
    
    # determine whether the guessed letter is in the puzzle word, update hit/miss counts and update clueword
    def next_try(self, guess):
        clue_w = self.hangman_round.get_clue()
        puzzle_w = self.hangman_round.get_puzzle()
        
        if guess in self.user_inputs:
            return self.ALREADY_ENTERED_MESSAGE_INDEX # already guessed letter
        elif guess in clue_w:
            return self.PART_OF_CLUE_MESSAGE_INDEX # letter is part of the clue
        elif guess not in puzzle_w: # wrong guess of letter
            self.hangman_round.set_miss_count(self.hangman_round.get_miss_count()+1)
            self.user_inputs += guess
            return self.WRONG_MESSAGE_INDEX
        else:
            # right guess of letter
            self.hangman_round.set_hit_count(self.hangman_round.get_hit_count()+1)
            self.user_inputs += guess
            
            # update the clueWord
            for c, v in enumerate(puzzle_w):
                if v == guess:
                    clue_w = clue_w[0:c] + guess + clue_w[c+1:]
            self.hangman_round.set_clue(clue_w)
            return self.RIGHT_MESSAGE_INDEX
            
    
    # calculate score based on hit and miss counts
    def get_score(self):
        hits = self.hangman_round.get_hit_count()
        misses = self.hangman_round.get_miss_count()
        
        if misses == 0:
            return hits
        else:
            return round(hits/misses, 2)




