import requests
from livelineentities import *
import parse_html
import datetime
import pymysql.cursors

connSettings = []
connection = None

def main():
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
    games = parse_html.getAllGames(result,datetime.date.today())
	
    for game in games:
        
        game.insertSchedule()
   
	
	
#def populateSchduleFromGames():



if __name__ == '__main__':
    main()