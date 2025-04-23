from __future__ import absolute_import
# Please do not change this configuration file for Quisk.  Copy it to
# your own config file and make changes there.
#
# This config file is for hamlib control of a QMX through hamlib, with Quisk
# acting as a panadapter.  The daemon rigctld must be running.  The open() method
# below tries to start it, or you can start it by hand.

import sys, os

if sys.platform == "win32":
  name_of_sound_capt = 'Primary'
  name_of_sound_play = 'Primary'
  latency_millisecs = 150
  data_poll_usec = 20000
else:
  name_of_sound_capt = 'hw:0'
  name_of_sound_play = 'hw:0'
  latency_millisecs = 150
  data_poll_usec = 5000

# Use the hamlib hardware module to talk to the QMX
from quisk_hardware_hamlib import Hardware as BaseHardware

class Hardware(BaseHardware):
  def ChangeFrequency(self, tune, vfo, source='', band='', event=None):
    BaseHardware.ChangeFrequency(self, tune, vfo, source, event)
    self.quisk_freq = tune 
    self.quisk_vfo = tune -12600 # my change to align waterfall with vfo
    #if DEBUG: print('Change', source, tune)
    return self.quisk_freq, self.quisk_vfo
    
  def __init__(self, app, conf):
    BaseHardware.__init__(self, app, conf)
    # Change the port and timing parameters here:
    # self.hamlib_rigctld_port = 4532		# Standard rigctld control port
    # self.hamlib_poll_seconds = 0.5		# Time interval to poll for changes
  def open(self):
    # 
    ret = BaseHardware.open(self)
    #if not self.hamlib_connected:	# rigctld is not started.  Try to start it.
      #os.system("rigctld -m 2002 -r /dev/serial/by-id/usb-QRP_Labs_QMX_Transceiver-if00 -s 4800 -C stop_bits=2 & ")	# Check the baud rate menu setting
      # If this fails, start rigctld by hand.
    return ret
