from compromisso import cadastrar_compromisso
from contatos import cadastrar_contato

def menu():
    print("1. Cadastrar Compromisso")
    print("2. Cadastrar Contato")
    print("3. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            data = input("Digite a data do compromisso (DD/MM/AAAA): ")
            hora = input("Digite a hora do compromisso (HH:MM): ")
            descricao = input("Digite a descrição do compromisso: ")
            cadastrar_compromisso(data, hora, descricao)
        elif opcao == "2":
            nome = input("Digite o nome do contato: ")
            idade = input("Digite a idade do contato: ")
            email = input("Digite o email do contato: ")
            cadastrar_contato(nome, idade, email)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
