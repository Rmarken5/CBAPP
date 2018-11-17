import requests
from livelineentities import *
import parse_html
import datetime
import pymysql.cursors
from cbapputil import date_time_util as dtu
from dbentities import *
import os.path

connSettings = []
connection = None

def main():
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    url = 'http://www.ncaa.com/scoreboard/basketball-men/d1'
    year = str(datetime.date.today().year)
    if(datetime.date.today().month < 10):
        month = '0' + str(datetime.date.today().month)
    else:
        month = str(datetime.date.today().month)
    if(datetime.date.today().day < 10):
        day = '0' + str(datetime.date.today().day)
    else:
        day = str(datetime.date.today().day)
    date = str(year) + '/' + str(month) + '/' + str(day)
    print('Running populate_schedule for date: ' + date)
    url = url + '/' + date
    r = requests.get(url)
    result = r.text
    games = getAllGames(result,datetime.date.today())
    teams = []
    teams_to_write = []
    for game in games:
        teams.append(game.home_team.schedule_name)
        teams.append(game.away_team.schedule_name)
    teams_from_file = []
    if os.path.isfile(os.path.join(file_dir,'../misc_files/teams_from_html.txt')):
        with open(os.path.join(file_dir,'../misc_files/teams_from_html.txt') ,'r+' ) as team_file:
             teams_from_file = [x.strip('\n') for x in team_file.readlines()]
        team_file.close()

    with open(os.path.join(file_dir,'../misc_files/teams_from_html_log.txt') ,'a+' ) as log:
        for team in sorted(teams):
            if team not in teams_from_file:
                teams_to_write.append(team)
            else:
                log.write(str(datetime.datetime.now()) + ' - ' + 'Ommiting, team already in file: ' + team + '\n' )
        for team in teams_to_write:
            log.write(str(datetime.datetime.now()) + ' - ' + 'Writing team to file: ' + team  + '\n')
        log.close()

    with open(os.path.join(file_dir,'../misc_files/teams_from_html.txt') ,'a+' ) as team_file:
        for team in teams_to_write:
            team_file.write(team + '\n')
    team_file.close()



def getAllGames(html,date):
    
    games = parse_html.getGamesFromBoard(html)
    scheduleArr = []
    
    if len(games) < 1:
        print 'No Games'

    for game in games:
        schedule = Schedule.Schedule()
        away_team = Team.Team()
        home_team = Team.Team()
        time = parse_html.getTimeForGame(game)
        if isinstance(date,str):
            date = dtu.getTimeObjectFromString(date)
        elif not isinstance(date, datetime.date):           
            raise Exception('date is not a date object or cannot be converted as one.')
        #time = getTimeFromDateTime(time)
        if time is not None:
            time = dtu.getTimeObjectFromString(time)
        away_participant = parse_html.getTeamOneFromGame(game)
        home_participant = parse_html.getTeamTwoFromGame(game)
        if (away_participant is not None and home_participant is not None
        and date is not None):
            print away_participant.participant_name
            print 'at'
            print home_participant.participant_name
            away_team.schedule_name = away_participant.participant_name
            home_team.schedule_name = home_participant.participant_name
            schedule.home_team = home_team
            schedule.away_team = away_team
            schedule.game_date = date
            schedule.game_time = time
            scheduleArr.append(schedule)
    return scheduleArr

def openFile():
    f = open('/home/pegaus/programming/python/CBAPP/NCAA_BASKETBALL_PROGRAM/misc_files/teams_from_html.txt' ,'a+' )
    return f

def getTeamsFromFile(file):
    teams = []
    fl = file.readlines()

    for l in fl:
        teams.appen(l)
    return teams

if __name__ == '__main__':
    main()