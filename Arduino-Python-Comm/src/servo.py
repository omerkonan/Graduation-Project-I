import serial
import time

class Servo:
	def __init__(self, angle_step = 15 , wtime = 2):
		self.angle_step = angle_step
		self.wtime = wtime
		self.boudrate = 9600
		self.timeout = 1
		self.stopbits = 1.5
		self.port_path = "/dev/ttyACM0"
	def send_msg(self):

		port = serial.Serial(self.port_path,self.boudrate, \
			timeout = self.timeout, stopbits=self.stopbits)

		port.write(b'0')
		time.sleep(3)
		i = 0

		while (True):
			port.write(str(i).encode('utf-8'))
			print("\'{}' message sent.".format(i))
			
			time.sleep(self.wtime)
			if i == 180:
				i = 0 
			i = i + self.angle_step

