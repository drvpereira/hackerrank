from functools import cmp_to_key

class Player:
    def __init__(self, name, score):        
        self.name = name
        self.score = score
    def __repr__(self):
        self.name = ""
        self.score = 0
        
    def comparator(a, b):
        score = b.score - a.score
        if score == 0:
            if a.name > b.name:
                return 1
            elif a.name < b.name:
                return -1
            else:
                return 0
        else:
            return score
