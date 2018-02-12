import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from dbentities import Pick
import connection_settings


pick_query = 'SELECT p.GAME_DATE, p.GAME_TIME, ht.SCHEDULE_NAME as \'HOME_TEAM\', p.SPREAD, awt.SCHEDULE_NAME as \'AWAY_TEAM\', ft.SCHEDULE_NAME as \'FAVORITE\'  FROM PICK p INNER JOIN TEAM ht ON p.HOME_TEAM_ID = ht.TEAM_ID INNER JOIN TEAM awt ON p.AWAY_TEAM_ID = awt.TEAM_ID INNER JOIN TEAM ft ON p.FAVORITE_TEAM_ID = ft.TEAM_ID WHERE p.GAME_DATE = %s'


def main():
	fromaddr = "send.markenapps@gmail.com"
	toaddr = "marken.ryan@gmail.com"
	today = datetime.today().date()
	print(datetime.strftime(today, '%Y-%d-%m'))
	msg = MIMEMultipart('alternative')
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = 'NCAA Basketball Lines ' + datetime.strftime(today, '%Y-%d-%m')
	html = '<html><head></head><body><table>'
	th = '<th><tr><td>GAME_DATE</td><td>GAME_TIME</td><td>HOME_TEAM</td><td>SPREAD</td><td>AWAY_TEAM</td><td>FAVORITE</td></tr></th>'
	html += th
	end_html = '</table></body></html>'
	picks = getPicks(today)
	for pick in picks:
		html += '<tr>'
		row = '<td>' + datetime.strftime(pick['GAME_DATE'], '%Y-%d-%m')  + '</td>' + '<td>' +str( pick['GAME_TIME']) + '</td>' + '<td>' + pick['HOME_TEAM'] + '</td>' + '<td>' + str(pick['SPREAD']) + '</td>' + '<td>' + pick['AWAY_TEAM'] + '</td>'  + '<td>' + pick['FAVORITE'] + '</td>' 
		html += row + '</tr>'
	html += end_html
	body = html
	msg.attach(MIMEText(body, 'html'))
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

def getPicks(date):

	try:
		coonnection = connection_settings.createConnection()

		with coonnection.cursor() as cursor:
			cursor.execute(pick_query,(date))
			picks = cursor.fetchall()
			print(picks)
			return picks
	except Exception as e:
		print (str(e))

if __name__ =='__main__':
	main()