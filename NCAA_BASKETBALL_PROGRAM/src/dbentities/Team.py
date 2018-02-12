import connection_settings
import sys
class Team(object):

    find_by_schedule_query = 'SELECT * FROM TEAM t WHERE t.SCHEDULE_NAME = %s'
    find_by_spread_query = 'SELECT * FROM TEAM t WHERE t.SPREAD_NAME = %s'
    update_team_query = 'UPDATE TEAM SET SPREAD_NAME = %s, SCHEDULE_NAME = %s, WINS = %s, LOSSES = %s, ATS_WINS = %s, ATS_LOSSES = %s WHERE TEAM_ID = %s'
    insert_team_query = 'INSERT TEAM (SPREAD_NAME, SCHEDULE_NAME, WINS, LOSSES, ATS_WINS, ATS_LOSSES) VALUES (%s, %s, %s, %s, %s, %s)'
    find_by_id = 'SELECT * FROM TEAM WHERE TEAM_ID = %s'

    def __init__(self):
        self.id = 0
        self.spread_name = ''
        self.schedule_name = ''
        self.wins = 0
        self.losses = 0
        self.ats_wins = 0
        self.ats_losses = 0
	
    def equals(self, other):
        
        return (self.id == other.id and
        self.spread_name == other.spread_name and
        self.schedule_name == other.schedule_name and
        self.wins == other.wins and
        self.losses == other.losses and
        self.ats_wins == other.ats_wins and
        self.ats_losses == other.ats_losses)

	
    def findTeamByScheduleName(self):
        try:
            if self.schedule_name is not '':
                
                #TODO - Check if team is in DB.
                connection = connection_settings.createConnection()
                    
                with connection.cursor() as cursor:
                        
                    cursor.execute(self.find_by_schedule_query,(self.schedule_name))
                    result = cursor.fetchone()
                    if result == None:
                        raise RuntimeError('Error in findTeamByScheduleName: \'results\' == None for ' + self.schedule_name)
                       
                    self.createTeamFromResults(result)
        except Exception as e:
            print('Issue in findTeamByScheduleName: ' + str(e))
            pass
        finally:
            connection.close()

    def findTeamBySpreadName(self):
       
        if self.spread_name is not '':
            
            try:
                connection = connection_settings.createConnection()
                
                with connection.cursor() as cursor:

                    cursor.execute(self.find_by_spread_query,(self.spread_name))
                    result = cursor.fetchone()
                    if result == None:
                        raise RuntimeError('Error in findTeamBySpreadName: \'results\' == None for ' + self.spread_name)
                    self.createTeamFromResults(result)
            except Exception as e:
                print('Error in findTeamBySpreadName: ' + str(e))
                pass
            finally:
                connection.close()

    def findTeamById(self):
        connection = None

        try:
            print ('findTeamById: ' + str(self.id))
            if self.id is not None:
                connection = connection_settings.createConnection()
                
                with connection.cursor() as cursor:

                    cursor.execute(self.find_by_id,(self.id))
                    result = cursor.fetchone()
                    print (result)
                    if result == None:
                        raise RuntimeError('Error in findTeamById: \'results\' == None for TEAM_ID:  ' + self.id)
                    self.createTeamFromResults(result)
        
        except Exception as e:
            print('Error in findTeamById: ' + str(e))
            pass
        finally:
                if connection is not None:
                    connection.close()
                

    def updateTeam(self):
        try:
            if self.id is not 0 and self.spread_name is not '' and self.schedule_name is not '':
               
                connection = connection_settings.createConnection()
                    
                with connection.cursor() as cursor:
                        
                    cursor.execute(self.update_team_query,(self.spread_name, self.schedule_name, self.wins, self.losses, self.ats_wins, self.ats_losses, self.id))
                    connection.commit()
                        
                    
        except Exception as e:
            print('Error in findTeamBySpreadName: ' + str(e))
            pass
        finally:
            connection.close()
	
    def insertTeam(self):
        try:
            if ((self.spread_name is not None and self.spread_name is not '') 
		       and (self.schedule_name is not None and self.schedule_name is not '')):

                connection = connection_settings.createConnection()
                
                with connection.cursor() as cursor:
                    
                    cursor.execute(self.insert_team_query, (self.spread_name, self.schedule_name, self.wins, self.losses, self.ats_wins, self.ats_losses, self.id))
                    connection.commit()
        except Exception as e:
            print('Issue in insertTeam: ' + str(e))
            pass
        finally:
            connection.close()
			
    def createTeamFromResults(self, results):
        
        if(results != None):
            self.id = results['TEAM_ID']
            self.spread_name = results['SPREAD_NAME']
            self.schedule_name = results['SCHEDULE_NAME']
            self.wins = results['WINS']
            self.losses = results['LOSSES']
            self.ats_wins = results['ATS_WINS']
            self.ats_losses = results['ATS_LOSSES']
        else:
            raise RuntimeError('Runtime Error: results are type \'None\'')
        
    def printTeam(self):

        print('Team: \n' + 'TEAM_ID: ' + str(self.id) + ' \n' +
        'SPREAD_NAME: ' + str(self.spread_name) + '\n' + 
        'SCHEDULE_NAME: ' + str(self.schedule_name) + '\n' +
        'WINS: ' + str(self.wins) + '\n' + 'LOSSES: ' + str(self.losses) + '\n' +
        'ATS_WINS: ' + str(self.ats_wins) + '\n' + 'ATS_LOSSES: ' + str(self.ats_losses))