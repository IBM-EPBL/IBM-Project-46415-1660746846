import random
while(True):
    temp=random.randint(10,99)
    humidity=random.randint(10,99)
    print("current temperature:",temp)
    print("current humidity:",humidity,"%")
    temp_ref=50
    humidity_ref=60
    if temp>temp_ref and humidity<humidity_ref:
        print("Turn on the Alarm")
    else:
        print("Turn off the Alarm")
    break
