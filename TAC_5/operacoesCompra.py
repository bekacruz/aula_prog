def imprimeProdutos(dic):
    print("Produtos:")
    for x in dic:
        print(x)
def imprimeQuantidade(dic):
    print ("Quantidade por produto:")
    for x in dic:
        print(x, '\t', dic[x][1])
def calculaTotalCompras(dic):
    print ("Preços (unitário e por produto):")
    t=0
    for x in dic:
        v = dic[x][0] * dic[x][1]
        t = t + v
        print (x, '\t', dic[x][0], '\t', v)
    print ("Total da compra: %s" %t)

