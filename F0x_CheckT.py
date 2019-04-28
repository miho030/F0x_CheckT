#-*- coding: utf-8 -*-

# Copyright By Nicht; Mixty(KISA, Kucis)
"""
This Script made niche; Misty
To check server's cpu info

Based on Py3.7.3 stabled version,
Follow & published with GNU is Not Unix; General Public License Ver.3 : based on ricard stolman

Checking your system info and continue check your cpu temperature
"""
import socket
import platform
import multiprocessing
from datetime import datetime
import clr
from clr import AddReference

openhardwaremonitor_hwtypes = ['Mainboard','SuperIO','CPU','RAM','GpuNvidia','GpuAti','TBalancer','Heatmaster','HDD']
cputhermometer_hwtypes = ['Mainboard','SuperIO','CPU','GpuNvidia','GpuAti','TBalancer','Heatmaster','HDD']
openhardwaremonitor_sensortypes = ['Voltage','Clock','Temperature','Load','Fan','Flow','Control','Level','Factor','Power','Data','SmallData']
cputhermometer_sensortypes = ['Voltage','Clock','Temperature','Load','Fan','Flow','Control','Level']


# Showing Interfaces....
print("#===========================================================================================================================#")
print("=                                                                                                                           =")
print("=               '@:                        #@:   @                         @.                                               =")
print("=     @@@@@#   @; @@                     #@. :#  @                         @.      @@@@@@@`                                 =")
print("=     @`      #+   @,                   :@       @                         @.         @`                                    =")
print("=     @`      @    @@  @.   @:          @'       @ @@@'   ,@@@@    `@@@@   @.  +@     @`             @ @@@'  @:    @`       =")
print("=     @`      @   @:@  '@  @#           @`       @@  .@   @   ##   @,      @. :@      @`             @@   @  +@   :@        =")
print("=     @@@@@, `@  @ .@   @#,@            @        @    @  +@   .@  +@       @.,@       @`             @    @.  @   @'        =")
print("=     @`     `@.@  .@    @@             @        @    @  @@@@@@@  @#       @,@`       @`             @    @:  @+  @         =")
print("=     @`      @@   :@    @@             @`       @    @  @#       @+       @.@#       @`             @    @,  ,@ '@         =")
print("=     @`      @,   #+   @''@            @+       @    @  +@       #@       @. @+      @`             @    @    @`@,         =")
print("=     @`      #@   @   #@  @#           :@       @    @  `@       `@       @.  @:     @`      @@:    @   :@    ##@          =")
print("=     @`      #@   @   #@  @#           :@       @    @  `@       `@       @.  @:     @`      @@:    @   :@    ##@          =")
print("=     @`       @@@@:  ,@    @:           +@@@@#  @    @   +@@@@+   ;@@@@   @.  ,@.    @`      @@:    @@@@@      @#          =")
print("=                                                                                                    @          @           =")
print("=                                                                                                    @         #@           =")
print("=                                                                                                    @        +@            =")
print("=                                                                                                            @;             =")
print("#===========================================================================================================================#\n\n\n")



print("#############################################################")
print("#           [ Fox_Cpu_Temperature_Checker 0.0.1]            #")
print("#                                                           #")
print("#                                                           #")
print("#                                  Made by Misty            #")
print("#           Waring : published with GNU; GPL Ver3           #")
print("#############################################################\n")

# Starting system analysis
print("[!] ", "Checking your system *wait...\n\n")
now = datetime.now()
print"[-] Checking Start time is.. : ", now, "\n"

#import your system name and network ip addr
#f0x_name = socket.gethostname()
#f0x_ip = socket.gethostbyname(f0x_name)
#print"컴퓨터 이름 : ", f0x_name
print"컴퓨터 Ip addr :", f0x_ip, "\n"

print"[+] ", "OS 종류: ", platform.system()
print"[+] ", "OS 상세정보: ", platform.platform()
print"[+] ", "OS 버전: ", platform.version()
print"[+] ", "프로세서: ", platform.processor()
print"[+] ", "CPU 수: ", multiprocessing.cpu_count(), "\n\n"




def initialize_openhardwaremonitor():
    file = 'OpenHardwareMonitorLib.dll'
    clr.AddReference(file)

    from OpenHardwareMonitor import Hardware

    handle = Hardware.Computer()
    handle.MainboardEnabled = True
    handle.CPUEnabled = True
    handle.RAMEnabled = True
    handle.GPUEnabled = True
    handle.HDDEnabled = True
    handle.Open()
    return handle

def initialize_cputhermometer():
    file = 'CPUThermometerLib.dll'
    clr.AddReference(file)

    from CPUThermometer import Hardware
    handle = Hardware.Computer()
    handle.CPUEnabled = True
    handle.Open()
    return handle

def fetch_stats(handle):
    for i in handle.Hardware:
        i.Update()
        for sensor in i.Sensors:
            parse_sensor(sensor)
        for j in i.SubHardware:
            j.Update()
            for subsensor in j.Sensors:
                parse_sensor(subsensor)


def parse_sensor(sensor):
        if sensor.Value is not None:
            if type(sensor).__module__ == 'CPUThermometer.Hardware':
                sensortypes = cputhermometer_sensortypes
                hardwaretypes = cputhermometer_hwtypes
            elif type(sensor).__module__ == 'OpenHardwareMonitor.Hardware':
                sensortypes = openhardwaremonitor_sensortypes
                hardwaretypes = openhardwaremonitor_hwtypes
            else:
                return

            if sensor.SensorType == sensortypes.index('Temperature'):
                print(u"%s %s Temperature Sensor #%i %s - %s\u00B0C" % (hardwaretypes[sensor.Hardware.HardwareType], sensor.Hardware.Name, sensor.Index, sensor.Name, sensor.Value))

if __name__ == "__main__":
    print("OpenHardwareMonitor:")
    HardwareHandle = initialize_openhardwaremonitor()
    fetch_stats(HardwareHandle)
    print("\nCPUMonitor:")
    CPUHandle = initialize_cputhermometer()
    fetch_stats(CPUHandle)



#  테스트 코드
"""
# Checking CPU temperature
f0x_temp = AvgCpuTemp.avg_cpu_temp.get_current_cpu_temp()
f0x_temp_average = AvgCpuTemp.avg_cpu_temp.get_average_temperature()
print "[!] ", "Checking your cpu temperature....wait\n"
print "[+] ", "CPU 온도 : ", f0x_temp
print "[+] ", "CPU 평균온도 : ", f0x_temp_average
"""
