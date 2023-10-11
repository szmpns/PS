
import sys 
import argparse

def stan_magazynu(produkty , stan_magazynu = {}):
    for i in range(0 , len(produkty) , 2):
        nazwa_towaru = produkty[i]
        ilosc_sztuk = int(produkty[i + 1])

        if nazwa_towaru in stan_magazynu:
            if stan_magazynu[nazwa_towaru] >= 0:
                stan_magazynu[nazwa_towaru] -= ilosc_sztuk
    return stan_magazynu

def wyswietl_stan_magazynu(stan_magazynu):
    print("-------------+------------")
    print("Nazwa towaru | Ilość sztuk")
    print("-------------+------------")
    for nazwa, ilosc in stan_magazynu.items():
        print(f"{nazwa} | {ilosc}")


stan_magazynu_dictionary = {
    "Komputer" : 10,
    "Laptop" : 20
}

arguments = sys.argv[1:]

def main():

    if len(arguments) == 0:
        print("ee")
    elif arguments[0] == "--stan_magazynu":
        wyswietl_stan_magazynu(stan_magazynu_dictionary)
    elif len(arguments) > 0:
        nowy_stan = stan_magazynu(arguments, stan_magazynu_dictionary)
        wyswietl_stan_magazynu(nowy_stan)

if __name__ == "__main__":
    main()