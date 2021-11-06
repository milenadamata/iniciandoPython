salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario + (salario*15/100)
print('Um funcionário que ganhava R${}, com aumento de 15%, passa a receber R${}'.format(salario, novo))
