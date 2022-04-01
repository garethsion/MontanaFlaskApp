#!usr/bin/env python

import pyvisa
import pyvisa.constants as pc

import json

class PowerSupply:
    def __init__(self):
        f = open('config\\pyvisarc.json') # need to get correct library file 
        lib = json.load(f)
        lib['config']['visa_lib']
        self.rm = pyvisa.ResourceManager(lib)
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
                        self.addr(r)
        try:
            self.inst = self.rm.open_resource(self.addr)
        except:
            print("Couldn't connect to instrument")
        return
    
    def channel_output(self, ch='CH1', cmnd='OFF'):
        self.inst.write("OUTPut " + ch + "," + cmnd)
        return