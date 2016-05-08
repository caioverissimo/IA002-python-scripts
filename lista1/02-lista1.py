### IAL002 - Primeira Lista
### 2. Escreva um programa que leia um número inteiro do teclado e diga se 
###	esse número é par ou ímpar

### Program for verify if an integer entry is an even or odd number ###



print('\n');
print("### Program for verify if an integer entry is an even or odd number ###")
print("### --------------------------------------------------------------- ###")
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


# Verify and write if the number is 'even' or 'odd'
if ( (entryValue % 2) == 0 ) :
    print("###RESULT###")
    print("The entry number", entryValue, "is even.")
else :
    print("The entry number", entryValue, "is odd.")


print("\n")
print("##### :-) Thanks for your patience! See ya!!! ;-) ###")


# print("Magic happens here!")