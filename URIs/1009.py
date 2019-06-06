nome = input()
salario = float(input())
vendas = float(input())

comissao = .15
salario = round(salario+(vendas*comissao), 2)

print("TOTAL = R$ %.2f" % salario)
