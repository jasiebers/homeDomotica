import MeterTelegramConfig as meter
import numpy as numpy
import pandas as pd
from datetime import datetime
import statistics as stat

meterTelegram = meter.GetMeterMessage(meter.ser)
verbruikMean = []
verbruikMax = []
verbruikMin = []
opwekMean = []
opwekMax = []
opwekMin = []
voltageMean = []
voltageMax = []
voltageMin = []

for i in range(1,12):
    verbruik = []
    opwek = []
    voltage = []
    residu = meterTelegram.time%900
    while residu <= meterTelegram.time%900:
        verbruik.append(meterTelegram.verbruik)
        opwek.append(meterTelegram.opwek)
        voltage.append(meterTelegram.voltage)
        meterTelegram = meter.GetMeterMessage(meter.ser)
    verbruikMean.append(stat.mean(verbruik))
    verbruikMax.append(max(verbruik))
    verbruikMin.append(min(verbruik))
    opwekMean.append(stat.mean(opwek))
    opwekMin.append(min(opwek))
    opwekMax.append(max(opwek))
    voltageMean.append(stat.mean(voltage))
    voltageMin.append(min(voltage))
    voltageMax.append(max(voltage))
    now = datetime.now()
    print(i)
    print(now.strftime('%H:%M:%S'))




    
