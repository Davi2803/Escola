import json

arquivo_cadastros="cadastros.json"

def salvar_cadastros (cadastros):
    with open (arquivo_cadastros, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, indent=4, ensure_asscii=False)    

def carregar_cadastros():
    try:
        with open (arquivo_cadastros,"r",encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except(FileNotFoundError,json.JSONDecodeError):
        return[]   

def exibir_menu():
    print("Bem vindo ao menu de cadastro!")
    print("1- Novo cadastro")
    print("2- Ver cadastro")
    print("3- Sair")
    print("------------------------------")
 

def cadastrar_pessoa(cadastros):
    nome = input("nome: ")
    idade = int(input("idade: "))
    turma = input("Turma: ")
    curso = input("curso: ")
    cadastros.append({"nome": nome, "idade": idade, "turma": turma, "curso": curso})
    print("Cadastro realizado com sucesso!")

def ver_cadastro(cadastros):
    if not cadastros:
        print("Nenhum cadastro no sistema")
    else:
        print("\n------LISTA DE CADASTROS------")
        for i, pessoa in enumerate(cadastros, 1):
            print(f"{i}. nome: {pessoa['nome']}, idade: {pessoa['idade']}, turma: {pessoa['turma']}, curso: {pessoa['curso']}")

def main():
    cadastros = []
    while True:
        exibir_menu()
        opção = input("Escolha uma opção: ")
        if opção == "1":
            cadastrar_pessoa(cadastros)
        elif opção == "2":
            ver_cadastro(cadastros)
        elif opção == "3":
            print("Obrigado por utilizar o sistema!")
            break
        else:
            print("Opção incorreta, tente novamente")

if __name__ == "__main__":
    main()