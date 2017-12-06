class Spread(object):

    def _setSpreadVisiting(self, spread_visiting=None):
        self._spread_visiting = spread_visiting
    
    def _getSpreadVisiting(self):
        return self._spread_visiting

    def _setSpreadAdjustVisiting(self, spread_adjust_visiting=None):
       self._spread_adjust_visiting = spread_adjust_visiting

    def _getSpreadAdjustVisiting(self):
       return self._spread_adjust_visiting

    def _setSpreadHome(self, spread_home=None):
        self._spread_home = spread_home
    
    def _getSpreadHome(self):
        return self._spread_home

    def _setSpreadAdjustHome(self, spread_adjust_home=None):
       self._spread_adjust_home = spread_adjust_home

    def _getSpreadAdjustHome(self):
       return self._spread_adjust_home


    spread_visiting = property(_getSpreadVisiting, _setSpreadVisiting)
    spread_adjust_visiting = property(_getSpreadAdjustVisiting, _setSpreadAdjustVisiting)
    spread_home = property(_getSpreadHome, _setSpreadHome)
    spread_adjust_home = property(_getSpreadAdjustHome, _setSpreadAdjustHome)