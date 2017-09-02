import time, json, curses, wiringpi


# import a class and a method by which to calibrate pulse
# https://stackoverflow.com/questions/6013844/python-init-syntax 
class Calibrator(object); 
	def __init__ (self, [arg?], pin=PIN1, calibration_file=None); 
		# super(Child, self)
		super (Calibrator, self).__init__()
			self.pin = pin
			#hadouken syntax 