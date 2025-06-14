from Database import reservas, horarios

def mostrar_reservas():
    print("\n--- RESERVAS ---")
    for reserva_id, dados in reservas.items():
        print(f"\nID da reserva: {reserva_id}")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

def reservas_matriz(horarios, reservas):

    #cabeçalho
    margem = " " * 6
    largura = len(horarios) * 7

    print()
    print(f"{margem}+{'=' * largura}+")
    print(f"{margem}|{'TABELA DE RESERVAS POR HORÁRIO'.center(largura)}|")
    print(f"{margem}+{'=' * largura}+")
    
    print(margem + "".join(f"{h:>6} " for h in horarios))
    print(f"{margem}+{'-' * largura}+")


    reservantes_por_hora = {
        h: [k for k, v in reservas.items() if h in v.get("Hora", [])]
        for h in horarios
    }

    if all(len(reservantes) == 0 for reservantes in reservantes_por_hora.values()):
        print("Nenhuma reserva encontrada.")
        return

    max_linhas = max(len(reservantes) for reservantes in reservantes_por_hora.values())

    for linha in range(max_linhas):
        print("      ", end="")
        for h in horarios:
            reservantes = reservantes_por_hora[h]
            if linha < len(reservantes):
                print(f"{reservantes[linha]:>6}", end=" ")
            else:
                print("    ", end=" ")
        print()
