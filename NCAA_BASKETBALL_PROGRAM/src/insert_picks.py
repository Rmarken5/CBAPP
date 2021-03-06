import scrape_vegas_insider as scrape
from dbentities import Pick
from dbentities import Team
from livelineentities import *
from cbapputil import date_time_util as dtu
import send_picks
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'output-files/teams_from_feed.txt')


f = open(filename, 'w')

def main():

    # games = rl.main()
    # picks = []
    # for game in games:
    #     pick = getPickFromGame(game)
    #     if pick is not None:
    #         picks.append(pick)

    games = scrape.scrapeSite()
    picks = []
    for game in games:
        pick = getPickFromGame(game)
        if pick is not None:
            picks.append(pick)

    for pick in picks:
        if pick is not None:
            pick.insertPick()
	
    send_picks.main()
    f.close( )

def getPickFromGame(game):
    pick = None
    if game != None and game.period != None and game.period.period_description == 'Game':
        pick = Pick.Pick()
        pick.game_date = dtu.getDateObjectFromString(game.event_datetime)
        pick.game_time = dtu.getTimeObjFromDTStringSec(game.event_datetime)
        
        team_one = getTeamFromParticipant(game.participant_one.participant_name)
        team_two = getTeamFromParticipant(game.participant_two.participant_name)
        if team_one is None:
            f.write(game.participant_one.participant_name + ' is not in the database. \n')
        if team_two is None:
            f.write(game.participant_two.participant_name + ' is not in the database. \n')
        if team_one is not None and team_two is not None:
            pick.away_team = team_one
            pick.home_team = team_two
            favorite = calculateFavorite(pick.away_team, pick.home_team)
            if favorite is not None:
                pick.favorite_team = favorite
                pick.spread = game.period.spread.spread_home
    return pick            
		
        
def getTeamFromParticipant(participant):
    team = None
    if participant is not None:
        team = Team.Team()
        team.spread_name = participant
        team.findTeamBySpreadName()
        if team.id is not 0:
            return team
    return None

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