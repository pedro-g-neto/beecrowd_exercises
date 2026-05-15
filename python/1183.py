#Leitura da operação a ser feita
operacao = input()
#Criação da matriz utilizando list comprehension
matriz = [[float(input())for _ in range(12)] for _ in range(12)]
#Percorrendo os elemmentos acima da diagonal principal e guardando em uma lista separada
elementos = []
for l in range(12):
    for c in range(l+1, 12):
        elementos.append(matriz[l][c])
# Desvios de fluxo
if operacao == 'S':
    resultado = sum(elementos)
elif operacao == 'M':
    resultado = sum(elementos)/len(elementos)
print(f'{resultado:.1f}')