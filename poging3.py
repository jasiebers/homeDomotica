import sys
import serial

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

def GetSMmessage(ser):
    #Open COM port
    ser.open()
    
    p1_line = ''
    #Wait till start of new telegram
    while p1_line[2:7] != "/ISK5":
        p1_raw = ser.readline()
        p1_str = str(p1_raw)
        p1_line = p1_str.strip()
    #Start gathering lines from telegram (24 lines in total)
    for i in range(0,24):
        p1_raw = ser.readline()
        p1_str = str(p1_raw)
        p1_line = p1_str.strip()
        #Gather data from line
        # Time instance
        if p1_line[2:11] == '0-0:1.0.0':
            time = int(p1_line[12:24])
        elif p1_line[2:11] == '1-0:1.7.0':
            verbruik = float(p1_line[12:18])
        elif p1_line[2:11] == '1-0:2.7.0':
            opwek = float(p1_line[12:18])
        elif p1_line[2:12] == '1-0:32.7.0':
            voltage = float(p1_line[13:18])
        elif p1_line[2:12] == '1-0:31.7.0':
            ampere = int(p1_line[13:16])
    #Close COM port
    ser.close()
    #Return SM message
    message = (time,verbruik,opwek,voltage,ampere)
    return (message)

message = GetSMmessage(ser)