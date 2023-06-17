# import numpy as np
# import matplotlib.pyplot as plt
# import serial
# import time 
# from matplotlib.animation import FuncAnimation

# fig = plt.figure()
# N = 10 #numbers of value in x direction

import matplotlib.pyplot as plt
import numpy as np
import serial
import time 
from matplotlib.animation import FuncAnimation

# Define X and Y data
N=20
# Create figure and axis objects
fig, ax = plt.subplots()


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
        # Plot data
        ax.clear()  
        ax.plot(xline, yline, 'red')

# Add title, axes labels, and legend
ax.set_title('Position tracking!')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
ani = FuncAnimation(plt.gcf(),animate,interval = 50)

# Show or save the plot
plt.show()