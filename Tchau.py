import os
print ("Calcule o valor da conta telefonica")
t = float(input("Digite o tempo que foi utilizado pelo usuario: "))
if t < 200:
    v = t * 0.2
    print ("o valor da conta sera de R$ %6.2f " %v)
if t >= 200 and t <= 400:
    v = t * 0.18
    print ("o valor da conta sera de R$ %6.2f " %v)

if t > 400:
    v = t * 0.15
    print ("o valor da conta sera de R$ %6.2f " %v)

    
