import readbasketballlines as rl
from dbentities import Pick
from dbentities import Team
from cbapputil import date_time_util as dtu
from datetime import datetime
import os.path


def main():
    games = rl.main()
    picks = []
    teams_from_file = []
    if os.path.isfile('/home/pegasus/python_workspace/CBAPP/NCAA_BASKETBALL_PROGRAM/misc_files/teams_from_api.txt'):
        with open('/home/pegasus/python_workspace/CBAPP/NCAA_BASKETBALL_PROGRAM/misc_files/teams_from_api.txt' ,'r+' ) as team_file:
        #open('/home/pegasus/python_workspace/CBAPP/NCAA_BASKETBALL_PROGRAM/misc_files/teams_from_api_log.txt' ,'a+') as log:
            
            teams_from_file = [x.strip('\n') for x in team_file.readlines()]
            
            
        team_file.close()
    with open('/home/pegasus/python_workspace/CBAPP/NCAA_BASKETBALL_PROGRAM/misc_files/teams_from_api_log.txt' ,'a+') as log:
        teams_from_game = []
        for game in games:
            if game is not None and game.period.period_description == 'Game':
                teams_from_game.append(game.participant_one.participant_name)
                teams_from_game.append(game.participant_two.participant_name)
        for sorted_team in sorted(teams_from_game):

            if sorted_team.strip() not in teams_from_file:
                log.write(str(datetime.now()) + ' - ' + 'Writing team to file: ' + sorted_team + '\n')
                picks.append(sorted_team)
            else:
                log.write(str(datetime.now()) + ' - ' + 'Omitting team from file: ' + sorted_team + '\n')
    log.close()
    with open('/home/pegasus/python_workspace/CBAPP/NCAA_BASKETBALL_PROGRAM/misc_files/teams_from_api.txt' ,'a+' ) as team_file:
            for team in picks:
                team_file.write(team + '\n')
    team_file.close()

if __name__ == '__main__':
    main()