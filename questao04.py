def questao04():

    print("======================================================")
    print("Exercicio 04, Prova do Dia 24/09/20 - Rafael Quadra")
    print("======================================================")

    print("")
    print("Informe uma lista de 10 elementos(numericos ou textuais): ")

    for i in range(10):
        texto = input(f">>>:\n")
        arquivo = open('arquivoquestao04.txt', 'a')
        arquivo.write(texto + "\n")
        print("Elemento Inserido!")
        print("")
        arquivo.close()

    arquivo = open('arquivoquestao04.txt', 'r')
    for linha in arquivo:
        linha = linha.rstrip()
        print(linha)
    arquivo.close()


if (__name__ == '__main__'):
    questao04()