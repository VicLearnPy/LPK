import colorama
import time 
import colorama
from colorama import Fore
import os

def close(): 
    input(Fore.WHITE + """
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

F1 = input(str("[LKP] The path of the file : "))
Cr = input("[LKP] The word to find : ")
file = open(F1, 'r')
file.close()

def check():
            with open(F1,) as f:
                if Cr in f.read():
                    print(Fore.GREEN +"""
[LKP] Yes there is  """)
#                 N = file.count(Cr)
#                    print(Fore.BLUE +""" 
#[LKP] Le mot apparait """ ,N ,Fore.BLUE +"Fois")
                else : 
                    print(Fore.RED + """
[LKP] No is not here""")


def wait(): 
    clear()
    graph()
    print (str(Fore.LIGHTBLUE_EX +("[LKP] Finding ...")))
    time.sleep(5)

wait()
check()
close()
