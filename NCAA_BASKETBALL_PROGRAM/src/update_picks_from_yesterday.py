from dbentities import Pick
from datetime import datetime, timedelta

# Update yesterday's picks
# 1) Get all picks based on yesterday's date.
# 2) Get both teams based on ID
# 3) Get schedule based on team ids, game date.
# 5) Update both teams ats record.
# 4) Check the score from schedule against the spread to see who if the pick was correct.
def main():
	
    today = datetime.today()
    yesterday = today - timedelta(days = 1)
    picks_from_yesterday = []
    picks_from_yesterday = getPicksByDate(yesterday)
    print (picks_from_yesterday)
	
def getPicksByDate(date):
	picks = None
	if date is not None:
		picks = Pick.Pick().getPicksByDate(date)
	return picks

	
	
	
	
	
if __name__ == '__main__':
	main()