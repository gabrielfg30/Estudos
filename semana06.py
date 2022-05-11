s = 'algoritmos'
for c in s:
    if c in 'aeiou': #Vai imprimir no terminal apenas as vogais
        print(c)

l = ['cão', 'gato', 'coelho']
print(l)
for i in l: #Transformando o i em l mostrara todos os componentes de l um por um como uma lista
    print(i)

acum = 0
for z in range(1, 100):
    if z % 2 == 0:
        acum = acum + z
print(acum)

a = ['a', 'b', 'c']
for b in range(len(a)): #Vai mostrar o tamanho da lista
    print(a[b])

for x in range(10): #Vai repetir até o 10 mas não vai repetir o 10 em sí
    print(x)

for y in range(1, 20, 2): #Vai ir do 1 ao 20 com passo 2 (pulando de 2 em 2)
    print(y)

num = eval(input('Digite um número positivo:')) 
while num < 0: #While feito para repetir a pergunta caso digitem números negativos
    num = eval(input('Digite um número positivo:'))

d = [] #criei um lista para por nomes onde o while vai parar quando der enter sem caractere
nome = input('Digite um nome:')
while nome != '':
    d.append(nome)
    nome = input('Digite um nome:')

for e in d:
    print(e)
