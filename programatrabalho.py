# BIBLIOTECA PARA LIMPAR A TELA
import os

# MENU PRINCIPAL - INVOCADO NA ULTIMA LINHA PELO CÓDIGO -> menu()


def menu():

    print("### Calcular a quantidade necessária de metros de fio - 1")
    print("### Calcular a quantidade necessária de tinta - 2")
    print("### Sair - 3")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        menuSecundarioFio()
    elif opcao == 2:
        menuSecundarioTinta()
    elif opcao == 3:
        sair()
    else:
        menu()


def menuSecundarioFio():
    print(" ### Único - 1")
    print(" ### Orçamento - 2")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        # RECEBER OS VALORES DO USUÁRIO
        metroQuadrado = float(input("Digite o metro quadrado do imóvel: "))
        preco = float(input("Digite o preço do metro do fio: "))

        # FAZER OS CALCULOS
        calculoFio = 3 * metroQuadrado
        calculoValorFio = preco * calculoFio

        # IMPRIMIR A RESPOSTA NA TELA
        print("""Você vai precisar de {} metros de fio \n
                Vai gastar {} reais
                """.format(calculoFio, calculoValorFio))

        # PERGUNTAR SE QUER CONTINUAR OU SAIR DO PROGRAMA
        continuar = input("Deseja voltar ao menu? (s/n) ")
        if continuar == 's':
            menu()
        elif continuar == 'n':
            os.close
        else:
            menuSecundarioFio()

    elif opcao == 2:
        # RECEBER OS VALORES DO USUÁRIO
        metroQuadrado = float(input("Digite o metro quadrado do imóvel: "))
        preco1 = float(input("Digite o preço do metro do fio na loja 1: "))
        preco2 = float(input("Digite o preço do metro do fio na loja 2: "))

        # FAZER OS CALCULOS
        calculoFio = 3 * metroQuadrado
        calculoPreco1 = preco1 * calculoFio
        calculoPreco2 = preco2 * calculoFio

        # IMPRIMIR A RESPOSTA NA TELA
        if calculoPreco1 > calculoPreco2:
            print("A loja 2 é mais barata")
        else:
            print("A loja 1 é mais barata")

        # PERGUNTAR SE QUER CONTINUAR OU SAIR DO PROGRAMA
        continuar = input("Deseja voltar ao menu? (s/n) ")
        if continuar == 's':
            menu()
        elif continuar == 'n':
            os.close

    else:
        # EM CASO DE ERRO, RETORNAR PARA O MENU SECUNDARIO
        menuSecundarioFio()


def menuSecundarioTinta():
    print(" ### Único - 1")
    print(" ### Orçamento - 2")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        # RECEBER OS VALORES DO USUÁRIO
        metroQuadrado = float(input("Digite o metro quadrado do imóvel: "))
        preco = float(input("Digite o preço do litro da tinta: "))

        # FAZER OS CALCULOS
        calculoLitroTinta = metroQuadrado / 2
        calculoValorTinta = preco * calculoLitroTinta

        # IMPRIMIR A RESPOSTA NA TELA
        print("""Você vai precisar de {} litros de tinta \n
          Vai gastar {} reais
          """.format(calculoLitroTinta, calculoValorTinta))

        # PERGUNTAR SE QUER CONTINUAR OU SAIR DO PROGRAMA
        continuar = input("Deseja voltar ao menu? (s/n) ")
        if continuar == 's':
            menu()
        elif continuar == 'n':
            os.close

    elif opcao == 2:
        # RECEBER OS VALORES DO USUÁRIO
        metroQuadrado = float(input("Digite o metro quadrado do imóvel: "))
        preco1 = float(input("Digite o preço do metro da tinta na loja um: "))
        preco2 = float(
            input("Digite o preço do litro da tinta na loja dois: "))

        # FAZER OS CALCULOS
        calculoLitroTinta = metroQuadrado / 2
        calculoValorTinta1 = preco1 * calculoLitroTinta
        calculoValorTinta2 = preco2 * calculoLitroTinta

        # IMPRIMIR A RESPOSTA NA TELA
        if calculoValorTinta1 > calculoValorTinta2:
            print("A loja 2 é mais barata")
        else:
            print("A loja 1 é mais barata")

        # PERGUNTAR SE QUER CONTINUAR OU SAIR DO PROGRAMA
        continuar = input("Deseja voltar ao menu? (s/n) ")
        if continuar == 's':
            menu()
        elif continuar == 'n':
            os.close

    else:
        # EM CASO DE ERRO, RETORNAR PARA O MENU SECUNDARIO
        menuSecundarioTinta()


def sair():
    os.close


# INVOCAÇÃO DA FUNÇÃO
menu()
