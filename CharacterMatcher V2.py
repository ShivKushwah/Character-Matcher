from random import randint
import random
import string
#Problem - Change a string to a different string using genetic algorithms
# Generate population of random strings of length of Input String (strToMatch)
# Choose best string (closest to strToMatch) and generate new population based on point mutating best string randomly


#TO USE: start() starts the program, restart() resets the program


####################################################
population = []
strToMatch = 'GeneticAlgorithm'
SIZE_POPULATION = 99

##########################################

#initialize population and start program
def start():
	i = 0
	temp = 'a'
	

	while len(temp) != len(strToMatch):
		temp += 'a'


	while i < SIZE_POPULATION:
		population.append(randomStringGenerator(temp)) #generates population with point mutations of initial string
		i = i + 1
	#population initialized 


	counter = 0
	temp2 = bestString()  

	while temp2 != list(strToMatch): #final condition

		print(temp2, counter)
		reproduce(temp2) 
		temp2 = bestString() #choose best string in new population
		counter += 1

	print(temp2, counter)
	return "Finished"

def restart(): #resets program to initial state
	global population
	population = []
	

def bestString(): #finds best string in population (closest to strToMatch)
	temp = [i for i in population]
	counter = 0
	while counter < len(population):
		temp[counter] = stringCompareTo(population[counter],strToMatch)
		counter = counter + 1
	maxFit = 0 
	indexOfMaxFit = 0
	currIndex = 0
	while currIndex < len(temp):
		if temp[currIndex] > maxFit:
			maxFit = temp[currIndex]
			indexOfMaxFit = currIndex
		currIndex = currIndex + 1
	return population[indexOfMaxFit]


def stringCompareTo(str1, str2): #compares two strings and returns how close they are to each other(int value)
	set1 = list(str1)
	set2 = list(str2)
	compareValue = 0
	for i in range(len(str1)):
		if set1[i] == set2[i]:
			compareValue = compareValue + 1
	return compareValue



def randomStringGenerator(strk): #generates random string based on point mutating parameter string
	strk = list(strk)
	randomNum = randint(0,len(strk)-1)
	strk[randomNum] = random.choice(string.ascii_letters) 
	return strk 

def reproduce(k): #creates new population based on point mutating best string
	i = 0
	while i < SIZE_POPULATION:
		population.append(randomStringGenerator(k))
		i = i + 1
