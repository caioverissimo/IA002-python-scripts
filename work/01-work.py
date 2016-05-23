### IAL002 - Trabalhos
### 1. A partir de uma lista com 16 nomes de times de futebol, apresentar toda as rodadas 
### (ida e volta) na tela.

### Show 2 times the combinations among all 16 teams given by input ###



print('\n');
print("### Cadastro de rodadas de um campeonato entre 16 times de futebol [ida e volta] ###")
print("### ---------------------------------------------------------------------------- ###")
print('\n');


# Ask for enter a value until it be an integer
while True :
    try :
        entryValue = input("Por favor, entre com um nome de time de futebol: ")
        if ( isinstance(entryValue, six.string_types)) :
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