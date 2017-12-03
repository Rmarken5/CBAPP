class TeamTotal(object):

    def _setOverAdjust(self,over_adjust=None):
        self._over_adjust = over_adjust

    def _getOverAdjust(self):
        return self._over_adjust

    def _setUnderAdjust(self, under_adjust=None):
        self._under_adjust = under_adjust

    def _getUnderAdjust(self):
        return self._under_adjust

    def _setTotalPoints(self, total_points=None):
        self._total_points = total_points

    def _getTotalPoints(self):
        return self._total_points

    over_adjust = property(_getOverAdjust,_setOverAdjust)
    under_adjust = property(_getUnderAdjust,_setUnderAdjust )
    total_points = property(_getTotalPoints,_setTotalPoints)



    # def __init__(self,total_points,over_adjust,under_adjust):
    #     self.over_adjust = over_adjust
    #     self.total_points = total_points
    #     self.under_adjust = under_adjust
