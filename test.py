import read

#This repeated lines of code are used for sorting our arrays by date
read.sort(read.carbonMonoxide, "date")
read.sort(read.nitrogenDioxide, "date")
read.sort(read.nitricOxide, "date")
read.sort(read.relativeHumidity, "date")
read.sort(read.relativeHumidity, "date")

#This is used print the data for testing
print(read.carbonMonoxide)
print(read.nitrogenDioxide)
print(read.nitricOxide)
print(read.relativeHumidity)
print(read.temperature)


#This is to print our values to see if its sorted
def printData(array):
    for n in array:
        text = "Value: {} Date: {} Time: {}".format(n.value, n.date, n.time)
        print(text)


printData(read.carbonMonoxide)
printData(read.nitrogenDioxide)
printData(read.nitricOxide)
printData(read.relativeHumidity)
printData(read.temperature)

#Used to create the files
read.createfile("carbonMonoxide.csv", read.carbonMonoxide)
read.createfile("nitricOxide.csv", read.nitricOxide)
read.createfile("nitrogenDioxide.csv", read.nitrogenDioxide)
read.createfile("relativeHumidity.csv", read.relativeHumidity)
read.createfile("temperature.csv", read.temperature)
