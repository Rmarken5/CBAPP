from livelineentities import Spread
from livelineentities import Total

class Period(object):


    def _setPeriodDescription(self,period_description=None):
        self._period_description = period_description
    
    def _getPeriodDescription(self):
        return self._period_description

    def _setPeriodCutoff(self, period_cutoff=None):
        self._period_cutoff = period_cutoff

    def _getPeriodCutoff(self):
        return self._period_cutoff

    def _setPeriodStatus(self, period_status=None):
        self._period_status = period_status

    def _getPeriodStatus(self):
        return self._period_status

    def _setSpread(self, spread=None):
        self._spread = spread
		
    def _getSpread(self):
        return self._spread
    
    def _setTotal(self, total=None):
        self._total = total
    
    def _getTotal(self):
        return self._total
		

    total = property(_getTotal, _setTotal)
    spread = property(_getSpread, _setSpread) 
    period_status = property(_getPeriodStatus, _setPeriodStatus)
    period_cutoff = property(_getPeriodCutoff,_setPeriodCutoff)
    period_description = property(_getPeriodDescription,_setPeriodDescription)
    
	
		