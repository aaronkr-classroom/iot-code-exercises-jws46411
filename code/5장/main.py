#main.py

from device import SensorDevice, ActuatorDevice, TempertureSensor, LightSensor

sensor = sensorDevice("Temp sensor")
actuator = ActuatorDevice("Led controller")

sensor.connect()
actuactor.connect()

print(sensor.staus())
print(actuator.staus())
print()

temp = TemperatureSensor("Temp1")
light = LightSensor("Light1")

print("Temp : ", temp.read())
print("Light: ", light.read())