# Agenda de tarefas interativa

tarefas = []            # Lista principal de tarefas, vazia (para ser preechida)
historico = []          # Pilha para desfazer tarefas
fila_execucao = []      # Fila para executar tarefas

def adicionar_tarefa(): # Função para adicionar tarefas
    descricao = input ("Digite a tarefa: ") # Tarefa digitada pelo usuário
    print()

    print ("Escolha a prioridade abaixo ↴ \n")
    print ("🟢 » Baixa")
    print ("🟡 » Média")
    print ("🔴 » Alta \n")
    prioridade = input (": ")

    print()
    print ("Digite a data abaixo ↴ \n")
    print ("⚠️   Siga o formato (dd/mm/aaaa). \n")
    data = input (": ")

    tarefa_completa = { # Meu dicionário para organizar......... (Chave e valor)
        'tarefa': descricao,
        'prioridade': prioridade,
        'data': data
    }

    print (f"Prioridade: {tarefa_completa['prioridade']} | Data: {tarefa_completa['data']}\n")

    tarefas.append(tarefa_completa)
    historico.append(tarefa_completa)
    fila_execucao.append(tarefa_completa)

    print (f"Tarefa '{tarefa_completa['tarefa']}' adicionada com sucesso! \n") # Resposta ao usuário

    salvar_tarefas_txt() # Só lembrando de salvar o arquivo depois de ter adicionado alguma tarefa

def cumprir_ultima_tarefa(): # Função para remover a última tarefa que foi adicionada na lista (Pilha - LIFO)
    if historico:
        ultima = historico.pop()
        tarefas.remove(ultima)
        fila_execucao.remove(ultima)

        print (f"Tarefa '{ultima['tarefa']}' removida com sucesso! \n") # Resposta ao usuário

        salvar_tarefas_txt() # Só lembrando de salvar o arquivo depois de ter desfeito alguma tarefa
    else:
        print ("Ops... Nenhuma tarefa para desfazer. \n") # Resposta ao usuário

def cumprir_primeira_tarefa(): # Função para remover a primeira tarefa que foi adicionada na lista (Fila - FIFO)
    if fila_execucao:
        feita = fila_execucao.pop(0)
        tarefas.remove(feita)

        print (f"Tarefa '{feita['tarefa']}' removida com sucesso! \n") # Resposta ao usuário

        salvar_tarefas_txt() # Só lembrando de salvar o arquivo depois de ter atendido alguma tarefa
    else:
        print ("Ops... Nenhuma tarefa para atender. \n")

def mostrar_tarefas(): # Função para mostrar as tarefas disponiveis
    print ()
    print ("📋  Lista de tarefas:")
    print ()

    for i, t in enumerate(tarefas):
        print (f"{i + 1}. {t['tarefa']} | Prioridade: {t['prioridade']} | Data: {t['data']}")

def salvar_tarefas_txt(): # Função para salvar as tarefas no arquivo .txt sempre que houver uma mudança na lista de tarefas
    # Abre o arquivo em modo de escrita, especificando o processo de execução e a codificação (aceitando caracteres especiais)
    arquivo = open ("tarefas.txt", "w", encoding = "utf-8")
    
    for t in tarefas:
        # Escreve a tarefa seguida de uma nova linha, assim listando e fazendo registro
        linha = (f"{t['tarefa']} | Prioridade: {t['prioridade']} | Data: {t['data']} \n")
        arquivo.write(linha)
    
    # Após escrever tudo que tinha, fecha o arquivo
    arquivo.close()

while True: # Laço de repetição que fica mostrando as opções do menu enquanto o usuário vai escolhendo
    
    # Menu de opções
    print()
    print ("🗓️   -  Agenda de tarefas interativa:")
    print()
    
    print ("------------------------------------")
    print ("- 1. Adicionar tarefa;             -")
    print ("- 2. Cumprir última tarefa;        -")
    print ("- 3. Cumprir primeira tarefa;      -")
    print ("- 4. Mostrar tarefas;              -")
    print ("- 5. Sair.                         -")
    print ("------------------------------------")

    print()
    opcao = input ("Escolha uma opção: ") # Entrada de dados feita pelo usuário
    print()
    
    match opcao:
        
        case '1':
            adicionar_tarefa()
        case '2':
            cumprir_ultima_tarefa()
        case '3':
            cumprir_primeira_tarefa()
        case '4':
            mostrar_tarefas()
        case '5':
            print ("Programa encerrado ✓ \n") # Resposta ao usuário
            break
        case _:
            print ("Opção escolhida inválida! \n") # Resposta ao usuário