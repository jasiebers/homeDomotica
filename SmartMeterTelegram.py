class SMT:

    def __init__(self,baudrate,bytesize,parity,stopbits):
        import sys
        import serial

        ser = serial.Serial()
        ser.baudrate = 115200
        ser.bytesize = serial.SEVENBITS
        ser.parity = serial.PARITY_NONE
        ser.stopbits = serial.STOPBITS_ONE
        ser.xonxoff = 0
        ser.rtscts = 0
        ser.timeout = 20
        ser.port = '/dev/ttyUSB0'

    # Code om slimme meter uit te lezen
    def GetSmartMeterMessage():
        #Initialize
        #Open COM port
        try:
            ser.open()
        except:
            sys.exit ("Fout bij het openen van %s." % ser.name)

        #p1_teller is teller om van 0 tot 20 te tellen: 20 is aantal berichten
        p1_teller = 0

        #Run
        #Haal bericht op
        while p1_teller < 23:
            p1_line = ""
            #Read 1 line from serial port
            try:
                p1_raw = ser.readLine()
            except:
                sys.exit("Seriele poort %s kan niet gelezen worden" % ser.name)
            p1_str = str(p1_raw)
            p1_line = p1_str.strip()
            p1_teller = p1_teller + 1

        #Close
        #Close port and show status
        try:
            ser.close()
        except:
            sys.exit("Oops %s. Programma afgebroken. Kon de seriele poort niet sluiten." % ser.name)
        return(message)



