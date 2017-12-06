from livelineentities import Participant

class Event(object):

    def _setEventDatetime(self, event_datetime=None):
        self._event_datetime = event_datetime

    def _getEventDatetime(self):
       return self._event_datetime		
    
    def _setSportType(self, sport_type=None):
       self._sport_type = sport_type

    def _getSportType(self):
       return self._sport_type

    def _setScheduleText(self, schedule_text=None):
       self._schedule_text = schedule_text

    def _getScheduleText(self):
       return self._schedule_text
	   
    def _setLeague(self, league=None):
        self._league = league
	
    def _getLeague(self):
        return _league
		
    def _setParticipant(self, participant=None):
        self._participant = participant

    def _getParticipant(self):
	    return self._participant
		
    event_datetime = property(_getEventDatetime, _setEventDatetime)
    sport_type = property(_getSportType, _setSportType)
    schedule_text = property(_getScheduleText, _setScheduleText)
    league = property(_getLeague, _setLeague)
    participant = property(_getParticipant, _setParticipant)
