from __future__ import division
import random

def numbers(ari8moi):
    numbers = []
    for i in range(100):
        numbers.append(random.sample(ari8moi,5))
    return numbers
def coutnumbers(epilogi,ari8moi):
    e = [0]*80
    exit = True
    bingo = 0
    while exit:
            bingo = bingo+1
            w = random.sample(ari8moi,1)
            ari8moi.remove(w[0])
            for i in range(0,80):
                    if w[0] in epilogi[i]:
                            e[i] += 1
                            if e[i] == 5:
                                    exit=False
    return bingo
bingos = 0
for i in range(1000):
        ari8moi=range(1,81)
        people = numbers(ari8moi)
        bingos += coutnumbers(people,ari8moi)
print (bingos/1000)
