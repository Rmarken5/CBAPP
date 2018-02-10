import readbasketballlines as rl
from dbentities import Pick
from dbentities import Team
from cbapputil import date_time_util as dtu


def main():
    games = rl.main()
    picks = []
    f = openFile()
    log = openLog()
    teams_from_file = getTeamsFromFile(f,log)
    teams_from_game = []
    
    for game in games:
        if game is not None and game.period.period_description == 'Game':
            teams_from_game.append(game.participant_one.participant_name)
            teams_from_game.append(game.participant_two.participant_name)

    for team in sorted(teams_from_game):
        if team not in teams_from_file:
            log.write('Writing team to file: ' + team)
            f.write(team + '\n')
        else:
            log.write('Omitting team from file: ' + team)
    f.close()
def openFile():
    f = open('C:/Users/Ryan/Documents/Python_Workspace/CBAPP/NCAA_BASKETBALL_PROGRAM/misc_files/teams_from_api.txt' ,'a+' )
    return f
def openLog( ):
    log = open('C:/Users/Ryan/Documents/Python_Workspace/CBAPP/NCAA_BASKETBALL_PROGRAM/misc_files/teams_from_api_log.txt' ,'a+')
    return log
def getTeamsFromFile(file,log):
    teams = []
    fl = file.readlines()

    for l in fl:
        log.write('Found in file: ' + l)
        teams.appen(l)
    return teams



if __name__ == '__main__':
    main();