from dbentities import Team
import connection_settings
import datetime

class Schedule(object):

    insert_schedule_sql = 'INSERT INTO SCHEDULE (GAME_DATE, GAME_TIME, HOME_TEAM_ID, AWAY_TEAM_ID, HOME_TEAM_SCORE, AWAY_TEAM_SCORE, WINNING_TEAM_ID, LOSING_TEAM_ID) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
    insert_initial_schedule_sql = 'INSERT INTO SCHEDULE (GAME_DATE, GAME_TIME, HOME_TEAM_ID, AWAY_TEAM_ID) VALUES(%s, %s, %s, %s)'
    update_schedule_sql = 'UPDATE SCHEDULE SET HOME_TEAM_SCORE = %s, AWAY_TEAM_SCORE = %s, WINNING_TEAM_ID = %s, LOSING_TEAM_ID = %s WHERE HOME_TEAM_ID = %s AND AWAY_TEAM_ID = %s AND GAME_DATE = %s'
    find_schedule_date_teams = 'SELECT * FROM SCHEDULE WHERE GAME_DATE = %s AND HOME_TEAM_ID = %s AND AWAY_TEAM_ID = %s'


    def __init__(self):
        self.schedule_id = 0
        self.game_date = None
        self.game_time = None
        self.home_team = None
        self.away_team = None
        self.home_team_score = 0
        self.away_team_score = 0
        self.winning_team = None
        self.losing_team = None

    def equals(self, other):
        if (self.schedule_id != other.schedule_id):
            return False
        if(self.game_date != None and other.game_date != None):
            if(self.game_date != other.game_date):
                return False
        elif(self.game_date != None and other.game_date == None):
            return False
        elif(self.game_date == None and other.game_date != None):
            return False
        if(self.game_time != None and other.game_time != None):
            if(self.game_time != other.game_time):
                return False
        elif(self.game_time != None and other.game_time == None):
            return False
        elif(self.game_time == None and other.game_time != None):
            return False
        if(self.home_team != None and other.home_team != None):
            if not(self.home_team.equals(other.home_team)):
                return False
        elif(self.home_team != None and other.home_team == None):
            return False
        elif(self.home_team == None and other.home_team != None):
            return False
        if(self.away_team != None and other.away_team != None):
            if not(self.away_team.equals(other.away_team)):
                return False
        elif(self.away_team != None and other.away_team == None):
            return False
        elif(self.away_team == None and other.away_team != None):
            return False        
        if(self.home_team_score != other.home_team_score):
            return False
        if(self.away_team_score != other.away_team_score):
            return False        
        if(self.winning_team != None and other.winning_team != None):
            if not(self.winning_team.equals(other.winning_team)):
                return False
        elif(self.winning_team != None and other.winning_team == None):
            return False
        elif(self.winning_team == None and other.winning_team != None):
            return False
        if(self.losing_team != None and other.losing_team != None):
            if not(self.losing_team.equals(other.losing_team)):
                return False
        elif(self.losing_team != None and other.losing_team == None):
            return False
        elif(self.losing_team == None and other.losing_team != None):
            return False
        return True
    
    # def printSchedule(self):
        # print('Schedule: \n: ' + '[' +
        # 'schedule_id: ' + str(self.schedule_id) + '\n' +
        # 'game_time: ' + str(self.game_date) + '\n' +
        # 'game_time: ' + str(self.game_time) + '\n' +
        # 'home_team: ' + str(self.home_team.printTeam()) + '\n' +
        # 'away_team: ' + str(self.away_team.printTeam()) + '\n' +
        # 'home_team: ' + str(self.home_team_score) + '\n' +
        # 'away_team_score: ' + str(self.away_team_score) + '\n' +
        # 'winning_team: ' + str(self.winning_team.printTeam()) + '\n' +
        # 'losing_team: ' + str(self.losing_team.printTeam()) +' ]')



    def insertSchedule(self):
    
        try:
            if self.game_date != None \
            and self.game_time != None \
            and self.home_team != None \
            and self.away_team != None:
               connection = connection_settings.createConnection();

               with connection.cursor() as cursor:
                   cursor.execute(self.insert_initial_schedule_sql,(self.game_date, self.game_time,self.home_team.id, self.away_team.id) )
                   connection.commit()
                   print('game inserted into schedule table: ' + self.away_team.schedule_name + ' @ ' + self.home_team.schedule_name + ' ' + datetime.datetime.strftime(self.game_date, '%Y/%m/%d') + ' ' + datetime.time.strftime(self.game_time,'%H:%M')  )
                   connection.close()
        
        except Exception as e:
            print('Issue in insertSchedule: \n' + str(e) + '\n' + 'home team schedule name: ' + self.home_team.schedule_name)
        
            
        
    def updateSchedule(self):
        
        try:
            
            if self.game_date != None \
            and self.home_team != None \
            and self.away_team != None:
               
                connection = connection_settings.createConnection();

                with connection.cursor() as cursor:
                    
                    cursor.execute(self.update_schedule_sql,(self.home_team_score, self.away_team_score, self.winning_team.id, self.losing_team.id, self.home_team.id, self.away_team.id, self.game_date.date()) )
                    connection.commit()
                    print(cursor._last_executed)
                    #print('game updated for schedule table: ' + self.away_team.schedule_name + ' @ ' + self.home_team.schedule_name + ' ' + datetime.datetime.strftime(self.game_date, '%Y/%m/%d')  + str(self.winning_team.id) + str(self.losing_team.id) )
                    connection.close()
            
            
        except Exception as e:
            print('Issue in updateSchedule: \n' + str(e) + '\n' + 'home team schedule name: ' + self.home_team.schedule_name)
        
            

    def findScheduleByDateTeams(self):

        try:
            
            if self.game_date != None \
            and self.home_team != None \
            and self.away_team != None:
            
                connection = connection_settings.createConnection();

                with connection.cursor() as cursor:
                    cursor.execute(self.find_schedule_date_teams,(self.game_date, self.home_team.id, self.away_team.id))
                    result = cursor.fetchone()
                    if result == None:
                        raise RuntimeError('Error in findScheduleByDateTeams: \'results\' == None for HOME_TEAM_ID: ' + str(self.home_team.id) + '. AWAY_TEAM_ID: ' + str(self.away_team.id) + '. GAME_DATE: ' + datetime.datetime.strftime(self.game_date, '%Y/%m/%d'))
                    
                    print('game updated for schedule table: ' + self.away_team.schedule_name + ' @ ' + self.home_team.schedule_name + ' ' + datetime.datetime.strftime(self.game_date, '%Y/%m/%d'))

            
            
        except Exception as e:
            print('Issue in findScheduleByDateTeams: \n' + str(e) + '\n' + 'home team schedule name: ' + self.home_team.schedule_name)
        finally:
            if connection is not None:
                connection.close()

    def createScheduleFromDict(self, dict):
        if dict is not None:

            self.schedule_id = dict['SCHEDULE_ID']
            self.game_date = dict['GAME_DATE']
            self.game_time = dict['GAME_TIME']
            if dict['HOME_TEAM_ID'] is not None:
                _home_team = Team.Team()
                _home_team.id = dict['HOME_TEAM_ID']
                _home_team.findTeamById()
                self.home_team = _home_team
            if dict['AWAY_TEAM_ID'] is not None: 
                _away_team = Team.Team()
                _away_team.id = dict['AWAY_TEAM_ID']
                _away_team.findTeamById()
                self.away_team = _away_team
            if dict['HOME_TEAM_SCORE'] is not None:
                self.home_team_score = dict['HOME_TEAM_SCORE']
            if dict['AWAY_TEAM_SCORE'] is not None:
                self.away_team_score = dict['AWAY_TEAM_SCORE']
            if dict['WINNING_TEAM_ID'] is not None:     
                _winning_team = Team.Team()
                _winning_team.id = dict['WINNING_TEAM_ID']
                _winning_team.findTeamById()
                self.winning_team = _winning_team
            if dict['LOSING_TEAM_ID'] is not None:     
                _losing_team = Team.Team()
                _losing_team.id = dict['LOSING_TEAM_ID']
                _losing_team.findTeamById()
                self.losing_team = _losing_team