# 🧪 Atividade prática 

## 📚 Matéria: Introdução à Estrutura de Dados com Python

### 🎯 Objetivo

Compreender e aplicar os conceitos de **lista**, **pilha** e **fila** por meio do desenvolvimento de uma **agenda de tarefas interativa** utilizando a linguagem **Python**.

---

### 🛠️ Descrição da atividade

Desenvolvimento de um programa de terminal que permite ao usuário:

- Adicionar tarefas a uma lista principal.
- Desfazer a última tarefa adicionada (simulando uma pilha).
- Atender tarefas na ordem em que foram inseridas (simulando uma fila).
- Visualizar todas as tarefas registradas.

---

### 🧩 Estruturas utilizadas

- `Listas`: para armazenar todas as tarefas.
- `Pilha (LIFO)`: para desfazer a última tarefa adicionada.
- `Fila (FIFO)`: para atender as tarefas na ordem de entrada.

---

### 💻 Código base

```python
tarefas = []            # Lista principal de tarefas
historico = []          # Pilha para desfazer tarefas
fila_execucao = []      # Fila para executar tarefas

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    historico.append(tarefa)
    fila_execucao.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada!\n")

def desfazer_ultima_tarefa():
    if historico:
        ultima = historico.pop()
        tarefas.remove(ultima)
        fila_execucao.remove(ultima)
        print(f"Tarefa '{ultima}' desfeita!\n")
    else:
        print("Nenhuma tarefa para desfazer.\n")

def atender_tarefa():
    if fila_execucao:
        feita = fila_execucao.pop(0)
        tarefas.remove(feita)
        print(f"Tarefa '{feita}' atendida!\n")
    else:
        print("Nenhuma tarefa para atender.\n")

def mostrar_tarefas():
    print("\n📋 Lista de Tarefas:")
    for i, t in enumerate(tarefas):
        print(f"{i + 1}. {t}")
    print()

while True:
    print("1. Adicionar Tarefa")
    print("2. Desfazer Última Tarefa")
    print("3. Atender Tarefa (modo fila)")
    print("4. Mostrar Tarefas")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        tarefa = input("Digite a tarefa: ")
        adicionar_tarefa(tarefa)
    elif opcao == '2':
        desfazer_ultima_tarefa()
    elif opcao == '3':
        atender_tarefa()
    elif opcao == '4':
        mostrar_tarefas()
    elif opcao == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida!\n")
```

---

### 📝 O que você deve fazer

1. Copie e execute o código acima em seu ambiente Python.
2. Teste todas as funcionalidades com diferentes tarefas.
3. Personalize o sistema:
    - ➕ Adicione prioridade ou data à tarefa.
    - 💾 Faça com que o programa salve as tarefas em um arquivo `.txt`.

---

### ✅ Critérios de avaliação

| Critério | Pontos |
| --- | --- |
| Código funcional | 4 pts |
| Uso correto de lista, pilha e fila | 2 pts |
| Personalização extra (ex: salvar, data, prioridade) | 2 pts |
| Organização e clareza do código | 2 pts |

---

### 📅 Entrega

📌 **Data limite**: *09 de maio.*

📩 **Forma de entrega**: envie o código e a explicação em PDF ou pelo repositório do GitHub.
