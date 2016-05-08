### IAL002 - Primeira Lista
### 3. Escreva um programa que leia um número real e informe a categoria a que 
###	pertence o lutador de boxe, conforme a tabela (note que a tabela foi criada 
###	apenas para efeito deste exercício e não reflete as verdadeiras categorias do 
###	boxe):

### Program for verify an real entry value and define its category (boxer weight) ###

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
print("### Program for verify an real entry value and define its category (boxer weight) ###")
print("### ----------------------------------------------------------------------------- ###")
print('\n');


# Ask for enter a value until it be an real
while True :
    try :
        entryValue = float(input("Please, enter an real number: "))
        if ( isinstance(entryValue, float)) :
            print("\n")
            break
    except ValueError :
        print("This value is not an float!")
        print("\n")


# Verify and write if the number is 'positive' or 'negative'
print("###RESULT###")
if ( entryValue < 65 ) :
    print("The current boxer weight", entryValue, "is on 'Pena' category.")
else :
    print("The entry number", entryValue, "is negative")


print("\n")
print("##### :-) Thanks for your patience! See ya!!! ;-) ###")


# print("Magic happens here!")