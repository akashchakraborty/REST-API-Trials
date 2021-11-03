import requests
import threading
import json
import time
import random
import logging
import sys
import datetime
val = 0
val1 = 0
val2 = 0
val3 = 0
val4 = 0

########################################### Logger Settings ########################################
filename = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.%f")+"LOG.log"
print("RECORDS Storage at : ",filename)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler(filename)
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter_f = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter_c = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter_f)
ch.setFormatter(formatter_c)	
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

########################################## Working Function #########################################
def thingspeak_post():
    #threading.Timer(15,thingspeak_post).start() #
    global val    
    global val1
    global val2
    global val3
    global val4

    val=random.randint(1,30)  
    val1=random.randint(31,60)
    val2=random.randint(61,90) 
    val3=random.randint(91,120)
    val4=random.randint(121,151)

    URl='https://api.thingspeak.com/update?api_key='
    KEY='X2HWV93MX66WQLXK'
    HEADER='&field1={}&field2={}&field3={}&field4={}&field5={}'.format(val,val1,val2,val3,val4)
    NEW_URL = URl+KEY+HEADER
    #print(NEW_URL)
    requests.get(NEW_URL)
    channelID='1555205'
    status = requests.get("https://api.thingspeak.com/channels/{}/status".format(channelID))
    # print(status)
    # data=urllib.request.urlopen(NEW_URL)
    # print(data)
    return status
    
if __name__ == '__main__':
    while True:
        try:
            status=thingspeak_post()
            status=(str(status))
            if "200" in status:
                logger.info("DATA SENT TO SERVER:: FIELD 1: {}, FIELD 2: {}, FIELD 3: {}, FIELD 4: {}, FIELD 5: {}".format(val,val1,val2,val3,val4))
                logger.info("ACK OK")
                logger.info("WAITING 15 SECONDS...")
                time.sleep(15)
            else:
                logger.error("Response is NOT-OK")
                time.sleep(15)
        except Exception as e:
            logger.error("Error Occurred: {}".format(e))