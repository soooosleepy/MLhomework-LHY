import time
import numpy as np
import pandas as pd

# with open('train.csv', 'r',encoding='unicode_escape',newline='') as f:
#     reader = csv.reader(f,header=None)
    
#     i = 0
#     for row in reader:
#         if(i <= 0):
#             prfloat(row)
#             i += 1

class Meteorology:

    def __init__(self,temp=-1,CH4=-1,CO=-1,NMHC=-1,NO=-1,NO2=-1,NOx=-1,O3=-1,PM10=-1,PM25=-1,rainfall=-1,RH=-1,SO2=-1,THC=-1, WD_HR=-1,wind_direct=-1,wind_speed=-1,WS_HR=-1):
        self.temp = temp
        self.CH4 = CH4
        self.CO = CO
        self.NMHC = NMHC
        self.NO = NO
        self.NO2 = NO2
        self.NOx = NOx
        self.O3 = O3
        self.PM10 = PM10
        self.PM25 = PM25
        self.rainfall = rainfall
        self.RH = RH
        self.SO2 = SO2
        self.THC = THC
        self.WD_HR = WD_HR
        self.wind_direct = wind_direct
        self.wind_speed = wind_speed
        self.WS_HR = WS_HR

    def __str__(self):
        p = "AMB_TEMP: " + str(self.temp) + "\nCH4: " + str(self.CH4) + "\nCO: " + str(self.CO) + "\nNMHC: " + str(self.NMHC) + "\nNO: " + str(self.NO) + "\nNO2: " + str(self.NO2) + "\nNOx: " + str(self.NOx) + "\nO3: " + str(self.O3) + "\nPM10: " + str(self.PM10) + "\nPM2.5: " + str(self.PM25) + "\nRAINFALL: " + str(self.rainfall) + "\nRH: " + str(self.RH) + "\nSO2: " + str(self.SO2) + "\nTHC: " + str(self.THC) + "\nWD_HR: " + str(self.WD_HR) + "\nWIND_DIRECT: " + str(self.wind_direct) + "\nWIND_SPEED: " + str(self.wind_speed) + "\nWS_HR: " + str(self.WS_HR) + "\n"
        return p 
temp = [Meteorology()]*366*24

def date2day(date):
    temp = time.strptime(date,'%Y/%m/%d')
    return temp.tm_yday


def readdata(path):
    temp = [Meteorology() for i in range(366*24)]
    data = pd.read_csv(path,header = None)
    list = data.values.tolist()
    del(list[0])
    for ii in list:
        num_day = date2day(ii[0])
        if(ii[2] == 'AMB_TEMP'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].temp = float(ii[jj+3])
                # print(num_day)
        elif (ii[2] == 'CH4'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].CH4 = float(ii[jj+3])
        elif (ii[2] == 'CO'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].CO = float(ii[jj+3])
        elif (ii[2] == 'NMHC'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].NMHC = float(ii[jj+3])
        elif (ii[2] == 'NO'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].NO = float(ii[jj+3])
        elif (ii[2] == 'NO2'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].NO2 = float(ii[jj+3])
        elif (ii[2] == 'NOx'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].NOx = float(ii[jj+3])
        elif (ii[2] == 'O3'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].O3 = float(ii[jj+3])
        elif (ii[2] == 'PM10'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].PM10 = float(ii[jj+3])
        elif (ii[2] == 'PM2.5'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].PM25 = float(ii[jj+3])
        elif (ii[2] == 'RAINFALL'):
            for jj in range(24):
                if(ii[jj+3] == 'NR'):
                    ii[jj+3] = '0'
                temp[(num_day-1)*24+jj].rainfall = float(ii[jj+3])
        elif (ii[2] == 'RH'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].RH = float(ii[jj+3])
        elif (ii[2] == 'SO2'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].SO2 = float(ii[jj+3])
        elif (ii[2] == 'THC'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].THC = float(ii[jj+3])
        elif (ii[2] == 'WD_HR'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].WD_HR = float(ii[jj+3])
        elif (ii[2] == 'WIND_DIREC'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].wind_direct = float(ii[jj+3])
        elif (ii[2] == 'WIND_SPEED'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].wind_speed = float(ii[jj+3])
        elif (ii[2] == 'WS_HR'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].WS_HR = float(ii[jj+3])
    return temp
        


def readdata_a(path):
    temp = [Meteorology() for i in range(240)]
    data = pd.read_csv(path,header = None)
    list = data.values.tolist()
    for ii in list:
        num_day = date2day(ii[0])
        if(ii[2] == 'AMB_TEMP'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].temp = float(ii[jj+3])
                # print(num_day)
        elif (ii[2] == 'CH4'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].CH4 = float(ii[jj+3])
        elif (ii[2] == 'CO'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].CO = float(ii[jj+3])
        elif (ii[2] == 'NMHC'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].NMHC = float(ii[jj+3])
        elif (ii[2] == 'NO'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].NO = float(ii[jj+3])
        elif (ii[2] == 'NO2'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].NO2 = float(ii[jj+3])
        elif (ii[2] == 'NOx'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].NOx = float(ii[jj+3])
        elif (ii[2] == 'O3'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].O3 = float(ii[jj+3])
        elif (ii[2] == 'PM10'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].PM10 = float(ii[jj+3])
        elif (ii[2] == 'PM2.5'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].PM25 = float(ii[jj+3])
        elif (ii[2] == 'RAINFALL'):
            for jj in range(24):
                if(ii[jj+3] == 'NR'):
                    ii[jj+3] = '0'
                temp[(num_day-1)*24+jj].rainfall = float(ii[jj+3])
        elif (ii[2] == 'RH'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].RH = float(ii[jj+3])
        elif (ii[2] == 'SO2'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].SO2 = float(ii[jj+3])
        elif (ii[2] == 'THC'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].THC = float(ii[jj+3])
        elif (ii[2] == 'WD_HR'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].WD_HR = float(ii[jj+3])
        elif (ii[2] == 'WIND_DIREC'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].wind_direct = float(ii[jj+3])
        elif (ii[2] == 'WIND_SPEED'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].wind_speed = float(ii[jj+3])
        elif (ii[2] == 'WS_HR'):
            for jj in range(24):
                temp[(num_day-1)*24+jj].WS_HR = float(ii[jj+3])
    return temp



