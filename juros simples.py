print("bem vindo a calculadora de juros\n simples")

c = int(input("digite o capital: "))
i = int(input("digite a taxa de juros: "))
t = int(input("digite o tempo: "))
i = i/100
j = (c*i*t)

print("o montante é ", j, "$")
