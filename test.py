import read


print(read.carbonMonoxide) #Our array
print(read.nitrogenDioxide)
print(read.nitricOxide)
print(read.relativeHumidity)
print(read.temperature)


def printData(array):
    for n in array:
        print("Value: " + n.value + " Date: " + n.date)


printData(read.carbonMonoxide)
printData(read.nitrogenDioxide)
printData(read.nitricOxide)
printData(read.relativeHumidity)
printData(read.temperature)
