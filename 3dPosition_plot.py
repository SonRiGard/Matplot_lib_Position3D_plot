
import numpy as np
import matplotlib.pyplot as plt
import serial
import time 
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.axes(projection='3d')
N = 10 #numbers of value in 1 line
ser = serial.Serial(
        # Serial Port to read the data from
        port='COM5',
 
        #Rate at which the information is shared to the communication channel
        baudrate = 9600,
   
        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,
 
       # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,
     
        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,
 
        # Number of serial commands to accept before timing out
        timeout=100
)
xline = []#luu gia tri của gia tri cua cac truc
yline = []#luu gia tri của gia tri cua cac truc
zline = []#luu gia tri của gia tri cua cac truc

for i in range(N):
    xline.append(0.0)
for i in range(N):
    yline.append(0.0)
for i in range(N):
    zline.append(0.0)
# Pause the program for 1 second to avoid overworking the serial port
# time.sleep(10)
x=ser.readline()
time.sleep(0.1)
       
def animate (i):
    x=ser.readline()
    print(x)
    # print(data[0]+data[1]+data[2])
    data = x.decode().rstrip().split(',')
    if len(data) == 3:
        # print(data[0]+data[1]+data[2])
        # # Data for a three-dimensional line
        xline.pop(0)
        xline.append(float(data[0]))
        yline.pop(0) 
        yline.append(float(data[1])) 
        zline.pop(0)
        zline.append(float(data[2])) 
        # ax.plot(xline, yline, zs=0, zdir='z', label='curve in (x, y)')
        # ax.plot(xline, yline, 'r')
        ax.plot3D(xline, yline, zline, 'red')
        
ani = FuncAnimation(plt.gcf(),animate,interval = 100)
# ax.view_init(elev=20., azim=-35, roll=0)
plt.show()