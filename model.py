import datetime
import enum

from enum import Enum

class Enchere ():
    
    def __init__(self,startdate=0,duration=0):
        self.location= "M1"
        self.startdate = datetime.datetime.now()
        self.duration = duration
        ## this value holds the latest accepted bid at each moment
        self.price = 0
        ## this value holds the name of the winner at each moment
        self.client = ""
        self.status = Enchere_Status.RUNNING
          
    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
        
    def set_status(self, status):
        self.status = status
        
    def set_client(self, client):
        self.client = client   
        
class Enchere_Status(Enum):
    INITIALIZED = 1
    RUNNING = 2
    FINISHED = 3