def calculadora():
    print("-------------------------")
    print("\nBem Vindo a Calculadora!\n")
    print("-------------------------")

    print("Que tipo de calculo você deseja fazer?")
    print("(1)Adição (2)Subtração (3)Multiplicação (4)Divisão (5)Potenciação")

    opcao = int(input("Escolha uma opção: "))

    while opcao not in [1,2,3,4,5]:
        print("Essa Opção Não Existe!!")
        opcao = int(input("Escolha uma opção: "))


    print(f"Você escolheu a opção {opcao}")

    if opcao == 1:
        print("------")
        print("Adição")
        print("------")
    elif opcao == 2:
        print("---------")
        print("Subtração")
        print("---------")
    elif opcao == 3:
        print("-------------")
        print("Multiplicação")
        print("-------------")
    elif opcao == 4:
        print("------")
        print("Divisão")
        print("------")
    else:
        print("-----------")
        print("Potenciação")
        print("-----------")

    num1 = float(input("Digite primeiro número: "))
    num2 = float(input("Digite outro número: "))

    if opcao == 1:
        resultado = sum([num1, num2])
        print("Resultado:", resultado)
    elif opcao == 2:
        resultado = num1 - num2
        print("Resultado:", resultado)
    elif opcao == 3:
        resultado = num1 * num2
        print("Resultado:", resultado)
    elif opcao == 4:
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Não é possível dividir por zero!")
    elif opcao == 5:
            resultado = pow(num1, num2)
            print("Resultado:", resultado)
    else:
        print("Operação Inválida!")

calculadora()