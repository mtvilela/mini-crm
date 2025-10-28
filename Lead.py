import json
from os.path import exists

class Lead:
    def __init__(self, nome, empresa, email="Vazio"):
        self.nome = nome
        self.empresa = empresa
        self.email = email


    def __str__(self):
        return f'Nome: {self.nome}\n Empresa: {self.empresa}\n Email: {self.email}\n'

    def to_dict(self):
        return{
            'nome': self.nome,
            'empresa': self.empresa,
            'email': self.email
        }


leads = []

def carregar_leads():
    if exists("leads.json"):
        with open("leads.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            for item in dados:
                leads.append(Lead(item["nome"], item["empresa"], item["email"]))


def salvar_leads():
    with open("leads.json", "w", encoding="utf-8") as arquivo:
        json.dump([lead.to_dict() for lead in leads], arquivo, ensure_ascii=False, indent=4)

def cadastro():
    nome = input('- Informações do LEADS -\n Nome: ')
    empresa = input("Empresa: ")
    email = input("Email (-se não tiver digite (0)-): ")
    if email == '0':
        email = None

    leads.append(Lead(nome, empresa, email))

    salvar_leads()

    print("Lead Cadastrado 👌")

def list_leads():
    if not leads:
        print("Nenhum lead cadastrado.")
        return

    print(f"{'ID':<3} | {'Nome':<20} | {'Empresa':<20} | {'Email':<30}")
    print("-" * 80)
    for i, l in enumerate(leads):
        print(f"{i:<3} | {l.nome:<20} | {l.empresa:<20} | {l.email:<30}")

def search_leads():
    if not leads:
        print("Nenhum lead cadastrado.")
        return

    termo = input("Buscar por nome, empresa ou email: ").strip().lower()

    resultados = []

    for lead in leads:
        if termo in lead.nome.lower() or termo in lead.empresa.lower() or (lead.email and termo in lead.email.lower()):
            resultados.append(lead)

    if resultados:
        print("\n✅ Resultados encontrados:\n")
        print(f"{'ID':<3} | {'Nome':<20} | {'Empresa':<20} | {'Email':<30}")
        print("-" * 80)

        for i, l in enumerate(resultados):
            print(f"{i:<3} | {l.nome:<20} | {l.empresa:<20} | {l.email:<30}")
    else:
        print("\n❌ Nenhum lead encontrado com esse termo.\n")
