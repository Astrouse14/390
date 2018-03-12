import math
import matplotlib.pyplot as plt
import numpy

BASS_P = 0.003 # p parameter for Bass model
BASS_Q = 0.7 # q parameter for Bass model
GROWTH = 0.007 # growth of the number of miles travelled
MILES = 3130509 # millions of miles travelled from DOT
REG_RATIO = 0.01054142011 # number of fatalities with regular miles travelled
AV_FRACTION = 0.1 # the percentage of the ratio with automous vehicles

def bass_model(p, q, t):
	"""
	This is the generic Bass model that takes p, q, and computes
	the end result at time t periods from now
	"""
	a = q/p
	b = p+q
	x = math.exp(-1 * b * t)
	y = 1 + a * x
	bass = (b ** 2 * x) / (p * y ** 2)
	return bass

def main():
	"""
	The main script of the program.
	"""
	i = 0
	miles = [MILES]
	new = [0]
	avmiles_mid = [0]
	while i < 30:
		miles.append(miles[i]*(1 + GROWTH))
		i = i + 1
		new.append(bass_model(0.003, 0.7, i))
		cumulative = numpy.sum(new)
		avmiles_mid.append(cumulative * miles[i])
	i = 0
	miles = [MILES]
	new = [0]
	avmiles_low = [0]
	while i < 30:
		miles.append(miles[i]*(1 + GROWTH))
		i = i + 1
		new.append(bass_model(0.001, 0.5, i))
		cumulative = numpy.sum(new)
		avmiles_low.append(cumulative * miles[i])
	i = 0
	miles = [MILES]
	new = [0]
	avmiles_high = [0]
	while i < 30:
		miles.append(miles[i]*(1 + GROWTH))
		i = i + 1
		new.append(bass_model(0.005, 0.9, i))
		cumulative = numpy.sum(new)
		avmiles_high.append(cumulative * miles[i])
	plt.plot(avmiles_mid, 'r')
	plt.plot(avmiles_low, 'g')
	plt.plot(avmiles_high, 'b')
	plt.show()

if __name__ == "__main__":
	main()

