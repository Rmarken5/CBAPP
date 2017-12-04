from livelineentities import TeamTotal

class Odds(object):

    def _setMoneyLine(self,money_line=None):
	    self._money_line = money_line
	  
    def _getMoneyLine(self):
        return self._money_line
    
    def _setTeamTotal(self,team_total=None):
        self._team_total = team_total
		
    def _getTeamTotal(self):
        return self._team_total
	  

    money_line = property(_getMoneyLine, _setMoneyLine)
    team_total = property(_getTeamTotal, _setTeamTotal)
