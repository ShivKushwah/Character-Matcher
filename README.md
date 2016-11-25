# Character-Matcher
Project that uses a genetics algorithm to output the string "GeneticAlgorithm"

TO USE
1.Install python3
2.Run the file using the terminal 
Example command -> (python3 -i /Users/Shiv/Desktop/Programming/Projects/Genetic\ Algorithms/Working\ Programs/CharacterMatcher\ V2.py)
3. Type start() to start the program. After running, type restart() to reset the program (you need to type start() to run the program again)

Basics of program
Program tries to change "a" (current string) into "GeneticAlgorithm"(final string). It generates populations of random strings that are similar to current string based on point mutating current string randomly. Then, it chooses the best string in the population, and generates a new population based on point mutating it randomly (this new population should be closer to the final string). This process repeats until the final string is reached. At each generation, the program prints out the best string and the generation number.
