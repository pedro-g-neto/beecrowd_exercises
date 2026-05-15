#Lendo a operação
operacao = input()
#Criando a matriz e inicializando a lista dos elementos
matriz = [[float(input()) for _ in range(12)] for _ in range(12)]
elementos = []
#Percorrendo a matriz e adicionando os elementos abaixo da diagonal principal na lista
for l in range(12):
    for c in range(l):
        elementos.append(matriz[l][c])
#Desvios de fluxo
if operacao == 'S':
    resultado = sum(elementos)
elif operacao == 'M':
    resultado = sum(elementos)/len(elementos)

print(f'{resultado:.1f}')