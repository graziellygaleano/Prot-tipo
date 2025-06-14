from Database import reservas, horarios

def editor_reserva(reservas):
    reserva_id = input("\nDigite o ID da reserva que deseja editar: ")
    while reserva_id not in reservas:
        print("Reserva não encontrada!")
        print(reserva_id)
        print(reservas)
        reserva_id = input("Digite o ID da reserva que deseja editar: ")

    dados = reservas[reserva_id]

    while True:
        print("\n--- Informações atuais da reserva ---")
        print(f"1: Hora: {dados['Hora']}")
        print(f"2: Destino: {dados['Destino']}")
        print(f"3: Quantidade: {len(dados['Código'])}")
        print(f"4: Códigos: {dados['Código']}")

        print("\nComandos:")
        print("e -> editar")
        print("s -> sair e salvar")

        comando = input("Digite o comando: ").lower()

        if comando == "e":
            while True:
                num_linha = input("Digite o número da linha (1-4) que deseja editar: ")
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

            # edita quantidade e códigos
            elif num_linha == "3":
                while True:
                    qtd_str = input("Digite a nova quantidade: ")
                    if qtd_str.isdigit() and int(qtd_str) > 0:
                        qtd
