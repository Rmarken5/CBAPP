from datetime import datetime, timedelta
import requests
import parse_html

def main():
    today = datetime.today()
    yesterday = today - timedelta(days = 1)
    print(datetime.strftime(yesterday, '%Y/%m/%d'))
    url = 'http://www.ncaa.com/scoreboard/basketball-men/d1' +'/' + datetime.strftime(yesterday, '%Y/%m/%d')
    print(url)
    r = requests.get(url)
    results = r.text
    games = []
    games = parse_html.getAllGames(results,yesterday)
    print(games)
    for game in games:
    	print (game)

if __name__ == '__main__':
	main()