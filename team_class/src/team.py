class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players 
        self.coach = coach
        self.points = 0
        
        
    def add_player(self, new_player):
        self.players.append(new_player)
        
    def has_player(self, check_player):
        # LAB SOLUTION
        # for player in self.players:
        #     if check_player == player:
        #         return True
        # return False    

        # MENTOR SOLUTION
        if check_player in self.players:
            return True
        else:
            return False
    
    def play_game(self, game_won):
        if game_won ==  True:
            self.points += 3