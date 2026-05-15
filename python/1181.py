#Inicializando a matriz e a variável de resultado
matriz = []
resultado = 0
for l in range(12):
        matriz.append([None]*12)
#Lendo os parâmetros da operação
linha = int(input())
operacao = input()
#Preenchendo a matriz
for l in range(12):
    for c in range(12):
        matriz[l][c] = float(input())
#Desvios de fluxo para cada operação
if operacao == 'S': #Soma
    for c in range(12):
        resultado += matriz[linha][c]
    print(f'{resultado:.1f}')
elif operacao == 'M': #Média
    for c in range(12):
        resultado += matriz[linha][c]
    resultado = resultado/12
    print(f'{resultado:.1f}')