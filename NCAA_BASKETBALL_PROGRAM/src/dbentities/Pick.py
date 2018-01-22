# Python code to map to PICK table
# url = http://livelines.betonline.com/sys/LineXML/LiveLineObjXml.asp?sport=basketball&league=NCAA%20Basketball
# Author - Ryan Marken
# 1/15/2018

import connection_settings
import datetime

class Pick(object):

    select_pick_by_date_home_away = 'SELECT * FROM PICK WHERE GAME_DATE = %s AND HOME_TEAM_ID = %s AND AWAY_TEAM_ID = %s'
    
    update_pick_by_id = 'UPDATE PICK SET PICKED_CORRECTLY = %s WHERE PICK_ID = %s'

    def __init__(self):
        self.pick_id = 0
        self.game_date = None
        self.game_time = None
        self.home_team = None
        self.spread = 0.0
        self.away_team = None
        self.favorite_team = None
        self.picked_correctly = None


    def insertPick(self):
        insert_pick_query = 'INSERT PICK (GAME_DATE, GAME_TIME, HOME_TEAM_ID, SPREAD, AWAY_TEAM_ID, FAVORITE_TEAM_ID) VALUES (%s, %s, %s, %s, %s, %s)'
        try:
            connection = connection_settings.createConnection()
            print(self.spread)
            if connection is not None and self.game_date is not None \
            and self.game_time is not None and self.home_team is not None \
            and self.away_team is not None and self.favorite_team is not None:

                with connection.cursor() as cursor:
                    
                    cursor.execute(insert_pick_query, (self.game_date, self.game_time, self.home_team.id, self.spread, self.away_team.id, self.favorite_team.id))
                    connection.commit()
					
                    print('Insert into pick complete: date: ' + datetime.datetime.strftime(self.game_date,'%Y/%m/%d') + '. Home team: ' \
                    + self.home_team.spread_name + '. Away team: ' + self.away_team.spread_name )

        except Exception as e:
            print('Issue in insertPick(): ' + str(e))
        finally:
            connection.close()


    def selectPick(self):
        try:
            connection = connection_settings.createConnection()
            if connection is not None and self.game_date is not None \
            and self.home_team is not None \
            and self.away_team is not None:

                with connection.cursor() as cursor:
                    
                    cursor.execute(select_pick_by_date_home_away, (self.game_date, self.home_team.id, self.away_team.id))
                    connection.commit()
					
                    print('Select pick complete: date: ' + datetime.datetime.strftime(self.game_date,'%Y/%m/%d') + ' time: ' + datetime.time.strftime(self.game_time, '%H:%M') + '. Home team: ' \
                    + self.home_team.spread_name + '. Spread: ' + str(self.spread) +'. Away team: ' + self.away_team.spread_name + 'Favorite team: ' + self.favorite_team.spread_name )

        except Exception as e:
            print('Issue in selectPick(): ' + str(e))
        finally:
            connection.close()

    def updatePick(self):
        try:
            connection = connection_settings.createConnection()
            if connection is not None and self.game_date is not None \
            and self.home_team is not None \
            and self.away_team is not None:

                with connection.cursor() as cursor:
                    
                    cursor.execute(update_pick_by_id, (self.picked_correctly, self.pick_id))
                    connection.commit()
					
                    print('Update pick complete... picked correctly: ' +  self.favorite_team.spread_name )

        except Exception as e:
            print('Issue in updatePick(): ' + str(e))
        finally:
            connection.close()
#TODO - Create select and update methods
        
        