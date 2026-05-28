# primeira tentativa, talvez não tenha sido aceito devido a nao receber os valores na mesma linha
#values = []
#
#while (len(values) <= 2):
#  values.append(int(input()))
#
#print(sorted(values))
#print('\n')
#print(values)

# o map gera um objeto a set iterado (lazy)
# poderia ser utilizado também para atribuir a variaveis distintas como: var1, var2 = map(int, str1.split())
values = list(map(int, input().split()))

for v in sorted(values):
  print(v)

print()

for v in values:
  print(v)