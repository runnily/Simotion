from matplotlib import pyplot as plt
import datetime
import read


#To create the graph

#Our public variables which we are sorting by dates
read.sort(read.carbonMonoxide, "date")
read.sort(read.nitrogenDioxide, "date")
read.sort(read.nitricOxide, "date")
read.sort(read.relativeHumidity, "date")
read.sort(read.temperature, "date")


def fetchValues(array):
    #To fetch the values in the data
    values = []
    for n in array:
        values.append(n.value)
    values.sort()
    return values

def fetchTime(array):
    #Same thing as fetch value but this time fetching the times
    times = []
    for n in array:
        times.append(datetime.datetime.combine(n.date, datetime.time(0,0,0)))
    return times

#This gets the x axises
x = fetchTime(read.nitrogenDioxide)
SMALL_SIZE = 8

#This is for figure 1; carbon monoxdes
plt.figure(1)
plt.title("Carbon Monoxde")
plt.plot(x,fetchValues(read.carbonMonoxide))
plt.rc('font', size=SMALL_SIZE)
plt.xlabel("Time")
plt.ylabel("Values")

#This is for figure 2; Nitrogen dioxide
plt.figure(2)
plt.title("Nitrogren Dioxide")
plt.plot(x,fetchValues(read.nitrogenDioxide), 'b-')
plt.rc('font', size=SMALL_SIZE)
plt.xlabel("Time")
plt.ylabel("Values")


#This is for figure 3; Nitric oxide
plt.figure(3)
plt.title("Nitric Oxide")
plt.plot(x,fetchValues(read.nitricOxide), 'g-')
plt.rc('font', size=SMALL_SIZE)
plt.xlabel("Time")
plt.ylabel("Values")

#This is for figure 4; relative humidity
plt.figure(4)
plt.title("Relative Humidity")
plt.plot(x, fetchValues(read.relativeHumidity), 'y-')
plt.rc('font', size=SMALL_SIZE)
plt.xlabel("Time")
plt.ylabel("Values")

plt.figure(5)
plt.title("Temperature")
plt.plot(x, fetchValues(read.temperature),'r-')
plt.rc('font', size=SMALL_SIZE)
plt.xlabel("Time")
plt.ylabel("Values")
plt.show()

