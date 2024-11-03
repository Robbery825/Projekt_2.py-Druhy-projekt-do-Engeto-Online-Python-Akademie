"""
Projekt_2.py: Druhý projekt do Engeto Online Python Akademie
author: Robert Svorada
email: robert825@seznam.cz
Discrod: strejda.bob
"""
" Bulls and Cows"
import time
cara = "-" * 60 
def user():
        print("Hi there!")
        print(cara)
        print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
user()
print(cara)

def get_cislo():
    while True:
        cislo = input("Zadej své čtyřmístné číslo, každá číslice musí být unikátní: ")
        if not cislo.strip():
            print("Vstup nemůže být prázdný!")
        elif len(cislo) != 4:
            print("Číslo musí mít přesně 4 číslice!")
        elif not cislo.isdigit():
            print("Vstup musí být celé číslo!")
        elif len(set(cislo)) != 4:
            print("Každá číslice musí být unikátní!")
        elif "0" in cislo:
            print("Číslo nesmí obsahovat 0!")
        else:
            return cislo
sec_cislo = get_cislo()
print("Enter a number:", sec_cislo)
print(cara)       

def get_bulls_cows(tajne, hadej):
    bulls = sum(1 for i in range(4) if hadej[i] == tajne[i])
    cows = sum(1 for digit in set(hadej) if digit in tajne) - bulls
    return bulls, cows

def f_bulls_and_cows(bulls, cows):
    bulls_text = "Bull" if bulls == 1 else "Bulls"
    cows_text = "Cow" if cows == 1 else "Cows"
    
    return f"{bulls} {bulls_text}, {cows} {cows_text}"

pokusy = 0
start_time = time.time()
while True:
    hadej = input("Zadej svůj odhad: ")
    if len(hadej) != 4 or not hadej.isdigit() or len(set(hadej)) != 4 or "0" in hadej:
        print("Neplatný odhad. Ujisti se, že tvoje číslo obsahuje 4 unikátní číslice a neobsahuje 0!")
        continue
        
    pokusy += 1
    bulls, cows = get_bulls_cows(sec_cislo, hadej)
    print(f">>>\n{f_bulls_and_cows(bulls, cows)}") 

    if bulls == 4:
        end_time = time.time()
        celkovy_cas = end_time - start_time
        print(f"Correct, you've  guessed the right number in {pokusy} guesses.")
        print(f"Your total game time: {celkovy_cas:.2f} sekund.")
        break
print(cara)
print("That's amazing!")
