import random
N= int(input("Kuinka monta pistettä haluat:"))

n=0
lasku= 0
while lasku <N:
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)

    if x*x + y*y <1:
        n=n+1
        lasku=lasku+1
arvo=4 * n/N
print("piin likiarvo: ", arvo)