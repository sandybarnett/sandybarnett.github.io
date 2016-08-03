import matplotlib.pyplot as plt
import os.path

#Choose name to check
time=801

#seting the directory to currently
directory = os.path.dirname(os.path.abspath(__file__))  

filename = os.path.join(directory, 'stop_times.txt')
datafile = open(filename,'r')
next(datafile)

times=[]
stops=[]

for line in datafile:
    #..seperates comma deliminated file
    splitline = line.split(',')
    departure_time = splitline[2]
    departure_time= departure_time.split(":")
    departure_time= int(departure_time[0]+departure_time[1])
    stopid = splitline[3]
    streetname = splitline[5]
    if time==departure_time:
        times.append(departure_time)
        stops.append(stopid)
datafile.close()

#open stop locations to get gps coordinates
filename = os.path.join(directory, 'stops.txt')
datafile = open(filename,'r')
next(datafile)

longs=[]
lats=[]
errors=[]
for line in datafile:
    splitline = line.split(',')
    stop_id = splitline[0]
    if len(splitline)==9:
        latitude = splitline[4]
        longitude = splitline[5]
        for item in stops:
            if item==stop_id:
                longs.append(float(longitude))
                lats.append(float(latitude))
                break
    else:
        errors.append(splitline)     


fig, ax = plt.subplots(1,1)
ax.plot(longs, lats,'bs')
ax.set_title("Bus Stops at "+str(time)+" in the Greater Chicago Area (Mapped by GPS)")
fig.show()
