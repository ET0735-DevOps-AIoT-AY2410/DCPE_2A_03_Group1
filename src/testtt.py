import time
import sprinkler 

sprinkler.init()
sprinkler.when_fire_detected(True) # 180     
time.sleep(2)                          
sprinkler.when_fire_detected(False) # 0