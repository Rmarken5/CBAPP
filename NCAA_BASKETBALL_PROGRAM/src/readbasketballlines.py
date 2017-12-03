#Python code to parse lines from the feed
#url = http://livelines.betonline.com/sys/LineXML/LiveLineObjXml.asp?sport=basketball&league=NCAA%20Basketball
#Author - Ryan Marken

import csv
import urllib.request as request
import xml.etree.ElementTree as ET

ncaa_name = "NCAA Basketball"

#This function takes a url parses the xml.
def parseXML(url):

    opener = request.build_opener()
    resp = opener.open(url)
    print(resp)	
    tree = ET.parse(resp)
    print(tree)
    root = tree.getroot()
	
    newsitems = []
    print(root.text)
    for event in root.findall('event'):
        league = event.find('league').text
        
        if  checkLeagueForNCAA(league):
            print('There\'s one')
			
def checkLeagueForNCAA(leaguename):
    if leaguename == ncaa_name:
        return True
    else:
        return False
def main():
    
	basketballgames = parseXML('http://livelines.betonline.com/sys/LineXML/LiveLineObjXml.asp?sport=basketball&league=NCAA%20Basketball')
	
if __name__ == "__main__":
	
    main()
		
