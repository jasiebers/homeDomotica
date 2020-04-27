# DSMR P1 uitlezen
# (c) 10-2012 - GJ - gratis te kopieren en te plakken
versie = "2.0"
import sys
import serial
import pandas as pd

##############################################################################
#Main program
##############################################################################
print ("DSMR P1 uitlezen",  versie)

class meterMessage:
    def __init__(self):
        self.time = int()
        self.LDN1 = float()
        self.LDN2 = float()
        self.ODN1 = float()
        self.ODN2 = float()
        self.tarifIndicator = int()
        self.verbruik = float()
        self.opwek = float()
        self.powerFailures = int()
        self.longPowerFailures = int()
        self.powerFailureLog = str()
        self.voltageSags = int()
        self.voltageSwells = int()
        self.testMessage = str()
        self.voltage = float()
        self.ampere = int()
        self.instantLDN = float()
        self.instantODN = float()
        self.gas = float()
    
#Set COM port config
ser = serial.Serial()
ser.baudrate = 115200
ser.bytesize=serial.SEVENBITS ## SEVENBITS
ser.parity=serial.PARITY_NONE
ser.stopbits=serial.STOPBITS_ONE
ser.xonxoff=0
ser.rtscts=0
ser.timeout=20
ser.port="/dev/ttyUSB0"

def GetMeterMessage(ser):
    
    message = meterMessage()
    
    #Open COM port
    ser.open()
    
    #Initialize
    #Lengte van de telegram is 28 lines
    #p1_teller is tellertje voor van 0 tot 28 te tellen
    p1_teller=0

    while p1_teller < 27:
        p1_line = ''
        #Read 1 line van de seriele poort
        try:
            p1_raw = ser.readline()
        except:
            sys.exit ("Seriele poort %s kan niet gelezen worden. Aaaaaaaaarch." % ser.name )
        p1_str=str(p1_raw)
        p1_line=p1_str.strip()
        
        ##Haal objecten in de telegram op
        #Time instance
        if p1_line[2:11] == '0-0:1.0.0':
            message.time = int(p1_line[12:24])
            print('time instance found')
        elif p1_line[2:11] == '1-0:1.8.1':
            message.LDN1 = float(p1_line[12:22])
        elif p1_line[2:11] == '1-0:1.8.2':
            message.LDN2 = float(p1_line[12:22])
        elif p1_line[2:11] == '1-0:2.8.1':
            message.ODN1 = float(p1_line[12:22])
        elif p1_line[2:11] == '1-0:2.8.2':
            message.ODN2 = float(p1_line[12:22])
        elif p1_line[2:13] == '0-0:96.14.0':
            message.tarifIndicator = int(p1_line[14:18])
        elif p1_line[2:11] == '1-0:1.7.0':
            message.verbruik = float(p1_line[12:18])
        elif p1_line[2:11] == '1-0:2.7.0':
            message.opwek = float(p1_line[12:18])
        elif p1_line[2:13] == '0-0:96.7.21':    
            message.powerFailures = int(p1_line[14:19])
        elif p1_line[2:12] == '0-0:96.7.9':
            message.longPowerFailures = int(p1_line[13:18])
        elif p1_line[2:13] == '1-0:99.97.0':
            if p1_line[15] != ')':
                message.powerFailureLog = str(p1_line[14:p1_line.find(')')])
        elif p1_line[2:13] == '1-0:32.32.0':
            message.voltageSags = int(p1_line[14:19])
        elif p1_line[2:13] == '1-0:32.36.0':
            message.voltageSwells = int(p1_line[14:19])
        elif p1_line[2:13] == '0-0:96.13.0':
             if p1_line[15] != ')':
                 message.testMessage = str(p1_line[14:p1_line.find(')')])
        elif p1_line[2:12] == '1-0:32.7.0':
            message.voltage = float(p1_line[13:18])
        elif p1_line[2:12] == '1-0:31.7.0':
            message.ampere = int(p1_line[13:16])
        elif p1_line[2:12] == '1-0:21.7.0':
            message.instantLDN = float(p1_line[13:19])
        elif p1_line[2:12] == '1-0:22.7.0':
            message.instantODN = float(p1_line[13:19])
        elif p1_line[2:12] == '0-1:24.2.1':
            message.gas = float(p1_line[(1+p1_line.find(')')):len(p1_line)][(p1_line[(p1_line.find(')')+1):len(p1_line)].find('(')+1) : (p1_line[(p1_line.find(')')+1):len(p1_line)].find(')')-3)])
            
        # als je alles wil zien moet je de volgende line uncommenten
        #print(p1_line)
        p1_teller = p1_teller +1

    #Close port and return message
    ser.close()
    return(message)
