from livelineentities import Odds

class Participant(object):

    def _setParticipantName(self, participant_name=None):
	    self._participant_name = particpant_name

    def _getParticipantName(self):
	    return self._participant_name

    def _setRotNum(self, rot_num=None):
        self._rot_num = rot_num
	
    def _getRotNum(self):
        return self._rot_num
		
    def _setVisitingHomeDraw(self, visiting_home_draw=None):
        self._visiting_home_draw = visiting_home_draw

    def _getVisitingHomeDraw(self):
	    return self._visiting_home_draw
		
    def _setOdds(self, odds=None):
	    self._odds = odds

    def _getOdds(self, odds=None):
	    return self._odds
	
	
    participant_name = property(_getParticipantName,_setParticipantName)
    rot_num = property(_getRotNum,_setRotNum)
    visiting_home_draw = property(_getVisitingHomeDraw, _setVisitingHomeDraw)
    odds = property(_getOdds, _setOdds);
	