import os

#Check cpu load average

cpu_load = os.getloadavg()
print("CPU Load Average: ", cpu_load[0], cpu_load[1], cpu_load[2])
