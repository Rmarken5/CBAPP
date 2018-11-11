import requests
import io
import datetime 
from livelineentities import *
from cbapputil import date_time_util as dtu

current_year = datetime.datetime.now().year

def findTable(html):
    table = ''
    i = 0
    if html == None:
        print('No HTML to Parse')
    document_lines = html.split('\n')
    for line in document_lines:

        if '<table cellpadding=2 class=frodds-data-tbl>' in line:
            i+=1
        if i > 0:
            table = table + line + '\n'
            if '</table>' in line:
                i-=1
            elif '<table' in line:
                i+=1
    
    return table

def getRowsFromTable(_table):

    rows = []
    flag = False
    row = ''
    if _table == None:
        print 'No table to parse'
    table_lines = _table.split('\n')

    for line in table_lines:
        if '<tr' in line:
            flag = True
        if flag == True:
            row = row + line
        if '</tr>' in line:
            row = row + line
            flag = False
            rows.append(row)
            row = ''
    return rows

def getTeamOneFromRow(_row):

    row_lines = _row.split('\n')
    for line in row_lines:
        if 'class="tabletext"' in line:
            team = line[line.index('title="')+7:]
            team = team[:team.index('">')]
            return team
            

def getTeamTwoFromRow(_row):

    row_lines = _row.split('\n')
    for line in row_lines:
        if 'class="tabletext"' in line:
            second = line.split('<br>')
            temp = second[2]
            team = temp[temp.index('title="')+7:]
            team = team[:team.index('">')]
            return team

def getLineForMatchup(_row):
    val = 0.0
    table_cells = _row.split('<td')
    if len(table_cells) >1:
        cells = table_cells[2]
        sections = cells.split('<br>')
        i = 0
        for sec in sections[1:]:
            i += 1
            
            if 'u' not in sec and sec != '&nbsp;':
                if 'frac12' in sec :
                    value = sec[:sec.index('&')] + '.5'
                else:
                    value = sec[:sec.index('&')]
                break

        # if 'frac12' in value:
        #   value = value[value.index('<br>')+4:value.index('&')] +'.5'
        # else:
        #   value = value[value.index('<br>')+4:value.index('&')]
        if value is not None and len(value) > 0:
            if value == 'PK':
                val = 0.0;
            elif i == 1:
                
                val = float(value) * -1;
            else:
                
                val = float(value);
        else:
            val = 00;
        return val

        
def getDateForMatchup(_row):
    struc = {}
    table_cells = _row.split('<td')
    if len(table_cells)  >=2:
        cell = table_cells[1]
        date_time = cell[cell.index('<span class="cellTextHot">') + len('<span class="cellTextHot">') : cell.index('</span>')]
        date = date_time.split(' ')[0]
        time = date_time.split(' ')[2] + ' ' +date_time.split(' ')[3]
        date = date + '/' + str(current_year)
        struc['date'] = date;
        struc['time'] = time;
        for k,v in struc.items():
            # print v
            return struc

def createParticipant(line_participant):
    participant = Participant()
    participant.participant_name = line_participant
    line_odd = line_participant.find('odds')
    odds = createOdds(line_odd)
    participant.odds = odds
    return participant

def createEvent(_row):
    if _row is not None and _row is not '':
        event = Event();
        date_time = getDateForMatchup(_row)
        if date_time is not None and date_time['date'] is not None and date_time['time'] is not None:
            date = date_time['date']
            time = date_time['time']
            time = dtu.getTimeObjectFromString(time)
            date = dtu.reformatDateString(date)

            event.event_datetime = date + ' ' + time.strftime('%H:%M:%S')
            if(datetime.datetime.now().date() == dtu.getDateObjectFromString(event.event_datetime)):
                event.league = 'NCAA Basketball'
                away_team = getTeamOneFromRow(_row)
                home_team = getTeamTwoFromRow(_row)
                line = getLineForMatchup(_row)
                participant_one = Participant()
                participant_two = Participant()
                participant_one.participant_name = away_team
                participant_two.participant_name = home_team
                period = Period()
                spread = Spread()
                spread.spread_home = line
                period.spread = spread
                period.period_description = 'Game'
                event.participant_one = participant_one
                event.participant_two = participant_two
                event.period = period

                print event.event_datetime
                print event.participant_one.participant_name
                print event.participant_two.participant_name
                print event.period.spread.spread_home;


                return event
        return None

def scrapeSite():
    games = []
    url = 'http://www.vegasinsider.com/college-basketball/odds/las-vegas/'
    r = requests.get(url)
    result = r.text
    lineNum = 0
    games = []
    participants = []
    date = datetime.date.today()
    table = findTable(result)
    rows = getRowsFromTable(table)
    for row in rows:


        event = createEvent(row)
        if event is not None:
            games.append(event)
    return games

def main():
    url = 'http://www.vegasinsider.com/college-basketball/odds/las-vegas/'
    r = requests.get(url)
    result = r.text
    lineNum = 0
    games = []
    participants = []
    date = datetime.date.today()
    table = findTable(result)
    rows = getRowsFromTable(table)
    for row in rows:


        createEvent(row)
        print '---------------'
        
    

if __name__ == '__main__':
    main()



