### IAL002 - Primeira Lista
### 7. Escreva um programa que calcule os N primeiros termos de uma PG com razão R e 
###	primeiro termo P1 fornecidos palo usuário. Também deve ser calculada e apresentada a 
###	soma desses N termos. 

### Calculates the sum of geometric progression given N of terms, the ratio R and first term P1 ###

print('\n');
print("### Calculates the sum of geometric progression given N of terms, the ratio R and first term P1 ###")
print("### ---------------------------------------------------------------------------------- ###")
print('\n');

# Variables declaration and initializing
sumOfProgression = 0
firstTermsList = []
count = 1

# Ask for enter a value (Number of terms) until be integer
while True :
    try :
        numberOfFirstTerms = int( input( "How many Geometric Progression first terms do you want calculate the sum? (Please, enter an integer): " ) )
        if ( isinstance( numberOfFirstTerms, int )) :
            print("\n")
            break

    except ValueError :
        print("This value is not an int!")
        print("\n")


# Ask for enter a value (Ratio) until be integer
while True :
    try :
        ratio = int( input( "Which ratio has the 'Geometric Progression'?: " ) )
        if ( isinstance( ratio, int )) :
            print("\n")
            break

    except ValueError :
        print("This value is not an int!")
        print("\n")

# Ask for enter a value (First Term) until be float
while True :
    try :
        firstTerm = float( input( "Which is the 'Geometric Progression' first term? (Please, enter an integer): " ) )
        if ( isinstance( firstTerm, float )) :
            print("\n")
            break

    except ValueError :
        print("This value is not an real!")
        print("\n")


# add the first term to the list of terms
firstTermsList.append(firstTerm)


# Creates a list of all N first terms
while ( count < numberOfFirstTerms ) :
	
	count += 1
	currentTermPosition = count+1
	# a[n] = a[1] * q**(n-1) (o termo N de uma PG)
	currentTerm = firstTerm * ( ratio ** ( (currentTermPosition)-1 ) )
	firstTermsList.append(currentTerm)
	


# Calculates the sum of N first terms
sumOfProgression = ( firstTerm * ( ( ratio ** numberOfFirstTerms ) - 1 ) ) / ( ratio - 1)

		
# Verify and write if the number is 'positive' or 'negative'
print( "###RESULT###" )
print( "This is the Geometric Progression first", numberOfFirstTerms ,"numbers:" )
print( firstTermsList )
print( "The sum of these first terms: " )
print( sumOfProgression )


print("\n")
print("##### :-) Thanks for your patience! See ya!!! ;-) ###")


#print("Magic happens here!")