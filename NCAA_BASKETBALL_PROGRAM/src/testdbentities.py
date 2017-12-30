from dbentities import Team
from dbentities import Schedule
import pymysql.cursors

x = Team.Team()
x.id = 1
x.schedule_name = 'Baylor'
y = Schedule.Schedule()


print(x.findTeamByScheduleName())
