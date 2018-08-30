#!/usr/bin/env python3
# -*- encoding:utf-8 -*-


class LCD:
	import smbus
	import time
	
	def __init__(self, i2c = 1):
		self.i2c = i2c
		self.bus = self.smbus.SMBus(self.i2c)
		self.displayFunction = 0
		self.displayControl = 0
		self.displayMode = 0
		self.locateX = 0
		self.locateY = 0
		self.width = 0
		self.height = 0
		## I2C Address
		self.ADDR_LCD = (0x7C >> 1)
		self.ADDR_RGB = (0xC4 >> 1)
		## color
		self.COLOR_WHITE = 0
		self.COLOR_RED = 1
		self.COLOR_GREEN = 2
		self.COLOR_BLUE = 3
		self.REG_RED = 0x04
		self.REG_GREEN = 0x03
		self.REG_BLUE = 0x02
		self.REG_MODE1 = 0x00
		self.REG_MODE2 = 0x01
		self.REG_OUTPUT = 0x08
		## command
		self.LCD_CLEARDISPLAY = 0x01
		self.LCD_RETURNHOME = 0x02
		self.LCD_ENTRYMODESET = 0x04
		self.LCD_DISPLAYCONTROL = 0x08
		self.LCD_CURSORSHIFT = 0x10
		self.LCD_FUNCTIONSET = 0x20
		self.LCD_SETCGRAMADDR = 0x40
		self.LCD_SETDDRAMADDR = 0x80
		## flags for display entry mode
		self.LCD_ENTRYRIGHT = 0x00
		self.LCD_ENTRYLEFT = 0x02
		self.LCD_ENTRYSHIFTINCREMENT = 0x01
		self.LCD_ENTRYSHIFTDECREMENT = 0x00
		## flags for display on/off control
		self.LCD_DISPLAYON = 0x04
		self.LCD_DISPLAYOFF = 0x00
		self.LCD_CURSORON = 0x02
		self.LCD_CURSOROFF = 0x00
		self.LCD_BLINKON = 0x01
		self.LCD_BLINKOFF = 0x00
		## flags for display/cursor shift
		self.LCD_DISPLAYMOVE = 0x08
		self.LCD_CURSORMOVE = 0x00
		self.LCD_MOVERIGHT = 0x04
		self.LCD_MOVELEFT = 0x00
		## flags for function set
		self.LCD_8BITMODE = 0x10
		self.LCD_4BITMODE = 0x00
		self.LCD_2LINE = 0x08
		self.LCD_1LINE = 0x00
		self.LCD_5x10DOTS = 0x04
		self.LCD_5x8DOTS = 0x00



	
	def __dell__(self):
		pass
	
	
	def begin(self, w, h):
		self.width = w
		self.height = h

		if self.height > 1:
			self.displayFunction |= self.LCD_2LINE
		self.locateX = 0
		self.time.sleep(.05)
		self.__command(self.LCD_FUNCTIONSET | self.displayfunction)
		self.time.sleep(.05)
		self.__command(self.LCD_FUNCTIONSET | self.displayfunction)
		self.time.sleep(.05)
		self.__command(self.LCD_FUNCTIONSET | self.displayfunction)
		self.time.sleep(.05)
		self.__command(self.LCD_FUNCTIONSET | self.displayfunction)
		self.time.sleep(.05)

		self.displaycontrol = self.LCD_DISPLAYON | self.LCD_CURSOROFF | self.LCD_BLINKOFF
		self.display()		



	def setRGB(self, r, g, b):
		pass
	
	def clear(self):
		self.__command(self.LCD_CLEARDISPLAY | self.displayControl)
		self.time.sleep(.05)
	
	def noDisplay(self):
		self.displayControl &= ~self.LCD_DISPLAYON
		self.__command(self.LCD_DISPLAYCONTROL | self.displayControl)
	
	def display(self):
		self.displayControl |= self.LCD_DISPLAYON
		self.__command(self.LCD_DISPLAYCONTROL | self.displayControl)
	
	def noCursor(self):
		self.displayControl &= ~self.LCD_CURSORON
		self.__command(self.LCD_DISPLAYCONTROL | self.displayControl)
	
	def cursor(self):
		self.displayControl |= self.LCD_CURSORON
		self.__command(self.LCD_DISPLAYCONTROL | self.displayControl)
	
	def noBlink(self):
		self.displayControl &= ~self.LCD_BLINKON
		self.__command(self.LCD_DISPLAYCONTROL | self.displayControl)
	
	def blink(self):
		self.displayControl |= self.LCD_BLINKON
		self.__command(self.LCD_DISPLAYCONTROL | self.displayControl)
	
	def noBlinkLED(self):
		pass
	
	def blinkLED(self):
		pass
	
	def color(self, r, g, b):
		pass
	
	def locate(self, x, y):
		pass
	
	def print(self, msg):
		pass
	
	
	def __command(self, cmd):
		self.bus.write_byte_data(self.ADDR_LCD, 0x80, cmd)
	
	def __data(self, data):
		self.bus.write_byte_data(self.ADDR_LCD, 0x40, data)
	



if __name__ == "__main__":
	o = LCD()
	o.begin(16,2)
	o.print("1234567890")
	o.clear()
