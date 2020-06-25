
"""
Created on Mon Mar-10 2020

@author: wfok
"""
'''
Tasks:
    copy trace and screenshot from specan to below dir"
    create input excel file and read input line by line
    stroe waveform (or trace) and screenshot with file name based on resolution
    use subprocesses to change resolution and compares getmode readback
    allow 1 minute before taking single run measurement
    load state on specan as an option
    Note: unlikely to be able to confirm automatically that TV changed to desired resolution, but need to first verify manually
    
   
'''    
import csv
import os
import time
import numpy as np
from shutil import copyfile

fmt = "%m%d%Y_%H%M%S"
t = time.strftime(fmt)
print("Timestamp Start = ", t)
from time import sleep

import pyvisa
rm = pyvisa.ResourceManager()
rm.list_resources()
#('ASRL1::INSTR', 'ASRL2::INSTR', 'GPIB0::12::INSTR')
SPECAN = rm.open_resource('TCPIP::172.26.137.74::INSTR')
#SPECAN = rm.open_resource('TCPIP::172.26.137.73::INSTR')
print (SPECAN.query('*IDN?')) # Query the Identification string
print(rm.list_resources())
'''

Console_Name = input ("Enter Console Name: ")
Console_Name = str(Console_Name)
Console_SN = input ("Enter Console Serial Number: ")
Console_SN = str(Console_SN)  
mode = input ("Enter mode ")
mode = str(mode)  

CFX_Config_Type = input ("Enter CFX_Config_Type: ESM or DV?")
CFX_Config_Type = str(CFX_Config_Type)
CFX_Config_Type_SN = input ("Enter CFX_Config_Type Serial Number: ")
CFX_Config_Type_SN = str(CFX_Config_Type_SN)  

Radio_Type = input ("Enter Radio Type: NW or ACC ")
Radio_Type = str(Radio_Type)    
Ant_Name = input ("Enter Antenna Name: ant1, ant2, Pri, or Div? ")
Ant_Name = str(Ant_Name)
Band = input ("Enter Freq. band: 2G or 5G?")
Band = str(Band)
'''


Console_Name = "Lockhart"
Console_SN = "0123456789"

CFX_Config_Type = "EV2"
CFX_Config_Type_SN = "#4"
mode = 'CFX'
Radio_Type = "ACC"    
Ant_Name = "ant1"
Band = "2G"


SUBFOLDER = "{}{} {} {} {} {}"

PASSIVE_DATA_DIR = r"C:\\Users\\v-wifok\\Desktop\\{} {}{}{}_{} {}".format(Console_Name, "(SN-",Console_SN,")", mode, CFX_Config_Type)
if not os.path.exists(PASSIVE_DATA_DIR):
    os.makedirs(PASSIVE_DATA_DIR)
    
def setup_directories(timestamp):

    #basepath = os.path.join(PASSIVE_DATA_DIR, timestamp)
    basepath = os.path.join(PASSIVE_DATA_DIR)
  
    subfolder = SUBFOLDER.format(CFX_Config_Type, CFX_Config_Type_SN, Radio_Type, Ant_Name, Band, t)

    subfolderpath = os.path.join(basepath, subfolder)
    
    print(subfolderpath)
    FILENAMES = ["02.00.00", "02.00.04", "02.00.05"]
    FILENAMES = ["02.00.00"]
    for FILENAME in FILENAMES: 
        SFILENAME = str(FILENAME)
        SPECAN.write('*RST;*CLS')
        SPECAN.write('SYSTem:DISPlay:UPDate ON')
        SPECAN.write('FREQ:START 2.1 GHz') # Setting the center frequency
        SPECAN.write('FREQ:STOP 2.8 GHz') # Setting the span    
         #SPECAN.write('DISP:TRAC:Y:MODE REL')
        SPECAN.write('DISP:TRAC:Y 50dB')
        SPECAN.write('BAND 100 kHz') # Setting the RBW
        SPECAN.write('BAND:VID 100 kHz') # Setting the VBW
        SPECAN.write('SWE:POIN 1001') # Setting the sweep points
        SPECAN.write('INP:EGA ON')   #  Pre-amp ON
        SPECAN.write('DISP:WIND:TRAC:Y:RLEV -75.0') # Setting the Reference Level -- note to get to +20dBm ref level, need to first set ATTN to 40dB on above line
        SPECAN.write('DISP:WIND:TRAC:Y:RLEV:OFFS -50 dB')
        SPECAN.write('INP:ATT 40') # Setting the sweep points -- then set to ATTN 30dB or it will not work
        #SPECAN.write('MMEMory:LOAD: On')
        #SPECAN.write('MMEM:LOAD:STAT 1, "C:\Savejm_00T_002 G.dfl"') 
        #SPECAN.write('INIT;*WAI')
        #SPECAN.write('INIT:CONT OFF')
        #SPECAN.write('SWE:COUN 16')

        
        #sleep (3)
        SPECAN.write('CALC:MARK:AOFF')
       # SPECAN.write('INIT:CONT OFF')
       
        SPECAN.write('CALC:MARK1:X 2.412 GHz')
        SPECAN.write('CALC:MARK1:FUNC:NOIS ON')
        
        SPECAN.write('CALC:MARK2:X 2.417 GHz')
        SPECAN.write('CALC:MARK2:FUNC:NOIS ON') 
        
        SPECAN.write('CALC:MARK3:X 2.422 GHz')
        SPECAN.write('CALC:MARK3:FUNC:NOIS ON')
        
        SPECAN.write('CALC:MARK4:X 2.427 GHz')
        SPECAN.write('CALC:MARK4:FUNC:NOIS ON')        
        
        
        SPECAN.write('CALC:MARK5:X 2.432 GHz')
        SPECAN.write('CALC:MARK5:FUNC:NOIS ON')
        
        SPECAN.write('CALC:MARK6:X 2.437 GHz')
        SPECAN.write('CALC:MARK6:FUNC:NOIS ON') 
        
        SPECAN.write('CALC:MARK7:X 2.442 GHz')
        SPECAN.write('CALC:MARK7:FUNC:NOIS ON')
        
        SPECAN.write('CALC:MARK8:X 2.447 GHz')
        SPECAN.write('CALC:MARK8:FUNC:NOIS ON')        
              
        SPECAN.write('CALC:MARK9:X 2.452 GHz')
        SPECAN.write('CALC:MARK9:FUNC:NOIS ON') 
        
        SPECAN.write('CALC:MARK10:X 2.457 GHz')
        SPECAN.write('CALC:MARK10:FUNC:NOIS ON')
        
        SPECAN.write('CALC:MARK11:X 2.462 GHz')
        SPECAN.write('CALC:MARK11:FUNC:NOIS ON')              
        
        
        
        
        SPECAN.write('CALC:MARK2:FUNC:NOIS ON')
        SPECAN.write('CALC:MARK12:X 2.132 GHz')
        SPECAN.write('CALC:MARK12:FUNC:NOIS ON')
        SPECAN.write('CALC:MARK13:X 2.352 GHz')
        SPECAN.write('CALC:MARK13:FUNC:NOIS ON')
        
       
       # SPECAN.write('INIT;*WAI')
        #SPECAN.write('CALC:MARK1:FUNC:NOIS:RES?')
        #SPECAN.write('CALC:MARK2 ON')
        
       # SPECAN.write('INIT;*WAI')
        #SPECAN.write('CALC:MARK2:FUNC:NOIS:RES?')
        #print ("Noise marker-2 ", Y)
        
        
        
        #SPECAN.write('MMEMory:LOAD: On')
        #SPECAN.write('MMEM:LOAD:STAT 1, "C:\Save.dfl"') 
        SPECAN.write('MMEM:NAME \'C:\\Users\\v-wifok\\Desktop\\q.png\'')
        SPECAN.write('HCOP:IMM') # Make the screenshot now
        SPECAN.write('MMEM:NAME \'C:\\Users\\v-wifok\\Desktop\\q.png\'')
        SPECAN.write('MMEMory:LOAD: On')
        SPECAN.write('TRAC TRACE1,+A$ ')
        SPECAN.write('TRAC:DATA:MEM? TRACE1,1,1001') 
        
        SPECAN.write('FORM:DEXP:FORM CSV') 
        SPECAN.write('MMEM:LOAD1:TRAC 1')
        SPECAN.write('MMEM:STOR1:TRAC 1, \'C:\\Users\\v-wifok\\Desktop\\q.csv\'')
        # SPECAN.write('MMEM:STOR1:TRAC 1, \'C:\trace-max.csv\'')      ------------- important: same as above line, this line won't work since it has only C:\   instead of C:\\
        SPECAN.write(':MMEM:STOR1 :TRAC 1, \'C:\\TEST.ASC\'')

        SPECAN.write('ALL')
        sleep (3)
        SPECAN.write('DISP:TRAC1 ON')
        SPECAN.write('INP:ATT 20')
        SPECAN.write('DISP:TRAC2 ON')
        SPECAN.write('INP:ATT 10')
        SPECAN.write('DISP:TRAC3 ON')  
        SPECAN.write('DISP:TRAC4 ON')           
       # SPECAN.write('INP:ATT 0')
        SPECAN.write('ALL')
        SPECAN.write('MIN | MAX | VIEW | MAX')
        SPECAN.write('DISP:TRAC1: PRES: MMVM')
        SPECAN.write('DISP:TRAC4:MODE: VIEW')

        #sleep (10)
        
#        SPECAN.write('DISP:TRAC:MODE MAX')        
        
        
        
        
        for datatype in ["Screenshots", "Waveforms"]:   # what if it's trace
              
            fullpath = os.path.join(subfolderpath, FILENAME, datatype)
             
            if not os.path.exists(fullpath):
                os.makedirs(fullpath)
                
            if datatype == "Screenshots":                                      #adding a dummy excel file in waveform folder only.
                copyfile("C:\\Users\\v-wifok\\Desktop\\q.png", os.path.join(fullpath, ''+SFILENAME+'.png'))
                
            if datatype == "Waveforms":                                      #adding a dummy excel file in waveform folder only.
                copyfile("C:\\Users\\v-wifok\\Desktop\\q.csv", os.path.join(fullpath, ''+SFILENAME+'.csv'))
       
    return basepath
    
basepath = setup_directories(t)

print(basepath)
