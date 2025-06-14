from Database import dispositivos

#FUNÇÕES
"""   
    -- "Adicionar aparelho": chamar a função adicionarAparelho() 
    -- "Mostrar aparelhos": chamar a função mostrarAparelho()
    -- "Editar aparelho": chamar a função editarAparelho()
    -- "Excluir aparelhos": chamar a função excluirAparelho()
    -- "Voltar ao menu anterior": imprime a mensagem "Voltando...
"""

#CADASTRAR EQUIPAMENTOS
def cadastro_dispositivos():
    print("         +====Bem vindo ao Sistema IF de Notebooks====+ \n    Primeiramente você irá inserir os dados, ou seja, marca, modelo e quantidade.")
    while True:
        marca = input("Marca: ").strip().upper()
        modelo = input("Modelo: ").strip()
        quantidade = int(input("Quantidade: "))        
        dispositivos.setdefault(marca, [])
        num_inicial = len(dispositivos[marca]) + 1

        for i in range(quantidade): 
            serial = str(num_inicial + i).zfill(8)
            codigo = f"{marca}{serial}"
            dispositivos[marca].append({
                "codigo": codigo,
                "modelo": modelo,
                "status": "disponível"
            })
            print(f"Dispositivo cadastrado: {codigo}")

        continuar = input("\nQuer cadastrar outra marca? (s para sim / n para não): ").lower().strip()
        if continuar != "s": 
            break

def total_cadastrado():
    total = sum(len(lista) for lista in dispositivos.values())
    return total

def editar_dispositivos():
    "Editar Marca ou modelo do dispositivo"
    pass

def excluir_dispositivos():
    "Apagar equipamento cadastrado"
    pass

#MOSTRAR APARELHOS
def mostrar_aparelhos():
    if not dispositivos:
        print("Você precisa adicionar aparelhos primeiro")
    else:
        for marca, lista in dispositivos.items():
            print(f"\nMarca {marca}: ")
        for d in lista: 
            print(f"  {d['codigo']} | {d['modelo']} | {d['status']}")

#MENU GERENCIAR
def menu_gerenciar():
    escolha = -1
    while escolha != 5:
        print("1. Adicionar aparelhos")
        print("2. Mostrar aparelhos ")
        print("3. Editar Aparelhos")
        print("4. Excluir aparelhos")
        print("5. Sair")

        escolha = int(input("Digite a sua opcao: "))

        if escolha < 1 or escolha > 5:
            print("\tVocê digitou um valor inválido!\n")
            continue

        if escolha == 1:
            cadastro_dispositivos()
        elif escolha == 2:
            mostrar_aparelhos()
        elif escolha == 3:
            print("editar_aparelho()")  
        elif escolha == 4:
            print("excluir_aparelho()")
        else:
            print("Voltando para o menu principal")


