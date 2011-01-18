
threesum = 0
fivesum = 0
for natural in range(1000):
    if natural % 3 == 0:
        threesum += natural
    elif natural % 5 == 0:
        fivesum += natural

sumsum = threesum + fivesum
print sumsum 
