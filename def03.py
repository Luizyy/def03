hora_valor = float(input("Quanto você ganha por hora trabalhada? "))
hora_trabalhada = int(input("E quantas horas você trabalhou esse mês? "))

def salario():
    hora_trabalhada_2 = float(hora_trabalhada)
    salario_total = hora_valor * hora_trabalhada_2
    print(f"Seu salário é {salario_total}")

salario()