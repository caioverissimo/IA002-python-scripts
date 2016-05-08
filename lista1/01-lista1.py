### IAL002 - Primeira Lista
### 1. Escreva um programa que leia um número inteiro do teclado e diga se esse 
### número é positivo ou negativo

### Program for verify if an integer entry value is negative or positive ###



print('\n');
print("### Program for verify if an integer entry value is negative or positive ###")
print("### -------------------------------------------------------------------- ###")
print('\n');


# Ask for enter a value until it be an integer
while True :
    try :
        entryValue = int(input("Please, enter an integer number: "))
        if ( isinstance(entryValue, int)) :
            print("\n")
            break
    except ValueError :
        print("This value is not an integer!")
        print("\n")


# Verify and write if the number is 'positive' or 'negative'
if ( entryValue >= 0 ) :
    print("###RESULT###")
    print("The entry number", entryValue, "is positive.")
else :
    print("The entry number", entryValue, "is negative.")


print("\n")
print("##### :-) Thanks for your patience! See ya!!! ;-) ###")


# print("Magic happens here!")