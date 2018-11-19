import requests
import io
from livelineentities import *
import datetime
from dbentities import Schedule
from dbentities import Team
from cbapputil import date_time_util as dtu

#outfile.write(line)
url = 'http://www.ncaa.com/scoreboard/basketball-men/d1'
#pathlib.Path('./output-files').mkdir(parents=True, exist_ok=True) 
#outfile = open('./output-files/html-by-line.txt','w+')
r = requests.get(url)
result = r.text
lineNum = 0
games = []
participants = []
date = datetime.date.today()
#print(date)

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def findScoreboard(html):
    #print('findScoreboard is called: ' + html)
    lines = html.split('\n')
    if len(lines) < 1:
        print 'No lines from html' 
    section_occurances = 0
    write_flag = False
    output = ''
    for line in lines:
        #print line
        if write_flag == True and '<div' in line:
            #print('Write flag true ', 'Section found.' )
            section_occurances = section_occurances + 1
        if write_flag == True and '</div>' in line:
            #print('Write flag true ', '/Section found.' )
            section_occurances = section_occurances - 1
            if section_occurances <= 0:
                write_flag = False
        if '<div id="scoreboardContent" class="layout--content-left">' in line:
            #print('Write flag set to true ', 'Section id = scoreboard.' )
            write_flag = True
            section_occurances = section_occurances + 1
        if write_flag == True:
            
            output = output + line + '\n'
    return output

def getGamesFromBoard(html):
    scoreboard = findScoreboard(html)
    lines = scoreboard.split('\n')
    if len(lines) < 1:
        print 'No Lines from board'
    section_occurances = 0
    write_flag = False
    output = []
    holder = ''
    for line in lines:
        if write_flag == True and '<div' in line:
            section_occurances = section_occurances + 1  
        if write_flag == True and '</div>' in line:
          # print('write flag true end of section')
            section_occurances = section_occurances - 1
            holder = holder + line + '\n'
            if section_occurances <= 0:
               write_flag = False
               #print(holder)
               output.append(holder)
        if '<div class="gamePod gamePod-type-game' in line:
            holder = ''
            section_occurances = section_occurances + 1
            write_flag = True
        if write_flag == True:
            holder = holder + line + '\n'
    return output
    
def getTeamOneFromGame(game):
    
    lines = game.split('\n')
    for line in lines:
        # print line
        # print '------------------'
        if '<span class="gamePod-game-team-name">' in line:
            team = find_between(line,'<span class="gamePod-game-team-name">','</span>')
            team = team.strip()
            participant = Participant()
            participant.participant_name = team
            return participant
def getTeamTwoFromGame(game):
    
    count = 0
    lines = game.split('\n')
    for line in lines:
        # print line
        # print '------------------'
        if '<span class="gamePod-game-team-name">' in line:
            count = count + 1
            if count == 2:
                team = find_between(line,'<span class="gamePod-game-team-name">','</span>')
                team = team.strip()
                participant = Participant()
                participant.participant_name = team
                return participant

def getTimeForGame(game):
    time = None
    lines = game.split('/n')
    for line in lines:
        
        if '<span class="game-time">' in line:
            
            time = find_between(line, '<span class="game-time">', '</span>')
            
            # o = datetime.datetime.strptime(time, '%-I:%M %p')
            print(time)
            if(time == None):
                print('Time for ' + game + ' is returning \'None\'. ')
            return time

def getScores(game):
    i = 0
    scores = []
    sections = game.split('<li class=')
    away_section = sections[1]
    home_section = sections[2]
    score = find_between(away_section,'<span class="gamePod-game-team-score">', '</span>')
    print 'away score: ' + score
    scores.append(score)
    score = find_between(home_section,'<span class="gamePod-game-team-score">', '</span>')
    print 'home score: ' + score
    scores.append(score)
    return scores
            
def getDateFromDateTime(input):
    date = None

    if input != None and input != '':
        datesplit = input.split(' ')
        if datesplit is not None and len(datesplit) > 1:
            date = datesplit[0]
    return date

def getTimeFromDateTime(input):
    time = None

    if input != None and input != '':
        datesplit = input.split(' ')
        if datesplit is not None and len(datesplit) > 1:
            time = datesplit[1]
    return time 
        
def openFile():
   cur_dir = os.path.dirname(__file__)
   print(cur_dir)
   if not os.path.exists(cur_dir + '/' + 'output-files'):
       os.makedirs(cur_dir+'/'+'output-files')
   rel_dir_file = os.path.join(cur_dir, 'output-files/teams_from_html.txt')
   print(rel_dir_file)
   return open(rel_dir_file,"w")


def getAllGames(html,date):
    
    games = getGamesFromBoard(html)
    scheduleArr = []
     
    for game in games:
        schedule = Schedule.Schedule()
        away_team = Team.Team()
        home_team = Team.Team()
        time = getTimeForGame(game)
        if isinstance(date,str):
            date = dtu.getTimeObjFromDTStringAMPM(date)
        elif not isinstance(date, datetime.date):           
            raise Exception('date is not a date object or cannot be converted as one.')
        #time = getTimeFromDateTime(time)
        if time is not None:
            time = dtu.getTimeObjFromDTString(time)
        away_participant = getTeamOneFromGame(game)
        home_participant = getTeamTwoFromGame(game)
        if (away_participant is not None and home_participant is not None
        and date is not None):
            away_team.schedule_name = away_participant.participant_name
            home_team.schedule_name = home_participant.participant_name
            away_team.findTeamByScheduleName()

            home_team.findTeamByScheduleName()
            
            
            if away_team.id is not 0 and home_team.id is not 0:
                scores = []
                scores = getScores(game)

                if len(scores) > 1:
                    away_score = scores[0]
                    home_score = scores[1]
                    schedule.home_team_score = home_score
                    schedule.away_team_score = away_score
                    if home_score is not '' and away_score is not '':
                        if int(home_score) > int(away_score):
                            schedule.winning_team = home_team
                            schedule.losing_team = away_team
                        else:
                            schedule.losing_team = home_team
                            schedule.winning_team = away_team
                schedule.home_team = home_team
                schedule.away_team = away_team
                schedule.game_date = date
                schedule.game_time = time
                print('home team: ' + schedule.home_team.schedule_name + ', away team: ' + schedule.away_team.schedule_name )
                print('date: ' + datetime.datetime.strftime(schedule.game_date, '%Y/%m/%d'))
                if time is not None:
                    print(' time: ' + datetime.time.strftime(schedule.game_time,'%H:%M' ))
                
                scheduleArr.append(schedule)
    return scheduleArr
        
#scoreboard = findScoreBoard(result)

#games = getGamesFromBoard(scoreboard)


#for game in games:

#   participants.extend(getTeamsFromGame(game))
#for participant in participants:
#   print(participant.participant_name)
#    outfile.write(participant.participant_name +'\n')