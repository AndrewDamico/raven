Sprint 1

RAVEN Test Board

Power Supply: 5V
Pico Test Board (H)
	Bluetooth
	Ultrasonic Ranger
	Temp Readings
	Motor Setup
	Infrared Camera
	Screen

User Stories
	Communicate with Owl over Bluetooth (or Wireless?)
	Send Range over TTY
	Send IR readings over TTY
	Build Motor
	Control Motor (On-Device Script)
	Store readings in Database

[VIPER Setup]
	Get Pins
	Output Pins
	Output Image
	Connect to OWL
	Save Images to DB
	Save Pins to DB

[A2dam Setup]
	Access Database
	Marry Pins, Images, Readings
	Train Gann
	Test Gann
	
[LLED Distancing]
	LLED for Calibration
	Send LLED Distance


RAVEN Module

Multiple Sensors
Motor Assembly for IR

Input: 
	Bluetooth (Uses 1 UART): Used to send data to the OWL.
	Wifi? (Uses 1 UART?)
	Serial? (Would need to use an UART) – Nice to read output?

Requirements: 
1. Needs to be able to receive programming data from the RAVEN controller.
	a. Can this be done via wireless or Bluetooth?
2. Needs external ports to be able to control external modules (such as the motor)
3. LED? Nice to debug?
4. 



RAVEN Controller 

Requirements:

Screen and Input Buttons
Battery and UPS – Needed since we will need to calibrate each RAVEN upon install
40 PIN output? Nice to work on projects since the micro controller is inside box

	
