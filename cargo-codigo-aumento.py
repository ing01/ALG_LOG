# Algoritmo que recebe um código correspondente ao cargo de um funcionário e seu salário atual e mostra o 
# cargo, o valor do aumento e seu novo salário. De acordo com a tabela a seguir:
# 1: Escriturário =	50%;
# 2: Secretário	= 35%;
# 3: Caixa	= 20%;
# 4: Gerente = 10%;
# 5: Diretor = Não tem aumento.

salario = float(input('Digite o valor do salário: '))
cargo = int(input('Digite o código do cargo (1 à 5): '))
if cargo == 1:
    print('O cargo é Escrituário.')
    aumento = salario * 50/100
    print('O valor do aumento é de R$',aumento)
    novo_salario = salario + aumento
    print('O novo salário do Escrituário é de R$',novo_salario)
elif cargo == 2:
    print('O cargo é Secretário.')
    aumento = salario * 35/100
    print('O valor do aumento é de R$',aumento)
    novo_salario = salario + aumento
    print('O novo salário do Secretário é de R$',novo_salario)
elif cargo == 3:
    print('O cargo é Caixa.')
    aumento = salario * 20/100
    print('O valor do aumento é de R$',aumento)
    novo_salario = salario + aumento
    print('O novo salário do Caixa é de R$',novo_salario)
elif cargo == 4:
    print('O cargo é Gerente.')
    aumento = salario * 10/100
    print('O valor do aumento é de R$',aumento)
    novo_salario = salario + aumento
    print('O novo salário do Gerente é de R$',novo_salario)
elif cargo == 5:
    print('O cargo é diretor.')
    print('Este cargo não possui aumento no salário, portanto o salário é o mesmo.')
