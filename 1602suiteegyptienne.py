import time
import math


x = int(input("Entrez un entier a : "))
y = int(input("Entrez un entier b : "))
s = 0

while(x != 0):
	if(x % 2 == 1):
		s = s+y
	x = x/2
	y = y*2

print(s)