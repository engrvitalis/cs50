"""
This program prompts the user for a fraction, formatted as X/Y, 
wherein each of X and Y is an integer, and then outputs, as a 
percentage rounded to the nearest integer, how much fuel is in the tank. 
If, though, 1% or less remains, output E instead to indicate that the 
tank is essentially empty. And if 99% or more remains, output F instead 
to indicate that the tank is essentially full.
"""

def main():
	while True:
		ans = input("Fraction: ").split("/")

		# check for integers
		try:
			x = int(ans[0])
			y = int(ans[1])
		except:
			continue

		# check for improper fraction
		if x > y:
			continue

		try:
			print(fuel_level(x, y))
			break
		except ZeroDivisionError:
			pass

def fuel_level(x, y):
	 f = round(x / y * 100)

	 if f <= 1:
	 	return "E"
	 elif f >= 99:
	 	return "F"
	 else:
	 	return f'{f}%'	 	

main()
