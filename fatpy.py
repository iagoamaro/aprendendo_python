#!/bin/python
#calculador de fatorial
fat = int(input("Digite um numero: "))
fat_total = 1
for i in range(1,fat+1):
  #print(i)  
  fat_total = i * fat_total
print(i, fat_total)
