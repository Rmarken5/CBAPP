from dbentities import Team
import connection_settings
import datetime

class Schedule(object):

    insert_schedule_sql = 'INSERT INTO SCHEDULE (GAME_DATE, GAME_TIME, HOME_TEAM_ID, AWAY_TEAM_ID, HOME_TEAM_SCORE, AWAY_TEAM_SCORE, WINNING_TEAM_ID, LOSING_TEAM_ID) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
    insert_initial_schedule_sql = 'INSERT INTO SCHEDULE (GAME_DATE, GAME_TIME, HOME_TEAM_ID, AWAY_TEAM_ID) VALUES(%s, %s, %s, %s)'
	
    def __init__(self):
        self.schedule_id = 0
        self.game_date = None
        self.game_time = None
        self.home_team = None
        self.away_team = None
        self.home_team_score = 0
        self.away_team_score = 0
        self.winning_team = None
        self.lossing_team = None

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
        if(self.lossing_team != None and other.lossing_team != None):
            if not(self.lossing_team.equals(other.lossing_team)):
                return False
        elif(self.lossing_team != None and other.lossing_team == None):
            return False
        elif(self.lossing_team == None and other.lossing_team != None):
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
        # 'lossing_team: ' + str(self.lossing_team.printTeam()) +' ]')



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
			
		
        except Exception as e:
            print('Issue in insertSchedule: \n' + str(e) + '\n' + 'home team schedule name: ' + self.home_team.schedule_name)
        finally:
            connection.close()
		
		