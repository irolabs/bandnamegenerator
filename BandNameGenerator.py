from termcolor import colored
print("Welcome to Band Name Generator")
inputCity = input("Where do you live?\n")
inputPet = input("What is your favorite animal?\n")
print("This is your recommended band name\n")
printBandName = colored(inputCity+" "+inputPet,attrs=['bold'],color='green')
print(printBandName)