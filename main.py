from machine import Pin, I2C, ADC, UART
from time import sleep, sleep_ms
from machine_i2c_lcd import I2cLcd
import utime
from dht import DHT11, InvalidChecksum

uart = UART(0,9600)

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)

addr = i2c.scan()[0]
# print(hex(addr[0]))

lcd = I2cLcd(i2c, addr, 2, 16)

sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

#dhtsensor = Pin(15, Pin.PULL_DOWN)
dhtsensor = Pin(15, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(dhtsensor)
led = Pin(26, Pin.OUT)

def run_lcd():
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print (temperature)
    lcd.clear()
    lcd.putstr("Hello!\n")
    lcd.putstr("CPU Temp:%.2f" % temperature)
    #utime.sleep(2)
    #sleep(1)
    
def run_light():
    led.value(1)

def run_thermo():
    t = sensor.temperature
    h = sensor.humidity
    print("Temperature: {}".format(t))
    print("Humidity: {}".format(h))

def bluetooth():
    while True:
        if uart.any():
            command = uart.readline()
            print(command)   # uncomment this line to see the recieved data
            if command==b'\x31':
                led.high()
                print("ON")
            elif command==b'\x30':
                led.low()
                print("OFF")

if __name__ == "__main__":
    while True:
        sleep(5)
        run_lcd()    
        #run_light()
        run_thermo()
        #print (dht.Andy)
        bluetooth()
        sleep(2)
