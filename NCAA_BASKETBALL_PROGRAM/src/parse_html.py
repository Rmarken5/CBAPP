import requests
import io
from livelineentities import *
import datetime
from dbentities import Schedule
from dbentities import Team

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
print(date)

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def findScoreboard(html):
    lines = html.split('\n')
    section_occurances = 0
    write_flag = False
    output = ''
    for line in lines:
        if write_flag == True and '<section' in line:
            print('Write flag true ', 'Section found.' )
            section_occurances = section_occurances + 1
        if write_flag == True and '</section>' in line:
            print('Write flag true ', '/Section found.' )
            section_occurances = section_occurances - 1
            if section_occurances <= 0:
                write_flag = False
        if '<section id="scoreboard">' in line:
            print('Write flag set to true ', 'Section id = scoreboard.' )
            write_flag = True
            section_occurances = section_occurances + 1
        if write_flag == True:
            print('printing line')
            output = output + line + '\n'
    return output

def getGamesFromBoard(html):
    scoreboard = findScoreboard(html)
    lines = scoreboard.split('\n')
    section_occurances = 0
    write_flag = False
    output = []
    holder = ''
    for line in lines:
        if write_flag == True and '</section>' in line:
           print('write flag true end of section')
           section_occurances = section_occurances -1
           holder = holder + line + '\n'
           if section_occurances <= 0:
               write_flag = False
               print(holder)
               output.append(holder)
        if '<section class="game' in line:
            holder = ''
            section_occurances = section_occurances + 1
            write_flag = True
        if write_flag == True:
            holder = holder + line + '\n'
    return output
	
def getTeamsFromGame(game):
    output = []
    lines = game.split('/n')
    for line in lines:
        if '<h3>' in line:
            teams = find_between(line,'<h3>','</h3>')
            teams = teams.split('vs')
            for team in teams:
                team = team.strip()
                participant = Participant()
                participant.participant_name = team
                print(participant.participant_name)
                output.append(participant)
    return output

def getTimeFromGame(game):
    lines = game.split('/n')
    for line in lines:
        if '<div class="game-status pre ">' in line:
            time = find_between(line, '<div class="game-status pre ">', '</div>')
            return time
		
def openFile():
   cur_dir = os.path.dirname(__file__)
   print(cur_dir)
   if not os.path.exists(cur_dir + '/' + 'output-files'):
       os.makedirs(cur_dir+'/'+'output-files')
   rel_dir_file = os.path.join(cur_dir, 'output-files/teams_from_html.txt')
   print(rel_dir_file)
   return open(rel_dir_file,"w")

def parseGamesToObjects(game):
    participants = getTeamsFromGame(game)
	game_time = getTimeFromGame(game)
	
    
         	

#scoreboard = findScoreBoard(result)

#games = getGamesFromBoard(scoreboard)


#for game in games:

#   participants.extend(getTeamsFromGame(game))
#for participant in participants:
#   print(participant.participant_name)
#    outfile.write(participant.participant_name +'\n')