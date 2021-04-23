# -*- coding: utf-8 -*-
"""
@author: Vivian
"""

"""
HangmanRound() stores the information of the current round,
including the puzzle word, clue word, hits and misses. Boolean value is_round_complete signals if the round is complete.
Each variable has its getter and setter function.
"""
class HangmanRound:
    
    def __init__(self):
        self.puzzleword = ''
        self.clueword = ''
        self.is_round_complete = False
        self.hit_count = 0
        self.miss_count = 0
    
    # getter for puzzle word
    def get_puzzle(self):
        return self.puzzleword
    
    # setter for puzzle word
    def set_puzzle(self, puzzleword):
        self.puzzleword = puzzleword
    
    # getter for clue word
    def get_clue(self):
        return self.clueword
    
    # setter for clue word
    def set_clue(self, clueword):
        self.clueword = clueword
    
    # getter for is_round_complete
    def get_is_round_complete(self):
        return self.is_round_complete
    
    # setter for is_round_complete
    def set_is_round_complete(self, is_round_complete):
        self.is_round_complete = is_round_complete
    
    # getter for hit count
    def get_hit_count(self):
        return self.hit_count
    
    # setter for hit count
    def set_hit_count(self, hit_count):
        self.hit_count = hit_count
    
    # getter for miss count
    def get_miss_count(self):
        return self.miss_count
    
    # setter for miss count
    def set_miss_count(self, miss_count):
        self.miss_count = miss_count


