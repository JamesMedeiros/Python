tempo = float(input("minutos utilizados: "))
if tempo < 200:
    tarifa = 0.20
else:
    if tempo <= 400:
        tarifa = 0.18
    else:
        if tempo <= 800:
            tarifa = 0.15
        else:
            tarifa = 0.08
print("o valor da conta sera R$%6.2f" %(tarifa * tempo))
