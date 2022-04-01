#!usr/bin/env python

import pyvisa
import pyvisa.constants as pc

import json

class PowerSupply:
    def __init__(self):
        f = open('config\\pyvisarc.json') # need to get correct library file 
        lib = json.load(f)
        visa_lib = lib['config']['visa_lib']
        self.rm = pyvisa.ResourceManager(visa_lib)
        return

    def connect(self, addr=None, USB=False, ASRL=False, GPIB=False):
        ''' Not yet complete. I haven't added functionality for different types of instrument, only usb '''
        if addr:
            self.addr = addr
        else:
            resources = self.rm.list_resources()
            for r in resources:
                if USB:
                    if 'USB0' in r:
                        self.addr = r
        try:
            self.inst = self.rm.open_resource(self.addr)
        except:
            print("Couldn't connect to instrument")
        return
    
    def channel_output(self, ch='CH1', cmnd='OFF'):
        self.inst.write("OUTPut " + ch + "," + cmnd)
        return
    
    def set_voltage(self, ch='CH1', volts=0):
        self.inst.write('{:s}: VOLTage {:.3f}'.format(ch, volts))

    def read_voltage(self, ch='CH1'):
        self.inst.query('MEASure: VOLTage? ' + ch )
        return

    def set_current(self, ch='CH1', current=0):
        self.inst.write('{:s}: CURRent {:.3f}'.format(ch, current))

    def read_current(self, ch='CH1'):
        self.inst.query('MEASure: CURRent? ' + ch )
        return
