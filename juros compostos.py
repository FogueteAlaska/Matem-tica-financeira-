print("bem vindo a calculadora de juros\n compostos ")

c = int(input("digite o capital: "))
i = int(input("digite a taxa de juros: "))
t = int(input("digite o tempo aplicado: "))

i = i/100
j = c*(1+i)**t

print("o juros é de: ",j,"$")
print("o montante é de: ",c+j,"$")
