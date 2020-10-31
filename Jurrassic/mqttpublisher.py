#this is the actual file 
#this will be the publisher...

#region Importing

import clientClass
from clientClass import *


set = clientClass.Demo_Main("test.mosquitto.org")
print("Succeeded")

#this will the command Asyncronously
set.client.publish("main/heroDartmainLoop", "Hello MainLoop, Welcome To The Loop")


#endregion