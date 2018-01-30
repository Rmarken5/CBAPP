# Python code to map to PICK table
# url = http://livelines.betonline.com/sys/LineXML/LiveLineObjXml.asp?sport=basketball&league=NCAA%20Basketball
# Author - Ryan Marken
# 1/15/2018

import connection_settings
import datetime
from dbentities import Team

class Pick(object):

    select_pick_by_date_home_away = 'SELECT * FROM PICK WHERE GAME_DATE = %s AND HOME_TEAM_ID = %s AND AWAY_TEAM_ID = %s'
    
    update_pick_by_id = 'UPDATE PICK SET PICKED_CORRECTLY = %s WHERE PICK_ID = %s'
    
    select_picks_by_date = 'SELECT * FROM PICK WHERE GAME_DATE = %s'

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
                    
                    cursor.execute(self.select_pick_by_date_home_away, (self.game_date, self.home_team.id, self.away_team.id))
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
                    
                    cursor.execute(self.update_pick_by_id, (self.picked_correctly, self.pick_id))
                    connection.commit()
                    
                    print('Update pick complete... picked correctly: ' +  self.favorite_team.spread_name )

        except Exception as e:
            print('Issue in updatePick(): ' + str(e))
        finally:
            connection.close()
            
    def getPicksByDate(self, date):
        connectio = None
        picks = []
        try:
            print(date)
            connection = connection_settings.createConnection()
            if connection is not None and date is not None:

                with connection.cursor() as cursor:
                    
                    cursor.execute(self.select_picks_by_date, (date))
                    results = cursor.fetchall()
                    
                    return results
                

        except Exception as e:
            print('Issue in getPicksByDate(): ' + str(e))
        finally:
            if connection is not None:
                connection.close()

    def createPickFromDictionary(self, dictionaryEntry):
        if dictionaryEntry is not None:
            print (dictionaryEntry)
            self.pick_id = dictionaryEntry['PICK_ID']
            self.game_date = dictionaryEntry['GAME_DATE']
            self.game_time = dictionaryEntry['GAME_TIME']
            if dictionaryEntry['HOME_TEAM_ID'] is not None:
                _home_team = Team.Team()
                _home_team.id = dictionaryEntry['HOME_TEAM_ID']
                _home_team.findTeamById()
                print ('dictEntry: ' + str(dictionaryEntry['HOME_TEAM_ID']))
                print('createPickFromDictionary Name :  ' + _home_team.spread_name)
                self.home_team = _home_team
            self.spread = dictionaryEntry['SPREAD']
            if dictionaryEntry['AWAY_TEAM_ID'] is not None: 
                _away_team = Team.Team()
                _away_team.id = dictionaryEntry['AWAY_TEAM_ID']
                _away_team.findTeamById()
                self.away_team = _away_team
            if dictionaryEntry['FAVORITE_TEAM_ID'] is not None: 
                _favorite_team = Team.Team()
                _favorite_team.id = dictionaryEntry['FAVORITE_TEAM_ID']
                _favorite_team.findTeamById()
                self.favorite_team = _favorite_team
            self.picked_correctly = dictionaryEntry['PICKED_CORRECTLY']





#TODO - Create select and update methods
        
        