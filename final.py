from Database import reservas, horarios, salas  
from GerenciarReservas import selecionar_aparelhos, listar_aparelhos_disponiveis, validar_quantidade, total_cadastrado


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

                # edita quantidades
            elif num_linha == "3":
                    # ! Mostrar e validar os códigos que por enquanto estao sendo adicionados no fodase
                 novo_total = validar_quantidade(total_cadastrado())
                 lista_disponivel = listar_aparelhos_disponiveis()
                 print(lista_disponivel)
                 codigo = selecionar_aparelhos(lista_disponivel, novo_total)
                 dados["Código"] = codigo

            # edita os códigos
            elif num_linha == "4":
                valor_atual = dados["Código"]
                print("Códigos atuais:")
                for index, codigo in enumerate(valor_atual, start=1):
                    print(f"{index}: {codigo}")
                escolha = input("Quer editar um código específico? (s/n): ").lower()
                if escolha == 's':
                    pos_str = input("Digite o número do código que quer editar: ")
                    if pos_str.isdigit():
                        pos = int(pos_str) - 1
                        if 0 <= pos < len(valor_atual):
                            # ! Mostrar e validar os códigos que por enquanto estao sendo adicionados no fodase
                            novo_codigo = input("Digite o novo código: ")
                            if novo_codigo.isdigit():
                                valor_atual[pos] = novo_codigo
                                print("Código atualizado com sucesso!")
                            else:
                                print("Código inválido!")
                        else:
                            print("Posição inválida.")
                    else:
                        print("Número inválido.")
                # elif escolha == "n":
                #     novo_valor = input("Digite a nova lista inteira (ex: 1,2,3): ")
                #     novo_valor = novo_valor.strip()
                #     if novo_valor == "":
                #         dados["Códigos"] = []
                #     else:
                #         itens = [x.strip() for x in novo_valor.split(",")]
                #         nova_lista = []
                #         for item in itens:
                #             if item.isdigit():
                #                 nova_lista.append(int(item))
                #             else:
                #                 nova_lista.append(item)
                #         dados["Códigos"] = nova_lista
                #     print("Lista atualizada com sucesso!")
                else:
                    print("Opção inválida!")




            # # edita quantidade e códigos
            # elif num_linha == "3" or num_linha == "4":
            #     while True:
            #         qtd_str = input("Digite a nova quantidade de aparelhos: ")
            #         if qtd_str.isdigit() and int(qtd_str) > 0:
            #             nova_qtd = int(qtd_str)
            #             novos_codigos = []
            #             for i in range(nova_qtd):
            #                 cod = input(f"Digite o código do aparelho #{i+1}: ")
            #                 novos_codigos.append(cod)
            #             dados["Código"] = novos_codigos
            #             print("Códigos atualizados com sucesso!")
            #             break
            #         else:
            #             print("Quantidade inválida. Digite um número maior que zero.")

        elif comando == "s":
            print("Alterações salvas com sucesso!")
            break

        else:
            print("Comando inválido!")


# Chama o editor
# while True:
#     resposta = input("\nDeseja editar alguma reserva? (s/n): ").lower()
#     if resposta == "s":
#         editor_reserva()
#     elif resposta == "n":
#         break
#     else:
#         print("Opção inválida! Por favor digite s para sim e n para não.")

# # Mostra reservas finais
# print("\n--- RESERVAS FINAIS ---")
# for reserva_id, dados in reservas.items():
#     print(f"\nID da reserva: {reserva_id}")
#     for chave, valor in dados.items():
#         print(f"{chave}: {valor}")
