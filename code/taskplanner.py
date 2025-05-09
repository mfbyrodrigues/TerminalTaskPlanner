# Agenda de tarefas interativa

tarefas = []            # Lista principal de tarefas
historico = []          # Pilha para armazenar tarefas de forma que a última inserida seja a primeira a ser removida
fila_execucao = []      # Fila para armazenar tarefas que serão executadas na ordem em que foram inseridas

"""
    ANOTAÇÕES:

    tarefa → tarefa sem especificação.
    tarefa_completa → tarefa especificada: tarefa, prioridade e data.
    Imagens dos testes de cada estão na pasta "images"!

    print() → Linha em branco para organização visual.
    print ("\n")  → Duas linhas em branco para organização visual.

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

    # Resposta ao usuário
    print (f"Tarefa '{tarefa_completa['tarefa']}' adicionada com sucesso!") 
    print (f"Prioridade: {tarefa_completa['prioridade']} | Data: {tarefa_completa['data']}") 

    salvar_tarefas_txt() # Só lembrando de salvar o arquivo depois de ter adicionado alguma tarefa

def cumprir_ultima_tarefa(): # Função para remover a última tarefa que foi adicionada na lista no estilo pilha (LIFO)
    # Verifica se há alguma tarefa no histórico para desfazer
    if historico:
        ultima = historico.pop() # Remove a última tarefa do histórico
        tarefas.remove(ultima) # Remove a última tarefa da lista de tarefas
        fila_execucao.remove(ultima) # Remove a última tarefa da fila de execução

        print (f"Tarefa '{ultima['tarefa']}' removida com sucesso! \n") # Resposta ao usuário

        salvar_tarefas_txt() # Só lembrando de salvar o arquivo depois de ter "cumprido" alguma tarefa

    # Caso não haja nenhuma tarefa no histórico para desfazer
    else:
        print ("Ops... Nenhuma tarefa para desfazer. \n") # Resposta ao usuário

def cumprir_primeira_tarefa(): # Função para remover a primeira tarefa que foi adicionada na lista no estilo fila (FIFO)
    # Verifica se há alguma tarefa na fila de execução para atender
    if fila_execucao:
        feita = fila_execucao.pop(0) # Remove a primeira tarefa da fila de execução
        tarefas.remove(feita) # Remove a primeira tarefa da lista de tarefas

        print (f"Tarefa '{feita['tarefa']}' removida com sucesso! \n") # Resposta ao usuário

        salvar_tarefas_txt() # Só lembrando de salvar o arquivo depois de ter "cumprido" alguma tarefa
    
    # Caso não haja nenhuma tarefa na fila de execução para atender
    else:
        print ("Ops... Nenhuma tarefa para atender. \n") # Resposta ao usuário

def mostrar_tarefas(): # Função para mostrar as tarefas disponiveis
    print ()
    print ("📋  Lista de tarefas:")
    print ()

    # Laço de repetição que percorre a lista de tarefas e exibe cada tarefa com sua prioridade e data
    for i, t in enumerate(tarefas):
        print (f"{i + 1}. {t['tarefa']} | Prioridade: {t['prioridade']} | Data: {t['data']}") # Resposta ao usuário

def salvar_tarefas_txt(): # Função para salvar as tarefas no arquivo .txt sempre que houver uma mudança na lista de tarefas
    # Abre o arquivo em modo de escrita (nome do arquivo: "tarefas.txt"), especificando o processo de execução ("w") e a codificação, aceitando caracteres especiais ("utf-8")
    arquivo = open ("tarefas.txt", "w", encoding = "utf-8")
    
    for t in tarefas:
        linha = (f"{t['tarefa']} | Prioridade: {t['prioridade']} | Data: {t['data']} \n") # Cria uma linha de texto com os dados da tarefa separados por "|"
        arquivo.write(linha) # Escreve a linha da tarefa no arquivo
    
    # # Após escrever todas as tarefas, fecha o arquivo para salvar as alterações
    arquivo.close()

while True: # Laço de repetição que fica mostrando as opções do menu enquanto o usuário vai fazendo sua escolha
    
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

    # Verifica qual opção o usuário escolheu e executa a função correspondente
    match opcao: 
        
        case '1':
            adicionar_tarefa() # Chama a função para adicionar uma nova tarefa
        case '2':
            cumprir_ultima_tarefa() # Chama a função para cumprir (remover) a última tarefa
        case '3':
            cumprir_primeira_tarefa() # Chama a função para cumprir (remover) a primeira tarefa
        case '4':
            mostrar_tarefas() # Chama a função para mostrar todas as tarefas cadastradas
        case '5':
            print ("Programa encerrado ✓ \n") # Mensagem de encerramento para o usuário
            break # Encerra o laço de repetição e finaliza o programa
        case _:
            print ("Opção escolhida inválida! \n") # Mensagem de erro para opção inválida
