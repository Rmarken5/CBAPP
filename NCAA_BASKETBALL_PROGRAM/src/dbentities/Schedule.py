from dbentities import Team
class Schedule(object):
    def __init__(self):
        self.schedule_id = 0
        self.game_date = None
        self.home_team = None
        self.away_team = None
        self.home_team_score = 0
        self.away_team_score = 0
        self.winning_team = None
        self.lossing_team = None
        
		