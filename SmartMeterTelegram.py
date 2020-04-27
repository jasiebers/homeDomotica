import sys
import serial


self = serial.Serial()
self.baudrate = 115200
self.bytesize = serial.SEVENBITS
self.parity = serial.PARITY_NONE
self.stopbits = serial.STOPBITS_ONE
self.xonxoff = 0
self.rtscts = 0
self.timeout = 20
self.port = '/dev/ttyUSB0'
#Initialize
#Open COM port
self.open()

#p1_teller is teller om van 0 tot 20 te tellen: 20 is aantal berichten
p1_teller = 0

#Run
#Haal bericht op
while p1_teller < 26:
    p1_line = ""
    #Read 1 line from serial port
    try:
        p1_raw = self.readLine()
    except:
        sys.exit("Seriele poort %s kan niet gelezen worden" % self.name)
    p1_str = str(p1_raw)
    p1_line = p1_str.strip()
    print(p1_line)
    p1_teller = p1_teller + 1

#Close
#Close port and show status
self.close()



