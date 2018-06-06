import time
import utils
import model
import logging

from threading import Thread
from utils import get_log_time
from data import encheres
from model import Enchere_Status

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
        
class CronJobSeconds(Thread):
 
    def __init__(self, secondsToSleep):
        ''' Constructor. '''
        Thread.__init__(self)
        self.secondsToSleep = secondsToSleep
 
    def run(self):
        time.sleep(self.secondsToSleep)
        id =int(self.getName())
        ts = get_log_time()
        enchere = encheres[id]
        enchere.set_status(Enchere_Status.FINISHED)
        logger.info('[INFO] %s CRONJOB: Close bid with id %s ',ts,id)