from GerenciarDispositivos import menu_gerenciar
from GerenciarReservas import menu_reservas, mostrar_reservas
from MostrarReservas import reservas_matriz
from Database import horarios, reservas



def menu_principal():

    escolha = -1
    while escolha != 6:
        # Exibir opções
        print("1. Gerenciar Aparelhos")
        print("2. Mostrar Aparelhos reservados")
        print("3. Reservar Aparelhos")
        print("4. Devolver aparelhos")
        print("5. Ajuda")
        print("6. Sair")

        escolha = int(input("Digite a sua opcao: "))

        # Verificar se a opção está no intervalo válido
        if escolha < 1 or escolha > 6:
            print("\tVocê digitou um valor inválido!\n")
            continue

        # Executar ação com base na escolha
        if escolha == 1:
            menu_gerenciar()
        elif escolha == 2:
            reservas_matriz(horarios, reservas)
        elif escolha == 3:
            menu_reservas()
        elif escolha == 4:
            print("devolver_equipamento()")
        elif escolha == 5:
            print("ajuda()")
        else:
            print("Saindo...")




