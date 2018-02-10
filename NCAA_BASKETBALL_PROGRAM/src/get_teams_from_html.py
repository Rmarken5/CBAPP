import requests
from livelineentities import *
import parse_html
import datetime
import pymysql.cursors
from cbapputil import date_time_util as dtu
from dbentities import *

connSettings = []
connection = None

def main():
    f = openFile()
    teams_from_file = getTeamsFromFile(f)

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
    lineNum = 0
    games = []
    games = getAllGames(result,datetime.date.today())
    teams = []
    for game in games:
        teams.append(game.home_team.schedule_name)
        teams.append(game.away_team.schedule_name)
    for team in sorted(teams):
        if team not in teams_from_file:
            f.write(team + '\n')
    f.close()


def getAllGames(html,date):
    
    games = parse_html.getGamesFromBoard(html)
    scheduleArr = []
    
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
        participants = []
        participants.extend(parse_html.getTeamsFromGame(game))
        if (participants is not None and len(participants) == 2 
        and date is not None):
            away_participant = participants[0]
            home_participant = participants[1]
            away_team.schedule_name = away_participant.participant_name
            home_team.schedule_name = home_participant.participant_name
            schedule.home_team = home_team
            schedule.away_team = away_team
            schedule.game_date = date
            schedule.game_time = time
            scheduleArr.append(schedule)
    return scheduleArr

def openFile():
    f = open('C:/Users/Ryan/Documents/Python_Workspace/CBAPP/NCAA_BASKETBALL_PROGRAM/misc_files/teams_from_html.txt' ,'a+' )
    return f

def getTeamsFromFile(file):
    teams = []
    fl = file.readlines()

    for l in fl:
        teams.appen(l)
    return teams

if __name__ == '__main__':
    main()