import math
import matplotlib.pyplot as plt
import numpy

BASS_P = 0.003 # p parameter for Bass model
BASS_Q = 0.7 # q parameter for Bass model
GROWTH = 0.007 # growth of the number of miles travelled
MILES = 3130509 # millions of miles travelled from DOT
REG_RATIO = 0.01054142011 # number of fatalities with regular miles travelled
AV_FRACTION = 0.1 # the percentage of the ratio with automous vehicles

def BassModel(p, q, t):
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
	avmiles = [0]
	regmiles = [(MILES - 1)]
	while i < 30:
		miles.append(miles[i]*(1 + GROWTH))
		i = i + 1
		new.append(BassModel(BASS_P, BASS_Q, i))
		cumulative = numpy.sum(new)
		avmiles.append(cumulative * miles[i])
		regmiles.append(miles[i] - avmiles[i])
	totaldeaths = numpy.sum(regmiles)*REG_RATIO + numpy.sum(avmiles)*REG_RATIO*AV_FRACTION
	print int(totaldeaths)

if __name__ == "__main__":
	main()

