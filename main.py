import random

def generator(min,max,step=1):
    number = random.randrange(min, max, step)
    return(number)

minimo = input("Enter the minimum number \n")
massimo = input("Enter the maximum number \n")

print(generator(int(minimo),int(massimo)))

