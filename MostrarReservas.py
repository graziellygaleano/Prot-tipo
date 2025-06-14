from Database import reservas

def mostrar_reservas():
    print("\n--- RESERVAS ---")
    for reserva_id, dados in reservas.items():
        print(f"\nID da reserva: {reserva_id}")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")