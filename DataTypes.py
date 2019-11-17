import datetime
'''
This files is used to store the data types.
'''

class Data(object):
    '''
    A class which creates the types.
    :return:
    '''
    def __init__(self, value, time, date):
        self.value = float(value)
        #changing format into time
        formatTime = time.split(':')
        self.time = datetime.time(int(formatTime[0]), int(formatTime[1]), int(formatTime[2]))
        #changing format into date
        formatDate = date.split('/')
        self.date = datetime.date(int(formatDate[2]),int(formatDate[1]), int(formatDate[0]))





class Carbon_Monoxide(Data):
    '''
    :param Data: has attributes for the data times
    :return: non
    '''
    def __init__(self, value, time, date):
        super().__init__(value, time, date)  #calls the super method


class Nitric_Oxide(Data):
    '''
    This will create a type of the data nitric oxide
    :param Data:
    :return:
    '''
    def __init__(self, value, time, date):
        super().__init__(value, time, date)



class Nitrogen_Dioxide(Data):
    '''
    This will create a type of the data nitrogen dixoide
    :param Data:
    :return:
    '''
    def __init__(self, value, time, date):
        super().__init__(value, time, date)



class Relative_Humidity(Data):
    '''
    This will create a type called relative humidity
    :param Data:
    :return:
    '''
    def __init__(self, value, time, date):
        super().__init__(value, time, date)


class Temperature(Data):
    def __init___(self, value, time, date):
        super().__init__(value, time, date)