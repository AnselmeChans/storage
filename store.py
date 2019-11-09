import datetime
import csv




class DateTimeEventStore: 
    
    def __init__(self): 
        self.store = {}
    
    def store_event(self, at, data):
        """
            Function that store event at a specific time
        :param at: specific datime
        :type at: datetime
        :param data: specific data
        :type data: str  
        """
        self.store[at] = data
    
    def get_events(self, start, end):
        """
            Get all the event between a start date to a end date
        :param start: start datetime 
        :type start: datetime
        :param end: end datetime 
        :type end: datetime
        :return: list of data
        :type return: list
        
        """
        try:
            return [item for key, item in self.store.items() if start <= key <= end]
        except ValueError as err:
            print(err)    

    def store_event_csv(self, at, data): 
        """
            Function that store event at a specific time into a csv file
        :param at: specific datime
        :type at: datetime
        :param data: specific data
        :type data: str  
        """
        try:
            with open('store_event.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                for key, value in self.store.items():
                    writer.writerow([key, value])
        except Exception as e:
            print(e)
    
    def get_event_csv(self, start, end): 
        """
            Get all the event to a csv file between a start date to a end date
        :param start: start datetime 
        :type start: datetime
        :param end: end datetime 
        :type end: datetime
        :return: list of data
        :type return: list
        
        """
        
        result = []
        try:
            with open('store_event.csv', 'r') as csvFile:
                reader = csv.reader(csvFile)
                result.append(result)

                for row in reader:
                    print(row[0])
                    
                    datetime_object = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')

                    if start <= datetime_object <= end:
                        result.append(row)
            return result
        except FileNotFoundError: 
            print("File not found. Please try again.")
        except IOError:
            print("There was an IOError opening the file. Please try again.")