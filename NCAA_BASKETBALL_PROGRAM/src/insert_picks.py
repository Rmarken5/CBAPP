import readbasketballlines as rl
from dbentities import Pick
from cbapputil import date_time_util as dtu

def main():

    games = rl.main()
    picks = []
    for game in games:
        pick = getPickFromGame(game)
        picks.append(pick)

    for pick in picks:
        pick.insertPick()
		

def getPickFromGame(game):
    pick = None
    if game != None:
        pick = Pick()
        pick.game_date = dtu.getDateObjectFromString(game.event_datetime)
        pick.game_time = dtu.getTimeObjectFromString(game.event_datetime)
        team_one = getTeamFromParticipant(game.participant_one)
        team_two = getTeamFromParticipant(game.participant_two)
        if team_one is not None and team_two is not None:
            pick.away_team = team_one
            pick.home_team = team_two
            favorite = calculateFavorite(pick.away_team, pick.home_team)
            if favorite is not None:
                pick.favorite_team = favorite
                pick.spread = game.period.spread
		
        
def getTeamFromParticipant(participant):
    team = None
    if participant is not None:
        team = Team()
        team.spread_name = participant
        team.findTeamBySpreadName()
    return team

def calculateFavorite(away_team, home_team):

    if away_team is not None and home_team is not None:
        at_ats_rec = (away_team.ats_wins - away_team.ats_losses)
        ht_ats_rec = (home_team.ats_wins - home_team.ats_losses)
		
        if at_ats_rec > ht_ats_rec:
            return away_team
        else:
            return home_team
    return None


	
if __name__ == '__main__':
    main()