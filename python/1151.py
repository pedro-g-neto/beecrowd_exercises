n = int(input())
a = 0
b = 1
sequencia = []
for _ in range(n):
    sequencia.append(str(a))
    a, b = b, a + b
    
print(' '.join(sequencia))
