import connection_settings

class Team(object):

    find_by_schedule_query = 'SELECT * FROM TEAM t WHERE t.SCHEDULE_NAME = %s'

    def __init__(self):
        self.id = 0
        self.spread_name = ''
        self.schedule_name = ''
        self.wins = 0
        self.losses = 0
        self.ats_wins = 0
        self.ats_losses = 0
	
    def findTeamByScheduleName(self):
        print(str(0))
        if self.schedule_name is not '':
            print(str(1))
            try:
                print(str(2))
                connection = connection_settings.createConnection()
                print(connection)
                with connection.cursor() as cursor:
                    print(self.schedule_name)
                    cursor.execute(self.find_by_schedule_query,(self.schedule_name))
                    result = cursor.fetchone()
                    print(result['TEAM_ID'])
                    return result
            except:
                print('Error in FindTeamByScheduleName')
           # finally:
                #connection.close()
        