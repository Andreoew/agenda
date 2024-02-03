def dados_contato():
  nome = input("\n\033[1;33mDigite o nome:\033[0m ")
  telefone = input("\n\033[1;33mDigite o telefone:\033[0m ")
  email = input("\n\033[1;33mDigite o e-mail:\033[0m ")
  return nome, telefone, email

def salvar_novo_contato(contatos): 
  novo_contato = dados_contato()
  contato = {"Novo contato": novo_contato, "favorito": False}
  contatos.append(contato)
  print("\n✅ Adicionando novo contato...")
  nome, telefone, email = novo_contato
  print(f"\n\033[1;33mNovo contato:\033[0m\nNome: \033[1;32m{nome}\033[0m,\nTelefone: \033[1;32m{telefone}\033[0m\nE-mail: \033[1;32m{email}\033[0m \n\n✅ Salvo com sucesso!")
  return 

def visualizar_contatos(contatos):
  print("\nLista de contatos")
  if len(contatos) == 0:
    print("\033[1;31mNenhum contato encontrado.\033[0m")
  for indice, contato in enumerate(contatos, start=1):
    favorito = "❤️ " if contato["favorito"] else "  "
    nome, telefone, email = contato["Novo contato"]
    print(f"{indice}. [{favorito}] \033[1;32mNome: {nome}, Telefone: {telefone}, Email: {email}\033[0m")
  return

def editar_contato(contatos, indice_contado, dados_atualizados):
  print("Editando contato")
  indice_contado_ajustado = int(indice_contado) - 1
  if indice_contado_ajustado >= 0 and indice_contado_ajustado < len(contatos):
    contatos[indice_contado_ajustado]["Novo contato"] = dados_atualizados
    print("\n✅ sucesso! ✅")
    nome, telefone, email = dados_atualizados
    print(f"\n\033[1;33mNovo contato:\033[0m\nNome: \033[1;32m{nome}\033[0m,\nTelefone: \033[1;32m{telefone}\033[0m\nE-mail: \033[1;32m{email}\033[0m \n\n✅ Salvo com sucesso!")
  else:
    print("\n ❌ Erro. ❌")
    print("\033[1;31mErro: Índice de contato inválido.\033[0m")

def contato_favorito(contatos, indice_contado):
  indice_contato_ajustado = int(indice_contado) - 1
  if contatos[indice_contato_ajustado]["favorito"]:
    contatos[indice_contato_ajustado]["favorito"] = False
    print(f"Contato {indice_contado} removido da lista de favoritos")
    return
  else: 
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"Contato {indice_contado} marcado como favorito")
    return

def visualizar_contatos_favoritos(contatos):
  print("Lista de contatos favoritos ❤️")
  contatos_favoritos = [contato for contato in contatos if contato["favorito"]]

  if len(contatos_favoritos) == 0:
    print("\033[1;31mNenhum contato marcado como favorito.\033[0m")
  else:
    for indice, contato in enumerate(contatos, start=1):    
      if contato["favorito"]:
        favorito = "❤️ "  
        nome, telefone, email = contato["Novo contato"]
        print(f"{indice}. [{favorito}] \033[1;32mNome: {nome}, Telefone: {telefone}, Email: {email}\033[0m")
    return

def deletar_contato(contatos, indice_contado):
  indice_contado_ajustado = int(indice_contado) - 1
  if 0 <= indice_contado_ajustado < len(contatos):
    contatos.pop(indice_contado_ajustado)
    print("Contato deletado com sucesso!")
  else:
    print("\n ❌ Erro. ❌")
    print("\033[1;31mErro: Índice de contato inválido.\033[0m")


contatos = []
while True:
  print("\n\033[1;32mMenu da Agenda:\033[0m")
  print("1. Novo contato")
  print("2. Visualizar contatos")
  print("3. Atualizar contato")
  print("4. Marcar/desmarcar contato favorito")
  print("5. Visualizar favoritos")
  print("6. Apagar contato")
  print("7. Encerrar agenda")

  opcao = input("\n\033[1;33mDigite uma opção:\033[0m ")

  if opcao == "1":
    salvar_novo_contato(contatos)
  elif opcao == "2":
    visualizar_contatos(contatos)
  elif opcao == "3":
    visualizar_contatos(contatos)
    indice_contado = input("\n\033[1;33mDigite o número do contato que deseja editar:\033[0m ")
    dados_atualizados = dados_contato()
    editar_contato(contatos, indice_contado, dados_atualizados)
  elif opcao == "4":
    visualizar_contatos(contatos)
    indice_contado = input("\n\033[1;33mDigite o número do contato que deseja marcar/desmarcar favorito:\033[0m ") 
    contato_favorito(contatos, indice_contado)
  elif opcao == "5":
    visualizar_contatos_favoritos(contatos)
  elif opcao == "6":    
    if 0 >= len(contatos):
      print("\033[1;31mNenhum contato encontrado.\033[0m")
    else:
      visualizar_contatos(contatos)
      indice_contado = input("\n\033[1;33mDigite o número do contato que deseja deletar:\033[0m ")
      deletar_contato(contatos, indice_contado)
  elif opcao == "7":
    break
print("Agenda encerrada")