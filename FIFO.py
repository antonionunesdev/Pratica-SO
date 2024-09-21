fila = []

quantidade_processos = int(input("Insira a quantidade de processos: "))

for i in range(quantidade_processos):
    tempo_execucao = int(input(f"Insira o tempo de execução do processo {i + 1}: "))
    fila.append(tempo_execucao)

print("\n Processos inseridos (tempo de execução):", fila, "\n")

while fila:
    processo = fila.pop(0)
    print("Executando o processo com tempo de execução ", processo)
    print("Fila de processos atualizada:", fila, "\n")

print("Todos os processos foram executados.")