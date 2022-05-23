class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = ["Junior Bevil", "Michael", "Jack", "Henry"]
        self.coach = coach
        self.points = 0
        
        
    def add_player(self, new_player):
        self.players.append(new_player)
        
    def has_player(self, check_player):
        for player in self.players:
            if check_player == player:
                return True
        return False    
    
    def play_game(self, result):
        if result ==  True:
            self.points += 3