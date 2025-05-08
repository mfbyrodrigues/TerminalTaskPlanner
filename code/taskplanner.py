# Agenda de tarefas interativa

tarefas = []            # Lista principal de tarefas, vazia (para ser preechida)
historico = []          # Pilha para desfazer tarefas
fila_execucao = []      # Fila para executar tarefas

"""
    tarefa → tarefa sem especificação.
    tarefa_ completa → tarefa especificada: tarefa, prioridade e data.
"""

def adicionar_tarefa(): # Função para adicionar tarefas
    # Lê a tarefa digitada pelo usuário
    descricao = input ("Digite a tarefa: ")
    print()

    # Exibe as opções e lê a prioridade escolhida pelo usuário
    print ("Escolha a prioridade abaixo ↴ \n")
    print ("🟢 » Baixa")
    print ("🟡 » Média")
    print ("🔴 » Alta \n")
    prioridade = input (": ")

    # Exibe a mensagem e lê a data digitada pelo usuário
    print()
    print ("Digite a data abaixo ↴ \n")
    print ("⚠️   Siga o formato (dd/mm/aaaa). \n")
    data = input (": ")
    print()

    tarefa_completa = { # Meu dicionário para organizar os dados da tarefa com suas respectivas chaves e valores
        'tarefa': descricao, # chave 'tarefa' armazena a descrição da tarefa
        'prioridade': prioridade, # chave 'prioridade' armazena a prioridade escolhida (🟢, 🟡, 🔴)
        'data': data # chave 'data' armazena a data informada pelo usuário (no formato dd/mm/aaaa)
    }

    # Adiciona a tarefa na lista principal, no histórico e na fila de execução
    tarefas.append(tarefa_completa)
    historico.append(tarefa_completa)
    fila_execucao.append(tarefa_completa)
    # Ou seja: "append" significa adicionar um item ao final de uma lista

    print (f"Tarefa '{tarefa_completa['tarefa']}' adicionada com sucesso!") # Resposta ao usuário
    print (f"Prioridade: {tarefa_completa['prioridade']} | Data: {tarefa_completa['data']}") # Resposta ao usuário

    salvar_tarefas_txt() # Só lembrando de salvar o arquivo depois de ter adicionado alguma tarefa

def cumprir_ultima_tarefa(): # Função para remover a última tarefa que foi adicionada na lista,no estilo pilha (LIFO)
    if historico:
        ultima = historico.pop()
        tarefas.remove(ultima)
        fila_execucao.remove(ultima)

        print (f"Tarefa '{ultima['tarefa']}' removida com sucesso! \n") # Resposta ao usuário

        salvar_tarefas_txt() # Só lembrando de salvar o arquivo depois de ter desfeito alguma tarefa
    else:
        print ("Ops... Nenhuma tarefa para desfazer. \n") # Resposta ao usuário

def cumprir_primeira_tarefa(): # Função para remover a primeira tarefa que foi adicionada na lista, no estilo fila (FIFO)
    if fila_execucao:
        feita = fila_execucao.pop(0)
        tarefas.remove(feita)

        print (f"Tarefa '{feita['tarefa']}' removida com sucesso! \n") # Resposta ao usuário

        salvar_tarefas_txt() # Só lembrando de salvar o arquivo depois de ter atendido alguma tarefa
    else:
        print ("Ops... Nenhuma tarefa para atender. \n") # Resposta ao usuário

def mostrar_tarefas(): # Função para mostrar as tarefas disponiveis
    print ()
    print ("📋  Lista de tarefas:")
    print ()

    for i, t in enumerate(tarefas):
        print (f"{i + 1}. {t['tarefa']} | Prioridade: {t['prioridade']} | Data: {t['data']}") # Resposta ao usuário

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
    print ("🗓️   Agenda de tarefas interativa ↴")
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