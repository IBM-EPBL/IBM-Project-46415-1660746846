import random

#Assigning random temperature value to a variable t in celsius

t=random.uniform(22.0,60.0)
print("Temperature is",t)
if (t>32):
    print ("Alarm is on since the temperature is above 32 celsius")
else:
    print ("Alarm is off since the temperature is below 32 celsius")

#Assigning random humidity value to a variable h in percentage

h=random.uniform(40,100)
print ("Humidity is ",h)
if (h>65):
    print("Alarm is on since the humidity is above 65%")
else:
    print("Alarm is off since the humidity is below 65%")
