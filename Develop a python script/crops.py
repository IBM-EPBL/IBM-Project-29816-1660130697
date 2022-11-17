import ibmiotf.application
import ibmiotf.device
import time
import random
import sys

# watson device details

organization = "nhen55"
devicType =  "Crops"
deviceId = "Crops1"
authMethod= "token"
authToken= "123456789"

#generate random values for randomo variables (temperature&humidity)



def myCommandCallback(cmd):
    print("command recieved:%s" %cmd.data['command'])
    print(cmd)
try:
        deviceOptions={"org": organization, "type": devicType,"id": deviceId,"auth-method":authMethod,"auth-token":authToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
        print("caught exception connecting device %s" %str(e))
        sys.exit()

#connect and send a datapoint "temp" with value integer value into the cloud as a type of event for every 10 seconds
deviceCli.connect()

while True:
        #get sensor data from DHT11
        Temp= random.randint(0,100)
        Humd= random.randint(0,100)
        data= {'temp':Temp,'humid':Humd}
        #print(data)
        def myOnPublishCallback():
            print("published Temperature = %s c" %Temp,"humidity:%s %%" %Humd)
        success=deviceCli.publishEvent ("IoTSensor","json",data,qos=0,on_publish= myOnPublishCallback)
           
        if not success:
            print("not connected to ibmiot")
        time.sleep(5)

deviceCli.commandCallback=myCommandCallback
#disconnect the device
deviceCli.disconnect()
