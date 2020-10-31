from models.Async import Async
import paho.mqtt.client as mqtt
import ctypes, os
import models.Async

#Checking with DPI for OS being windows
#We don't want to interpret the code on Macs, Linux or Others...

if os.name == "nt":
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

print("Boba Fett")

broker = "127.0.0.1"


        
class MqttBroker():
    #this will be the broker Class for the 
    #app
    
    broker = ""
    
    def __init__(self, br):
        self.broker = br
        
    

class Demo_Main():
    
    client = None
    broker = None
    
    def __init__(self, br):
        
        broker = br
        print("Trying To Load Main")
        print(".")
        print("..")
        print("...")
        
        br = MqttBroker(broker)
        br = br.broker
        
        #//print(br)
        
        self.client = mqtt.Client("WorkShopIo")
        #Async(func = self.client.connect(br, 1883))#where 1883 is the port
        
        self.client.connect(br,1883)
        

  


    
    





