import random
import string

alp = string.printable

def pass_gen(alp):
    pass_w = ""
    long = int(input("Ingrese la longitud de su password: "))
    for _ in range(long):
        pass_w = pass_w + random.choice(alp)
    print(pass_w)

#------------main funtion---------------#

def main():
    pass_gen(alp)

