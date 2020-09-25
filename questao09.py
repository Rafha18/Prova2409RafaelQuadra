def questao09():

    print("======================================================")
    print("Exercicio 09, Prova do Dia 24/09/20 - Rafael Quadra")
    print("======================================================")

    print("+++++++++++ BEM-VINDO A CALCULADORA ++++++++++++++++++")
    print("")

    numeroinfo1 = int(input("Informe o Primeiro Número a ser Calculado: "))
    print("======================================================")
    print("Observe o Número Correspondente a Operação que Deseja Realizar: ")
    print("")
    print("1 = SOMA (+)")
    print("2 = SUBTRAÇÃO (-)")
    print("3 = MULTIPLICAÇÃO (*)")
    print("4 = DIVISÃO (/)")
    print("5 = RESTO DA DIVISÃO (%)")
    print("")

    operacao = int(input("Informe o Código(NUMERO) da Operação a ser Realizada:"))
    print("======================================================")

    numeroinfo2 = int(input("Informe o Segundo Número do Cálculo a ser Realizado: "))
    print("======================================================")

    if operacao == 1:
        print("A Operação Matemática Selecionada foi a: SOMA")
        print("")
        resultadosoma = numeroinfo1 + numeroinfo2
        print("O Cálculo Realizado foi: ")
        print(f"{numeroinfo1} + {numeroinfo2}")
        print(f"Resultado: {resultadosoma}")

    if operacao == 2:
        print("A Operação Matemática Selecionada foi a: SUBTRAÇÃO")
        print("")
        resultadosoma = numeroinfo1 - numeroinfo2
        print("O Cálculo Realizado foi: ")
        print(f"{numeroinfo1} - {numeroinfo2}")
        print(f"Resultado: {resultadosoma}")

    if operacao == 3:
        print("A Operação Matemática Selecionada foi a: MULTIPLICAÇÃO")
        print("")
        resultadosoma = numeroinfo1 * numeroinfo2
        print("O Cálculo Realizado foi: ")
        print(f"{numeroinfo1} x {numeroinfo2}")
        print(f"Resultado: {resultadosoma}")

    if operacao == 4:
        print("A Operação Matemática Selecionada foi a: DIVISÃO")
        print("")
        resultadosoma = numeroinfo1 / numeroinfo2
        print("O Cálculo Realizado foi: ")
        print(f"{numeroinfo1} / {numeroinfo2}")
        print(f"Resultado: {resultadosoma}")

    if operacao == 5:
        print("A Operação Matemática Selecionada foi a: RESTO DA DIVISÃO")
        print("")
        resultadosoma = numeroinfo1 % numeroinfo2
        print("O Cálculo Realizado foi: ")
        print(f"{numeroinfo1} % {numeroinfo2}")
        print(f"Resultado: {resultadosoma}")

if (__name__ == '__main__'):
    questao09()