# Python code to parse lines from the feed
# url = http://livelines.betonline.com/sys/LineXML/LiveLineObjXml.asp?sport=basketball&league=NCAA%20Basketball
# Author - Ryan Marken

import csv
import urllib.request as request
import pathlib
import xml.etree.ElementTree as ET
from livelineentities import *

ncaa_name = "NCAA Basketball"
pathlib.Path('./output-files').mkdir(parents=True, exist_ok=True) 
outfile = open('./output-files/spread-by-line.txt','w+')

# This function takes a url parses the xml.
def parseXML(url):
    opener = request.build_opener()
    resp = opener.open(url)
    print(resp)
    tree = ET.parse(resp)
    print(tree)
    root = tree.getroot()
    i = 0
    events = []

    print(root.text)
    for line_event in root.findall('event'):
        league = line_event.find('league').text

        if checkLeagueForNCAA(league):
            print('There\'s one')
            print('iteration: ', i)
            event = createEvent(line_event)
            printEvent(event)
			
def checkLeagueForNCAA(leaguename):
    if leaguename == ncaa_name:
        return True
    else:
        return False

def createEvent(line_event):
    event = Event()
    event.event_datetime = line_event.find('event_datetimeGMT').text
    event.sport_type = line_event.find('sporttype').text
    event.schedule_text = line_event.find('scheduletext').text
    event.league = line_event.find('league').text
    line_participants = line_event.findall('participant')
    if len(line_participants) > 1:
        part_one = line_participants[0]
        part_two = line_participants[1]
        participant_one = createParticipant(part_one)
        participant_two = createParticipant(part_two)
		
        event.participant_one = participant_one
        event.participant_two = participant_two
    
    period = createPeriod(line_event)
    event.period = period
    return event


def createParticipant(line_participant):
    participant = Participant()
    participant.participant_name = line_participant.find('participant_name').text
    participant.rot_num = line_participant.find('rotnum').text
    participant.visiting_home_draw = line_participant.find('visiting_home_draw').text
    line_odd = line_participant.find('odds')
    odds = createOdds(line_odd)
    participant.odds = odds
    return participant
	
def createOdds(line_odd):
    odds = Odds()
    odds.money_line = line_odd.find('moneyline').text
    line_team_total = line_odd.find('teamtotal')
    odds.team_total = createTeamTotal(line_team_total)
    return odds

def createTeamTotal(line_team_total):
    team_total = TeamTotal()
    team_total.total_points = line_team_total.find('total_points').text
    team_total.over_adjust = line_team_total.find('over_adjust').text
    team_total.under_adjust = line_team_total.find('under_adjust').text

    return team_total

def createPeriod(line_event):
    period = Period()
    line_period = line_event.find('period')
    period.period_description = line_period.find('period_description').text
    period.period_cutoff = line_period.find('periodcutoff_datetimeGMT').text
    period.period_status = line_period.find('period_status').text
    line_spread = line_period.find('spread')
    spread = createSpread(line_spread)
    period.spread = spread
    line_total = line_period.find('total')	
    total = createTotal(line_total)
    period.total = total
    
    return period
    
def createSpread(line_spread):
    spread = Spread()
    spread.spread_visiting = line_spread.find('spread_visiting').text
    spread.spread_adjust_visiting = line_spread.find('spread_adjust_visiting').text
    spread.spread_home = line_spread.find('spread_home').text
    spread.spread_adjust_home = line_spread.find('spread_adjust_home').text
	
    return spread

def createTotal(line_total):
    total = Total()
    total.total_points = line_total.find('total_points').text
    total.over_adjust = line_total.find('over_adjust').text
    total.under_adjust = line_total.find('under_adjust').text
	
    return total
	
def printEvent(event):
    participant_one = event.participant_one
    participant_two = event.participant_two

    print(participant_one.participant_name)
    print(participant_two.participant_name)
    outfile.write(participant_one.participant_name + '\n')
    outfile.write(participant_two.participant_name + '\n')
	
	
def main():
    basketballgames = parseXML(
        'http://livelines.betonline.com/sys/LineXML/LiveLineObjXml.asp?sport=basketball&league=NCAA%20Basketball')


if __name__ == "__main__":
    main()
