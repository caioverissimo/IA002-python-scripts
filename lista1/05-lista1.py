### IAL002 - Primeira Lista
### 5. Escreva um programa que leia um número inteiro N e em seguida leia N números reais, 
###	calculando a soma de todos os valores digitados.

### Program for calculate total of determined-by-user number of values ###

print('\n');
print("### Program for calculate total of determined-by-user number of values ###")
print("### ------------------------------------------------------------------ ###")
print('\n');

# Variables declaration and initializing
entriesNumber = 0
count = 0
entriesList = []
sumOfEntries = 0

# Ask for enter a value (number of entries) until be integer
while True :
    try :
        entriesNumber = int( input( "How many numbers do your want to type? (Please, enter an integer): " ) )
        if ( isinstance( entriesNumber, int )) :
            print("\n")
            break

    except ValueError :
        print("This value is not an int!")
        print("\n")

# Ask for new [entryNumber] real values
while ( count < entriesNumber ) :

	# Ask for enter values until be real
	while True :
	    try :
	        currentEntryValue = float( input( "Please, enter an real number: " ) )
	        if ( isinstance( currentEntryValue, float )) :
	            print("\n")
	            break

	    except ValueError :
	        print("This value is not an real!")
	        print("\n")

	# add current entry value in the separate list
	entriesList.append(currentEntryValue)
	count += 1
	
		
# calculate sum of numbers
for number in entriesList :
	sumOfEntries += number
# Verify and write if the number is 'positive' or 'negative'
print( "###RESULT###" )
print( "This is the numbers:" )
print( entriesList )
print( "This numbers totalize: " )
print( sumOfEntries )


print("\n")
print("##### :-) Thanks for your patience! See ya!!! ;-) ###")


#print("Magic happens here!")