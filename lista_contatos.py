
import modulo_projeto
while True:
    print("\nAgenda de Contatos\n")
    print("1. Adicionar Contatos")
    print("2. Visualizar Agenda de Contatos")
    print("3. Favoritar Contato")
    print("4. Ver Favoritos")
    print("5. Apagar Contato")
    print("6. Fechar Agenda\n")

    escolha = input("O que você deseja fazer? ")
    
    from modulo_projeto import contatos

    if escolha == "1": 
        nome_contato = input("Digite o nome do contato que você deseja adicionar: ")
        telefone_contato = input("Agora digite o número do contato: ")
        email_contato = input("Por fim, adicione um email a este contato: ")
        modulo_projeto.adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)

    elif escolha == "2":
        modulo_projeto.ver_contatos(contatos)

    elif escolha == "3":
        modulo_projeto.ver_contatos(contatos)
        indice_contato = input("Qual contato você deseja favoritar? ")
        modulo_projeto.favoritar_contato(contatos, indice_contato, nome_contato)      

    elif escolha == "4":
        modulo_projeto.ver_favoritos(contatos)

    elif escolha == "5":
        indice_contato = input("Digite o número do contato que deseja apagar: ")
        modulo_projeto.apagar_contato(contatos, indice_contato)
        
    elif escolha == "6":
        modulo_projeto.fechar_agenda(contatos)

    