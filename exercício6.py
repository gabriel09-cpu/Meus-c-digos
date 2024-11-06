nome = str(input("Digite seu nome: "))
sobrenome = str(input("Digite seu sobrenome: "))
age = int(input("Digite sua idade: "))

sal = float(input("Quanto você ganha por hora? "))
horas = int(input("Quantas horas você trabalha? "))

sal_total = sal * horas
print(f"Você ganha {sal_total} por mês!")