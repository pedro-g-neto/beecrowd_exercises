matriz = []
resultado = 0

for l in range(12): #Inicializando a matriz
        matriz.append([None]*12)

coluna = int(input())
operacao = input()

for l in range(12): #Preenchendo a matriz
    for c in range(12):
        matriz[l][c] = float(input())

if operacao == 'S': #Soma
    for l in range(12):
        resultado += matriz[l][coluna]
    print(f'{resultado:.1f}')
else: #Média
    for l in range(12):
        resultado += matriz[l][coluna]
    resultado = resultado/12
    print(f'{resultado:.1f}')