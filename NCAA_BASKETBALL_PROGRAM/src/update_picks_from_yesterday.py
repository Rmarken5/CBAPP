from dbentities import Pick, Schedule
from datetime import datetime, timedelta
import math

# Update yesterday's picks
# 1) Get all picks based on yesterday's date.
# 2) Get both teams based on ID
# 3) Get schedule based on team ids, game date.
# 5) Update both teams ats record.
# 4) Check the score from schedule against the spread to see who if the pick was correct.
def main():
    
    today = datetime.today()
    yesterday = today - timedelta(days = 1)
    
    print(datetime.strftime(yesterday.date(), '%Y-%d-%m'))
    yesterday = yesterday.date()
    picks_from_yesterday = []
    picks_from_yesterday = getPicksByDate(yesterday)
    for dictEntry in picks_from_yesterday:
        home_score = None
        away_score = None
        home_team = None
        away_team = None
        favorite_team = None
        spread = None
        pick = Pick.Pick()
        pick.createPickFromDictionary(dictEntry)
        print ('Pick Spread Team Name: ' + pick.home_team.spread_name) 
        if pick is not None:
            spread = pick.spread
            schedule = Schedule.Schedule()
            schedule.game_date = pick.game_date
            schedule.home_team = pick.home_team
            schedule.away_team = pick.away_team
            schedule.findScheduleByDateTeams()
            home_team = pick.home_team
            away_team = pick.away_team
            favorite_team = pick.favorite_team
            if schedule is not None:
                home_score = schedule.home_team_score
                away_score = schedule.away_team_score
                difference = home_score - away_score
                if spread > 0: #Away Team is favored
                    if difference > 0 or math.fabs(difference) < spread: #Home team won outright or away team didn't cover spread.

                        home_team.ats_wins += 1
                        away_team.ats_losses += 1
                        if favorite_team.id == home_team.id:
                            pick.picked_correctly = True
                        else:
                            pick.picked_correctly = False
                    else:
                        if favorite_team.id == away_team.id:
                            pick.picked_correctly = True
                        else:
                            pick.picked_correctly = False
                        away_team.ats_wins += 1
                        home_team.ats_losses += 1
                else: #Home team is favored
                    if difference < 0 or difference < math.fabs(spread):  #Away Team won outright or home team didn't cover the spread.

                        away_team.ats_wins += 1
                        home_team.ats_losses += 1

                        if favorite_team.id == away_team.id:
                            pick.picked_correctly = True
                        else:
                            pick.picked_correctly = False
                        away_team.ats_wins += 1
                        home_team.ats_losses += 1
                    else:
                        home_team.ats_wins += 1
                        away_team.ats_losses += 1

                        if favorite_team.id == home_team.id:
                            pick.picked_correctly = True
                        else:
                            pick.picked_correctly = False
            home_team.updateTeam()
            away_team.updateTeam()
            pick.updatePick()                       




    
def getPicksByDate(date):
    picks = None
    if date is not None:
        picks = Pick.Pick().getPicksByDate(date)
    return picks

    
    
    
    
    
if __name__ == '__main__':
    main()