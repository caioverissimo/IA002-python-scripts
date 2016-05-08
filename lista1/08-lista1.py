### IAL002 - Primeira Lista
### 8. Escreva um programa que apresente todos os valores inteiros divisíveis por 5 
### situados entre um valor mínimo e um máximo, fornecidos pelo usuário. É obrigatório que 
### o valor máximo seja maior que o mínimo e se isso não ocorrer, deve ser dada uma mensagem 
### de erro ao usuário.


### Show all the divisible per '5' between a minimum and a maximum given ###

print('\n');
print("### Show all the divisible per '5' between a minimum and a maximum given ###")
print("### -------------------------------------------------------------------- ###")
print('\n');

# Variables declaration and initializing
rangeDivisiblePer5 = []

# Ask for enter a value (minimum) until be integer
while True :
    try :
        minimum = int( input( "Type a minimum number for a range (Please, enter an integer): " ) )
        if ( isinstance( minimum, int )) :
            print("\n")
            break

    except ValueError :
        print("This value is not an int!")
        print("\n")


# Ask for enter a value (maximum) until be integer
while True :
    try :
        maximum = int( input( "Type a maximum number for a range  (Please, enter an integer): " ) )
        if ( isinstance( maximum, int )) :
            print("\n")
            break

    except ValueError :
        print("This value is not an int!")
        print("\n")


# Verify all numbers between minimum and maxim divisible per '5' and add to a list
currentTerm = minimum
while currentTerm <= maximum :
	if ( ( currentTerm % 5 ) == 0 ) :
		rangeDivisiblePer5.append(currentTerm)
	currentTerm += 1

	
# Shows the list of terms between minimum and maximum divisibles per '5'
print( "###RESULT###" )
print( "This is the range between", minimum ,"and", maximum, ": " )
print( rangeDivisiblePer5 )


print("\n")
print("##### :-) Thanks for your patience! See ya!!! ;-) ###")


#print("Magic happens here!")