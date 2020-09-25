def questao05():

    print("======================================================")
    print("Exercicio 05, Prova do Dia 24/09/20 - Rafael Quadra")
    print("======================================================")

    print("Informe uma Palavra na Linha Abaixo:")
    palavra = input(">>>")

    novastring = palavra[::2]

    print("======================================================")
    print("A Sua Nova Palavra com os Caracteres Pares Deletados é:")

    print(f"{novastring}")
    print("======================================================")

if (__name__ == '__main__'):
    questao05()