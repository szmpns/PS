
import sys

def display(args , show_index):
    if show_index == True:    
        for i in range(len(args)):
            print(f"args[{i}] =", args[i])
    elif show_index == False:
        for i in range(len(args)):
            print(args[i])

argumenty = sys.argv

print("Start")

display(argumenty , True) # display nie jest już drukowana, ponieważ drukuje ona wyniki bezpośrednio wewnątrz siebie. (wcześniej None na końcu)

print("Stop")