
import sys

def display(args , show_index):
    if show_index == True:    
        for i in range(len(args)):
            print(f"args[{i}] =", args[i])
    elif show_index == False:
        for i in range(len(args)):
            print(args[i])

def run(moves , move_descriptions):

    lista_ruchow = []

    for ruch in moves:
        if  ruch in move_descriptions:
            opis = move_descriptions[ruch]
            lista_ruchow.append(opis)

    return lista_ruchow 

argumenty = sys.argv

move_descriptions_dictionary = {
    'f': 'Zwierzak idzie do przodu',
    'b': 'Zwierzak idzie do tyłu',
    'l': 'Zwierzak skręca w lewo',
    'r': 'Zwierzak skręca w prawo',
    }

print("Start")

# print(run(argumenty , move_descriptions_dictionary))

display(run(argumenty , move_descriptions_dictionary) , False)

# display(argumenty , True) # display nie jest już printowana, ponieważ drukuje ona wyniki bezpośrednio wewnątrz siebie. (wcześniej None na końcu)

print("Stop")