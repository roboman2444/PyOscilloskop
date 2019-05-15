#!/usr/bin/env python2
# -*- encoding: UTF8 -*-

import sys
import logging

from pyoscilloskop import RigolScope

## To get more debug output, do:
#logging.basicConfig(level=logging.DEBUG)

from universal_usbtmc.backends.linux_kernel import Instrument
dev_name = '/dev/usbtmc0'
device = Instrument(dev_name)

scope = RigolScope(device)

channel1Data = scope.get_channel_1().get_data();
channel2Data = scope.get_channel_2().get_data();
print("{0} values received for channel 1.".format(len(channel1Data)))
print("{0} values received for channel 2.".format(len(channel2Data)))

scope.reactivate_control_buttons()

