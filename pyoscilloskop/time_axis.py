# pyOscilloskop
# -*- encoding: UTF8 -*-
#
# Copyright (19.2.2011) Sascha Brinkmann
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy

class TimeAxis:

    def __init__(self, timescale, nmpts):
        self.timescale = timescale
        self.nmpts = nmpts

    def _get_time(self):
        return numpy.arange(-(self.nmpts/2.0)/50*self.timescale, (self.nmpts/2.0)/50*self.timescale, self.timescale/50.0)

    def get_time_axis(self):
        time = self._get_time()
        if (time[self.nmpts-1] < 1e-2):
            time = time * 1e6
        elif (time[self.nmpts-1] < 1):
            time = time * 1e3
        time = time[0:self.nmpts:1]
        return time

    def get_unit(self):
        time = self._get_time()
        if (time[self.nmpts-1] < 1e-2):
            t_unit = "uS"
        elif (time[self.nmpts-1] < 1):
            t_unit = "mS"
        else:
            t_unit = "S"
        return t_unit
