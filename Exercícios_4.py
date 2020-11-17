#Q1

def armazena(valor):
    v = []
    for x in valor:
        if x != -1:
            v.append(x)
        if x == -1:
            break
    return v

def quant(lista):
    return (len(lista))

def ordem(lista):
    for x in lista:
        print(x)

def inversa(lista):
    for i in lista[::-1]:
        print(i)

def soma(lista):
    s = sum(lista)
    return s

def media(lista):
    return soma(lista)/len(lista)

def acima_media (lista):
    t = 0
    for x in lista:
        if x > media(lista):
            t = t+1
    return t
n = int(input("digite um número:"))
lista = [n]
while n != -1:
    n = int(input("digite um número:"))
    lista.append(n)
lista.remove(n)

print("quantidade de números:", quant(lista))
print("valores em ordem:", ordem(lista))
print("valores na ordem inversa:", inversa(lista))
print("soma dos valores:", soma(lista))
print("média dos valores:", media(lista))
print("quantidade de valores acima da média:", acima_media(lista))

#nao imprime as ordens

#Q2
def calculaAreaRetangulo(l1,l2):
    x = int(input("Lado 1:"))
    y = int(input("Lado 2:"))
    if l2 == 0:
        return l1*l1
    else:
        return l1*l2
print(calculaAreaRetangulo())

#Q3

vogal = lambda caractere: caractere.upper() in "AEIOU"
consoante = lambda caractere: caractere.upper() in "BCDFGHJKLMNPQRSTUXWZ"
numero = lambda caractere: caractere in "1234567890"

frase = input("Digite uma frase: ")

total_vogal = 0
total_consoante = 0
total_numero = 0
total_outros = 0

for caractere in frase:
if vogal(caractere):
total_vogal += 1
elif consoante(caractere):
total_consoante += 1
elif numero(caractere):
total_numero += 1
else:
total_outros += 1

print("Total de consoantes = %d" % total_consoante)
print("Total de vogais = %d" % total_vogal)
print("Total de números = %d" % total_numero)
print("Total de outros = %d" % total_outros)


