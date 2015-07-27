from random import randint
c = int(input("Você deverá adivinhar um número de 1 a:"))
a = randint(1,c)
x = 1
p = int(input("Chute um número:"))
while p != a:
    print("Alto" if p > a else "Baixo")
    p = int(input("Chute um número:"))
    x = x + 1
if x == 1:
    print(" Como assim?De primeira!")
if x > 1:
    print("Parabéns!Você acertou!")
    print("Número de tentativas:%i"%x)
