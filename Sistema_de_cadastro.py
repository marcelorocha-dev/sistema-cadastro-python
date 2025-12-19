cadastros = []

def mostrar_menu():
    print("\n=== SISTEMA DE CADASTRO ===")
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Sair")

def cadastrar_pessoa():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    
    pessoa = {
        "nome": nome,
        "idade": idade
    }
    
    cadastros.append(pessoa)
    print("Cadastro realizado com sucesso!")

def listar_pessoas():
    if len(cadastros) == 0:
        print("Nenhum cadastro encontrado.")
    else:
        print("\n--- Pessoas cadastradas ---")
        for pessoa in cadastros:
            print(f"Nome: {pessoa['nome']} | Idade: {pessoa['idade']}")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_pessoa()
    elif opcao == "2":
        listar_pessoas()
    elif opcao == "3":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
