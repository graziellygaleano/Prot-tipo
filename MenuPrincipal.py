import os
from GerenciarDispositivos import menu_gerenciar
from GerenciarReservas import menu_reservas, mostrar_reservas, cancelar_reserva
from MostrarReservas import reservas_matriz
from Database import horarios, reservas
from paletadecores import *  # Importa as cores
from Ajuda import manual


titulo_custom = f"""{FUNDO_PRETO}{AZUL_BRILHANTE}{NEGRITO}
::::::::::: ::::::::::: :::::::::      :::      ::::::::  :::    ::: 
    :+:         :+:     :+:    :+:   :+: :+:   :+:    :+: :+:   :+:  
    +:+         +:+     +:+    +:+  +:+   +:+  +:+        +:+  +:+   
    +#+         +#+     +#++:++#:  +#++:++#++: +#+        +#++:++    
    +#+         +#+     +#+    +#+ +#+     +#+ +#+        +#+  +#+   
    #+#         #+#     #+#    #+# #+#     #+# #+#    #+# #+#   #+#  
###########     ###     ###    ### ###     ###  ########  ###    ###  

             {BRANCO}+====== SISTEMA ITrack ======+{AZUL_BRILHANTE}
{RESET}"""


def menu_principal():
    escolha = -1
    while escolha != 6:
        print(f"{AZUL_ESCURO}{NEGRITO}=============== MENU PRINCIPAL ==============={RESET}")
        print(f"{AZUL_BRILHANTE}1.{RESET} {BRANCO}Mostrar Empréstimos{RESET}")
        print(f"{AZUL_BRILHANTE}2.{RESET} {BRANCO}Gerenciar Equipamentos{RESET}")
        print(f"{AZUL_BRILHANTE}3.{RESET} {BRANCO}Gerenciar Empréstimos{RESET}")
        print(f"{AZUL_BRILHANTE}4.{RESET} {BRANCO}Devolver aparelhos{RESET}")
        print(f"{AZUL_BRILHANTE}5.{RESET} {BRANCO}Ajuda{RESET}")
        print(f"{AZUL_BRILHANTE}6.{RESET} {BRANCO}Sair{RESET}")

        escolha = int(input(f"{CIANO}Digite a sua opção: {RESET}"))

        if escolha < 1 or escolha > 6:
            print(f"{VERMELHO}⚠ Por favor, digite um número válido!{RESET}")
            continue

        if escolha == 1:
            reservas_matriz(horarios, reservas)
            input("Pressione um tecla para voltar ao menu")
            os.system('cls' if os.name == 'nt' else 'clear')            
        elif escolha == 2:
            menu_gerenciar()
            input("Pressione um tecla para voltar ao menu")
            os.system('cls' if os.name == 'nt' else 'clear')            
        elif escolha == 3:
            menu_reservas()
            input("Pressione um tecla para voltar ao menu")
            os.system('cls' if os.name == 'nt' else 'clear')            
        elif escolha == 4:
            cancelar_reserva()
            input("Pressione um tecla para voltar ao menu")
            os.system('cls' if os.name == 'nt' else 'clear')            
        elif escolha == 5:
            manual()
            input("Pressione um tecla para voltar ao menu")
            os.system('cls' if os.name == 'nt' else 'clear') 
            print(f"{AZUL_BRILHANTE}Saindo...{RESET}")



