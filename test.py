#!/usr/bin/python
# Filename: simplestclass.py

class Auto:
	def __init__(self):
		self.ort = 0

	def fahre(self):
		self.ort = self.ort + 10
		
	def getOrt(self):
		return self.ort

auto = Auto()
auto.fahre()
auto.fahre()
print(auto.getOrt())
		