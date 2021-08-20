import random

val = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#@/!¡?¿-_&="
p = ""


def pass_Gen(val, p):
    long = int(input("Ingrese la longitud de su password: "))
    for i in range(long):
        p = p + random.choice(val) 
    print(p)

def generator():
    cant = int(input("¿Cuantas contraseñas quiere?: "))
    x = 1
    while x <= cant:
        pass_Gen(val, p)
        x = x+1
 

generator()