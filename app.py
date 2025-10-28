from Lead import *


def printmenu():
    print("\nMini CRM Leads - Adicionar/Listar")
    print("[1] Adicionar lead")
    print("[2] Listar leads")
    print("[3] Buscar leads por (nome/empresa/email")
    print("[0] Sair")

def main():
    carregar_leads()
    while True:
        printmenu()
        op = input("Escolha: ")

        if op == "1":
            cadastro()
        elif op == "2":
            print("-- LISTA DE LEADS --\n")
            list_leads()
        elif op == "3":
            search_leads()
        elif op == "0":
            print("Até logo!")
            break
        else:
            print("Opção invalida")



if __name__ == "__main__":
    main()