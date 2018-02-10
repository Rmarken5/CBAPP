import readbasketballlines as rl
from dbentities import Pick
from dbentities import Team
from cbapputil import date_time_util as dtu


def main():
    games = rl.main()
    picks = []
    f = openFile()
    teams_from_file = getTeamsFromFile(f)
    teams_from_game = []
    
    for game in games:
        if game is not None and game.period.period_description == 'Game':
            teams_from_game.append(game.participant_one.participant_name)
            teams_from_game.append(game.participant_two.participant_name)

    for team in sorted(teams_from_game):
        if team not in teams_from_file:
            f.write(team + '\n')
    f.close()
def openFile():
    f = open('C:/Users/Ryan/Documents/Python_Workspace/CBAPP/NCAA_BASKETBALL_PROGRAM/misc_files/teams_from_api.txt' ,'a+' )
    return f

def getTeamsFromFile(file):
    teams = []
    fl = file.readlines()

    for l in fl:
        teams.appen(l)
    return teams



if __name__ == '__main__':
    main();