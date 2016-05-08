### IAL002 - Primeira Lista
### 4. Escreva um programa que leia valores numéricos inteiros e totalize separadamente 
###	os positivos e os negativos até que o usuário digite 0. Ao final mostre na tela esses 
### dois totais.

### Program for calculate total of positives and negatives integer numbers ###

###	weightCategory = {

###		"Menor que 65kg": 								"Pena",
###		"Maior ou igual a 65 kg e menor que 72 kg": 	"Leve",
###		"Maior ou igual a 72 kg e menor que 79 kg": 	"Ligeiro",
###		"Maior ou igual a 79 kg e menor que 86 kg": 	"Meio médio",
###		"Maior ou igual a 86 kg e menor que 93 kg": 	"Médio",
###		"Maior ou igual a 93 kg e menor que 100 kg": 	"Meio pesado",
###		"Maior ou igual a 100 kg": 						"Pesado"

###	}



print('\n');
print("### Program for calculate total of positives and negatives integer numbers ###")
print("### ---------------------------------------------------------------------- ###")
print('\n');


# Variables declaration and initializing
askForNewEntrance = 1
positiveEntryList = [];
negativeEntryList = [];
totalPositiveNumbers = 0;
totalNegativeNumbers = 0;


# Ask for new entry until the user types '0'
while ( askForNewEntrance != 0 ) :

	# Ask for enter values until be integer
	while True :
	    try :
	        currentEntryValue = int( input( "Please, enter an integer number: " ) )
	        if ( isinstance( currentEntryValue, int )) :
	            print("\n")
	            break

	    except ValueError :
	        print("This value is not an int!")
	        print("\n")
	# add current entry value in the separate list
	if ( currentEntryValue > 0 ) :
		positiveEntryList.append(currentEntryValue)
	elif ( currentEntryValue < 0 ) :
		negativeEntryList.append(currentEntryValue)
	# update the exit controller in case of '0'
	if ( currentEntryValue == 0 ) :
		askForNewEntrance = 0


# calculate sum of numbers (positives and negatives)
for number in positiveEntryList :
	totalPositiveNumbers += number

for number in negativeEntryList :
	totalNegativeNumbers += number


# Verify and write if the number is 'positive' or 'negative'
print( "###RESULT###" )
print( "This is the positive numbers:" )
print( positiveEntryList )
print( "This positive numbers totalize: " )
print( totalPositiveNumbers )

print( "This is the negative numbers:" )
print( negativeEntryList )
print( "This negative numbers totalize: " )
print( totalNegativeNumbers )


print("\n")
print("##### :-) Thanks for your patience! See ya!!! ;-) ###")


# print("Magic happens here!")