
contatos = []

def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"Nome: ": nome_contato, "Telefone: ": telefone_contato, "Email: ": email_contato, "Favorito": False}
    contatos.append(contato)
    print(f"{nome_contato} foi adicionado a sua Agenda de Contatos")
    return 

def ver_contatos(contatos):
    print("\nAgenda de Contatos")
    for indice, contato in enumerate (contatos, start=1):
        status = "⭐" if contato ["Favorito"] else " "
        nome_contato = contato["Nome: "]
        telefone_contato = contato["Telefone: "]
        email_contato = contato["Email: "]
        print(f"{indice}. [{status}] Nome: {nome_contato} | Telefone: {telefone_contato} | email: {email_contato} ")
    return
    
def favoritar_contato(contatos, indice_contato, nome_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["Favorito"] = True
    nome_contato = contatos[indice_contato_ajustado]["Nome: "]
    print(f"\n{nome_contato} foi favoritado em sua Agenda")
    return

def ver_favoritos(contatos):
    favoritos = [contato for contato in contatos if contato["Favorito"]]
    
    if not favoritos:
        print("Não há contatos favoritados.")
    else:
        for contato in favoritos:
            nome_contato = contato["Nome: "]
            telefone_contato = contato["Telefone: "]
            email_contato = contato["Email: "]
            print(f"Nome: {nome_contato} | Telefone: {telefone_contato} | Email: {email_contato}") 
    return

def apagar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos.pop(indice_contato_ajustado)
    print("\nContato apagado com sucesso!")
    return

def fechar_agenda(contatos):
    print("\nFechando Agenda de Contatos...")
    return exit(0)


    