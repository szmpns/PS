
with open("baza_danych.txt" , "r") as file:

    file = file.readlines()

    for i in range(len(file)):
        file[i] = file[i].rstrip()


    print(file)