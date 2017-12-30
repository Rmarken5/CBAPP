import requests
from livelineentities import *
import parse_html
import datetime
import pymysql.cursors

connSettings = []
connection = None

def main():
    url = 'http://www.ncaa.com/scoreboard/basketball-men/d1'
    date = str(datetime.date.today().year) + '_' + str(datetime.date.today().month) + '_' + str(datetime.date.today().day)
    print(date)
    url = url + date
    r = requests.get(url)
    result = r.text
    lineNum = 0
    games = []
    games = parse_html.findScoreboard(result)
    connSettings = initConnectionSettings()
    try:
        connection = pymysql.connect(host=connSettings['host'],
                                 user=connSettings['user_name'],
                                 password=connSettings['password'],
                                 db=connSettings['db'],
                                 charset=connSettings['charset'],
                                 cursorclass=connSettings['cursorclass'])
        print(str(connection))
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM TEAM'
            output = cursor.execute(sql)
            print(output)
    finally:
        connection.close()	
	
	
#def populateSchduleFromGames():

def initConnectionSettings():
    config = {'user_name':'tester',
        'password':'tester',
        'host': '10.0.0.94',
        'db':'ncaa_basketball_test',
        'charset':'utf8mb4',
        'cursorclass':pymysql.cursors.DictCursor
        }	
    return config


if __name__ == '__main__':
    main()