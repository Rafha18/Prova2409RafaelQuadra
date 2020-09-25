import re
from django.forms import forms

def questao07():

    print("======================================================")
    print("Exercicio 07, Prova do Dia 24/09/20 - Rafael Quadra")
    print("======================================================")
    print("")
    senha = input("Informe a Senha a Ser Verificada: ")

    minimonumero = 1
    minimoespecial = 1

    if len(re.findall(r"[0-9]", senha)) < minimonumero:
        print(f"A Senha ({senha}) Tem Que Ter no Mínimo {minimonumero} Numero e {minimoespecial} Caractere Especial!")

    if len(re.findall(r"[~`!@#$%^&*()_+=-{};:'><]", senha)) < minimoespecial:
        print(f" A Senha ({senha}) Tem Que Ter no Mínimo {minimoespecial} Caractere Especial!")

    if len(re.findall(r"[0-9]", senha)) > minimonumero and len(re.findall(r"[~`!@#$%^&*()_+=-{};:'><]", senha)) > minimoespecial:
        print(f"A Senha Informada ({senha}) Foi Aprovada com Sucesso!")


if (__name__ == '__main__'):
    questao07()
