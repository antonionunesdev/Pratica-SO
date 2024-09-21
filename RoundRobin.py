fila = []
numeros_processos = []

quantidade_processos = int(input("Insira a quantidade de processos: "))

for i in range(quantidade_processos):
    tempo_execucao = int(input(f"Insira o tempo de execução do processo {i + 1}: "))
    fila.append(tempo_execucao)  # Adiciona o tempo de execução do processo na fila.
    numeros_processos.append(i + 1)  # Armazena o número do processo.

# Exibe os processos inseridos com seus tempos de execução.
print("Processos inseridos (tempo de execução):", fila, "\n")

# Solicita ao usuário a quantidade de tempo, que define quanto tempo de cada processo pode ser executado por vez.
quantum = int(input("Insira o quantum de tempo: "))
print("")

# Início do loop principal que simula o escalonamento de processos.
# Ele vai continuar até que a fila esteja vazia, ou seja, quando todos os processos forem concluídos.
while fila:
    # Remove o primeiro processo da fila para ser executado e também o número do processo correspondente.
    processo = fila.pop(0)
    numero_processo = numeros_processos.pop(0)

    # Verifica se o tempo de execução do processo é maior que o quantum.
    if processo > quantum:
        # Se for, o processo não é concluído, então o tempo restante é recolocado na fila, assim como o número do processo.
        fila.append(processo - quantum)
        numeros_processos.append(numero_processo)
        # Mostra quanto tempo de determinado processo foi executado e quanto tempo resta para ele ser concluído.
        print(f"{numero_processo}° processo executado por {quantum} unidades de tempo, restante: {processo - quantum}")
    else:
        # Se o tempo de execução do processo for menor ou igual ao quantum, o processo é finalizado.
        print(f"{numero_processo}° processo finalizado após {processo} unidades de tempo.")
        print("____________________________________________________________________________________")

# Quando a fila está vazia, todos os processos foram concluídos.
print("\nTodos os processos foram executados.")