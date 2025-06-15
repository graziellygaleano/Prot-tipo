import os
from Database import dispositivos, horarios, salas, reservas
from GerenciarDispositivos import total_cadastrado
from MostrarReservas import mostrar_reservas


#FUNÇÕES AUX PARA CONFUGURAR "RESERVAS"
contador_reservas = 1

def gerar_id_sequencial():
    global contador_reservas
    numero = contador_reservas
    contador_reservas += 1
    return numero

#Criar destino para usar aparelhos
def salvar_salas():
    i = 0
    print("\n==== Cadastro de Salas ====")
    qtd_salas = int(input("Quantas salas serão cadastradas: "))
    while i < qtd_salas:
        sala = input("Insira o número ou nome da sala (ex: 'Sala 1' ou 'Laboratório'): ")
        salas.append(sala)
        i += 1  

    print("Salas cadastradas com sucesso!")

    print("\t=====Salas cadastrados =====")
    for sala in salas:
        print(f"{sala}")


#Criar horario de funcionamento
def definir_horario():
    global horarios

    horaI = 0
    horaF = 0

    print("\n==== Horário de funcionamento ====")

    #Trata horas inválidas (26 - 35)
    while horaI <= 0 or horaI > 24:
        horaI = int(input("Insira o horário inicial de funcionamento (formato 24h, ex: 8, 13, 19): "))

    while horaF <= 0 or horaF > 24:
        horaF = int(input("Insira o horário final de funcionamento (formato 24h, ex: 8, 13, 19): "))

        while horaF <= horaI:
            horaF = int(input("O horário final deve ser maior que o inicial. Tente novamente: "))

    horarios = list(range(horaI, horaF + 1))
    print("Horários cadastrado com sucesso!")

    print("\t=====Horários cadastrados =====")
    for hora in horarios:
        print(f"{hora}h")




#Configurações
def config_reservas():
    
    #MENU
    while True: 
        print("\t==== Configurações ====")
        print("1. Cadastrar destinos para usar aparelhos")
        print("2. Cadastrar horários para usar aparelhos")
        print("3. Sair")
        menu = -1
        while menu not in [1,2,3]:
            menu = int(input("Digite a opção escolhida: "))
        
        if menu == 1:
            salvar_salas()
        elif menu == 2:
            definir_horario()
        elif menu == 3:
            break




#FUNÇÕES AUX PARA CRIAR RESERVAS

def editor_reserva():
    reserva_id = input("\nDigite o ID da reserva que deseja editar: ")
    while reserva_id not in reservas:
        print("Reserva não encontrada!")
        # print(reserva_id)
        # print(reservas)
        reserva_id = input("Digite o ID da reserva que deseja editar: ")

    dados = reservas[reserva_id]

    while True:
        print("\n--- Informações atuais da reserva ---")
        print(f"Hora: {dados['Hora']}")
        print(f"Destino: {dados['Destino']}")
        print(f"Quantidade: {len(dados['Código'])}")
        print(f"Códigos: {dados['Código']}")

        print("\nComandos:")
        print("e -> editar")
        print("s -> sair e salvar")

        comando = input("Digite o comando: ").lower()

        if comando == "e":
            while True:

                print("\n--- Escolha uma opção para alterar ---")
                print(f"1. Hora")
                print(f"2. Destino")
                print(f"3. Alterar todos aparelhos")
                print(f"4. Substituir um aparelho")

                num_linha = input("Digite a opção (1-4) que deseja editar: ")
                if num_linha in ["1", "2", "3", "4"]:
                    break
                else:
                    print("Número inválido! Por favor digite 1, 2, 3 ou 4")

            # edita horários
            if num_linha == "1":
                while True:
                    print(horarios)
                    hora = input("Digite o horário inicial e final (ex: 8 10): ")
                    partes = hora.strip().split()

                    if len(partes) != 2 or not all(p.isdigit() for p in partes):
                        print("Entrada inválida!")
                        continue

                    hora_inicio, hora_fim = map(int, partes)

                    if hora_inicio not in horarios or hora_fim not in horarios or hora_inicio >= hora_fim:
                        print("Horário inválido! Tente novamente.")
                        continue

                    dados["Hora"] = [hora_inicio, hora_fim]
                    print("Horário atualizado com sucesso!")
                    break

            # edita salas
            elif num_linha == "2":
                print("\n--- Opções de salas ---")
                for sala in salas:
                    print(sala)
                destino = input("Em qual sala será usado o aparelho? ").capitalize()
                while destino not in salas:
                    print("Local inválido!")
                    destino = input("Em qual sala será usado o aparelho? ").capitalize()
                dados["Destino"] = destino
                print("Destino atualizado com sucesso!")

                # edita quantidades
            elif num_linha == "3":
                 novo_total = validar_quantidade(total_cadastrado())
                 lista_disponivel = listar_aparelhos_disponiveis()
                 print(lista_disponivel)
                 codigo = selecionar_aparelhos(lista_disponivel, novo_total)
                 dados["Código"] = codigo

            # edita os códigos
            elif num_linha == "4":
                valor_atual = dados["Código"]
                print("Códigos atuais:")
                codes = []
                for codigo in dados["Código"]:
                    codes.append(codigo)
                    print(codigo)
                    print(codes)

                old_code = input("Digite o código que quer editar: ")
                index = dados["Código"].index(old_code)
                if old_code not in codes:
                    print("Insira um código válido!")
                    while old_code not in codes:
                        mudar_code = input("Digite o número do código que quer editar: ")
                else:
                    listar_aparelhos_disponiveis()
                    substituido = selecionar_aparelhos(listar_aparelhos_disponiveis(),1)
                    dados["Código"][index] = substituido[0]


            else:
                    print("Opção inválida!")

        elif comando == "s":
            print("Alterações salvas com sucesso!")
            break

        else:
            print("Comando inválido!")



#Add horário
def escolher_horario():
    print("\n=== Opções de horário ===")
    for i in horarios:
        print(f"{i}:00")

    hora_inicio = int(input("Digite o horário inicial da reserva (ex: 8): "))
    hora_fim = int(input("Digite o horário final da reserva (ex: 10): "))

    while not all(h in horarios for h in range(hora_inicio, hora_fim + 1)):
        print("Horário inválido ou fora do intervalo disponível. Tente novamente.")
        hora_inicio = int(input("Digite o horário inicial da reserva (ex: 8): "))
        hora_fim = int(input("Digite o horário final da reserva (ex: 10): "))

    return [hora_inicio, hora_fim]


#add sala
def escolher_sala():
    print("\n=== Opções de Salas ===")
    for s in salas:
        print(s)

    sala = input("Em qual sala será usado o aparelho? ")
    while sala not in salas:
        print("Sala inválida. Tente novamente.")
        sala = input("Em qual sala será usado o aparelho? ")

    return sala


#quantidade de aparelhos
def validar_quantidade(total_cadastrado):
    total_emprestar = int(input(f"\nQuantos aparelhos deseja emprestar? (máx: {total_cadastrado}): "))
    while total_emprestar > total_cadastrado or total_emprestar <= 0:
        print("Quantidade inválida.")
        total_emprestar = int(input(f"Digite um valor entre 1 e {total_cadastrado}: "))
    return total_emprestar


#listar aparelhos
def listar_aparelhos_disponiveis():
    disponiveis = []
    print("\n=== Aparelhos disponíveis ===")
    for marca, lista in dispositivos.items():
        for aparelho in lista:
            if aparelho["status"] == "disponível":
                print(f"Código: {aparelho['codigo']:<20}, Marca: {marca:<20}, Modelo: {aparelho['modelo']:<20}, Status: {aparelho['status']:<20}")
                disponiveis.append(aparelho["codigo"])
    return disponiveis


#selecionar aparelhos
def selecionar_aparelhos(disponiveis, total_emprestar):
    reservado = []
    print("\nSelecionar aparelhos:")
    for i in range(total_emprestar):
        emprestar = ""
        while emprestar not in disponiveis or emprestar in reservado:
            emprestar = input("Insira o código do aparelho que deseja: ")
            if emprestar not in disponiveis:
                print("Código inválido ou indisponível. Tente novamente.")
            elif emprestar in reservado:
                print("Este aparelho já foi selecionado. Escolha outro.")
        reservado.append(emprestar)
    return reservado



#CRIAR RESERVAS
def criar_reserva():
    global reservas
    ID = gerar_id_sequencial()
    hora = escolher_horario()
    sala = escolher_sala()
    total_emprestar = validar_quantidade(total_cadastrado())
    disponiveis = listar_aparelhos_disponiveis()
    reservado = selecionar_aparelhos(disponiveis, total_emprestar)

    reservas[ID] = {
        "Hora": hora,
        "Destino": sala,
        "Código": reservado
    }

    print("\nReserva criada com sucesso!")
    print(f"ID: {ID}")
    print(reservas[ID])




#MENU EDITAR RESERVA


#CANCELAR RESERVA
def cancelar_reserva():
    if not reservas:
        print("\n⚠️ Nenhuma reserva cadastrada.")
        return

    print("\n=== Reservas Cadastradas ===")
    for id_reserva, dados in reservas.items():
        print(f"\nID: {id_reserva}")
        print(f"  Horário: {dados['Hora'][0]}h às {dados['Hora'][1]}h")
        print(f"  Destino: {dados['Destino']}")
        print(f"  Aparelhos: {', '.join(dados['Código'])}")

    reserva_id = input("\nDigite o ID da reserva que deseja cancelar: ").strip()

    if reserva_id not in reservas:
        print("❌ Reserva não encontrada!")
        return

    confirm = input(f"Tem certeza que deseja cancelar a reserva '{reserva_id}'? (s/n): ").strip().lower()

    if confirm == 's':
        del reservas[reserva_id]
        print("✅ Reserva cancelada com sucesso!")
    else:
        print("❎ Cancelamento abortado.")


#MENU
def menu_reservas():

    escolha = -1
    while escolha != 5:
        # Exibir opções
        print("\tMENU PRINCIPAL")
        print("0. Configurar reservas")
        print("1. Criar Reserva")
        print("2. Mostrar Reservas")
        print("3. Editar Reservas")
        print("4. Cancelar Reservas")
        print("5. Sair")

        escolha = int(input("Digite a sua opcao: "))

        # Verificar se a opção está no intervalo válido
        if escolha < 0 or escolha > 5:
            print("\tVocê digitou um valor inválido!\n")
            continue

        # Executar ação com base na escolha
        if escolha == 0:
            config_reservas()
            input("Pressione um tecla para voltar ao menu")
            os.system('cls' if os.name == 'nt' else 'clear')
        if escolha == 1:
            criar_reserva()
            input("Pressione um tecla para voltar ao menu")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif escolha == 2:
            mostrar_reservas()
            input("Pressione um tecla para voltar ao menu")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif escolha == 3:
            editor_reserva()
            input("Pressione um tecla para voltar ao menu")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif escolha == 4:
            cancelar_reserva()
            input("Pressione um tecla para voltar ao menu")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Voltando para o meu principal...")






