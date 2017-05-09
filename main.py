### The names for each digit #################
pf1   = ['','hena','di','tri','tetra','penta','hexa','hepta','octa','ennea']
pf10  = ['','docontakai','icosicontakai','tricontakai','tetracontakai','pentacontakai','hexacontakai','heptacontakai','octacontakai','enneacontakai']
pf100 = ['','henahecta','dihecta','trihecta','tetrahecta','pentahecta','hexahecta','heptahecta','octahecta','enneahecta']
first20 = ['triangle','quadrilateral','pentagon','hexagon','heptagon','octagon','nonagon','decagon','undecagon','dodecagon','triskaidecagon','tetradecagon','pentadecagon','hexadecagon','heptadecagon','octadecagon','enneadecagon','icosagon']
##############################################

# converts digit to polygon name
def numToWord(num):
	if int(num) < 21:
		return first20[int(num) - 3]
	if len(num) == 2:
		d10 = pf10[int(num[0])]
		d1 = pf1[int(num[1])]
		return d10 + d1 + 'gon'
	else:
		d100 = pf100[int(num[0])]
		d10 = pf10[int(num[1])]
		d1 = pf1[int(num[2])]
		return d100 + d10 + d1 + 'gon'
	
### The main loop ############################
print("THE WILSONIAN POLYGON NAME GENERATOR")
print("polygon names by faculty.kutztown.edu")
print('***************************************')
#print('NOTE: You MUST enter a THREE-DIGIT number\nfor it to work, otherwise it won\'t due\nto my wonderful cable management')
print('INSTRUCTIONS: Type in the number of sides, or type \'e\' to exit.')
print('***************************************')

def main():
	polygon = input('# of sides: >> ')
	if polygon == 'e':
		print('Good day sir!')
		print('[Exited]\n')
		sys.exit()
	elif polygon == '':
		main()
	elif int(polygon) <= 0:
		print('You bad ian.')
	elif int(polygon) > 999:
		print('Numbers 1000+ are unsupported, try something else.')
	elif polygon == '26':
		print('Hello Mrs. Downey. And in fact, a 26-sided shape is actually called a ' + numToWord(polygon) + '!')
	elif int(polygon) < 3:
		print('Not a polygon, try again.')
	else:
		print('A ' + polygon + '-sided shape is called a ' + numToWord(polygon) + '.')
##############################################

import sys

while True:
	main()
