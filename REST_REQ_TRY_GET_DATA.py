# GET https://api.thingspeak.com/channels/1555205/feeds.json?api_key=VNHUM0QO5QD2JJCV&results=2
import requests
import threading
import json
import time
import random
import logging
import sys
import datetime
import urllib3
http = urllib3.PoolManager()


filename = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.%f")+"LOG.log"

########################################### Logger Settings ########################################

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
def thingspeak_get_data():

    #threading.Timer(15,thingspeak_post).start() #

    URl='https://api.thingspeak.com/channels/1555205/feeds.json'

    data=http.request('GET',URl)

    # print("++++++++++++++++++++++++++")
    # print(type(data))
    # print("++++++++++++++++++++++++++")

    out = data.data
    out =out.decode('utf-8')
    out = json.loads(out)
    out_f = json.dumps(out,indent=4)
    # print(type(out_f))
    logger.info(out_f)
    
    # channelID='1555205'
    # status = requests.get("https://api.thingspeak.com/channels/{}/status".format(channelID))
    # print(status)
    # data=urllib.request.urlopen(NEW_URL)
    # print(data)
    return out_f
   



if __name__ == '__main__':

    while True:
        try:

            data=thingspeak_get_data()
            logger.info("DATA RECEIVED FROM SERVER:: {}".format(data))
            logger.info("WAITING 15 SECONDS...")

            time.sleep(15)

        except Exception as e:
            logger.error("Error Occurred: {}".format(e))
