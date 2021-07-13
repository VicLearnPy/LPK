import colorama
import time 
import colorama
from colorama import Fore
import os

def close(): 
    input("""
[LKP]Appuyez sur une touche pour fermer le programme ...""")

def clear():
     os.system('cls')

def graph(): 
        colorama.init()
        print(Fore.BLUE +"""  
                         
     _______ _______ _______ 
    |\     /|\     /|\     /|
    | +---+ | +---+ | +---+ |
    | |   | | |   | | |   | |
    | |L  | | |K  | | |P  | |
    | +---+ | +---+ | +---+ |
    |/_____\|/_____\|/_____\|
                         
""")

graph()

F1 = input(str("[LKP] Le chemin du fichier : "))
Cr = input("[LKP] Le mot a chercher : ")
file = open(F1, 'r')
file.close()

def check():
            with open(F1,) as f:
                if Cr in f.read():
                    print("""
[LKP] Oui elle est dedans """)
#                 N = file.count(Cr)
#                    print(Fore.BLUE +""" 
#[LKP] Le mot apparait """ ,N ,Fore.BLUE +"Fois")
                else : 
                    print("""
[LKP] Non elle n'est pas dedans""")


def wait(): 
    clear()
    graph()
    print (str(Fore.BLUE +("[LKP] En train de rechercher ...")))
    time.sleep(5)

wait()
check()
close()
