fila = []

quantidade_processos = int(input("Insira a quantidade de processos: "))

for i in range(quantidade_processos):
    prioridade = int(input(f"Insira a prioridade do processo {i + 1} (quanto menor o valor, maior a prioridade): "))
    fila.append(prioridade)

print("\nProcessos inseridos (prioridade):", fila)
fila.sort()
print("Processos ordenados (prioridade):", fila, "\n")

while fila:
    prioridade = fila.pop(0)
    print("Executando o processo com prioridade", prioridade, "...")
    print("Fila de processos por prioridade atualizada:", fila, "\n")

print("Todos os processos foram executados.")