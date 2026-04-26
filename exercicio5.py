salario = 1

while salario != 0:
    salario = float(input("Digite o salário (0 para sair): "))

    if salario == 0:
        break

    if salario <= 5000:
        imposto = 0
    elif salario <= 7400:
        imposto = salario * 0.14
    else:
        imposto = salario * 0.27

    print("Imposto:", imposto)