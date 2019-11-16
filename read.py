import csv
import DataTypes
import operator


#Public variables which are needed for putting the directories
carbonMonoxide = []
nitricOxide = []
nitrogenDioxide = []
relativeHumidity = []
temperature = []

def read():
    with open("data.csv") as file:
        data = csv.reader(file) #read file
        row_line = 0 #the row line
        for row in data:
            if row_line > 0: #for all rows greater than 0
                for i in range(7):
                    if i == 0: #To collect carbon monoxide
                        timeStamp = row[7].split(' ') #to get the data
                        add = DataTypes.Carbon_Monoxide(row[0], timeStamp[1], timeStamp[0])
                        carbonMonoxide.append(add)
                    if i == 1:
                        timeStamp = row[7].split(' ')
                        add = DataTypes.Nitric_Oxide(row[i], timeStamp[1], timeStamp[0])
                        nitricOxide.append(add)
                    if i == 2:
                        timeStamp = row[7].split(' ')
                        add = DataTypes.Nitrogen_Dioxide(row[i], timeStamp[1], timeStamp[0])
                        nitrogenDioxide.append(add)
                    if i == 3:
                        timeStamp = row[7].split(' ')
                        add = DataTypes.Relative_Humidity(row[i], timeStamp[1], timeStamp[0])
                        relativeHumidity.append(add)
                    if i == 4:
                        timeStamp = row[7].split(' ')
                        add = DataTypes.Temperature(row[i], timeStamp[1], timeStamp[0])
                        temperature.append(add)

            row_line += 1

    file.close()

#To read the file
def createfile(fileName, arrayData):
    with open(fileName, "w") as file:
        for data in arrayData:
            file.write(data.value+"\n")

read() #calls the read function
#Here we are sorting
carbonMonoxide.sort(key=operator.attrgetter('date'))
nitricOxide.sort(key=operator.attrgetter('date'))
nitrogenDioxide.sort(key=operator.attrgetter('date'))
relativeHumidity.sort(key=operator.attrgetter('date'))
temperature.sort(key=operator.attrgetter('date'))

#Here we are creating a file
createfile("carbonMonoxide.csv", carbonMonoxide)
createfile("nitricOxide.csv", nitricOxide)
createfile("nitrogenDioxide.csv", nitrogenDioxide)
createfile("relativeHumidity.csv", relativeHumidity)
createfile("temperature.csv", temperature)

