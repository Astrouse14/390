reg_ratio = 0.01054142011 #global variable that looks at the
pop_growth = 0.007
aut_growth = 0.2

def getFatalities(end_year, start_year, reg_miles, aut_miles):
	i = start_year
	tot_miles = reg_miles + aut_miles
	aut_ratio = (0.1)*reg_ratio #a key assumption of the model
	while i < end_year:
		i = i+1
		growth = (aut_miles * (1 + aut_growth))
		switch = ((aut_miles * tot_miles)/reg_miles)
		if i > 2030:
			aut_miles = growth
		else:
			aut_miles = growth + switch
		tot_miles = tot_miles * (1 + pop_growth)
		reg_miles = tot_miles - aut_miles
	fatalities = reg_miles * reg_ratio + aut_miles * aut_ratio
	return fatalities


def main():
	"""
	The main script of the program.
	"""
	year=2017
	reg_miles=3130508 #from DOT, in millions
	aut_miles=1 #we know it is a small number
	i = 0
	end_year = 2050
	fatalities=getFatalities(end_year, year, reg_miles, aut_miles)
	print end_year, int(fatalities)

if __name__ == "__main__":
	main()
