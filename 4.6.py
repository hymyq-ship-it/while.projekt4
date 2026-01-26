import random

n=0
N=100000000
i=0
while i <N:
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)

    if x** 2 + y**2 <1:
        n=n+1
    #seurava kierros
    i=i+1
#lasketaan piin likiarvo annetun kaavan avulla.
arvo=(4 * n/N)
print("piin likiarvo: ", arvo)
