############
###		 ###	
##	PPf	  ##
###      ###
############

from ruuvitag_sensor.ruuvi import RuuviTagSensor
from datetime import datetime
import json

def handle_data(found_data):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + 'MAC: ' + found_data[0]) 
    res = dict((k, found_data[1][k]) for k in ['temperature', 'humidity'] 
                                        if k in found_data[1]) 

    print("Balcony "+ str(res)) 

    file = open("<path.json-file>", "a+")
    file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + 'MAC: ' + found_data[0] + " " + str(res))
    file.write("\n")
    

RuuviTagSensor.get_datas(handle_data)

file.close 





