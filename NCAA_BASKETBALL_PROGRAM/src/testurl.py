import requests

url = 'http://www.ncaa.com/scoreboard/basketball-men/d1/2017/12/09'

r = requests.get(url)
result = r.text
lineNum = 0
lines = result.split('\n')
for line in lines:
    lineNum= lineNum + 1
    print(lineNum)
    print (line.strip())


