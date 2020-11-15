import operacoesCompra
n = 1

dic = {}
material = 0
total = []

while (material != "-1"):
    material = str(input("Digite o produto. Para parar, digite -1: "))
    if (material =="-1"):
        break
    preco = float(input("Preço:"))
    quant = float(input("Quantidade:"))
    tot = {material : [preco,quant]}
    dic.update(tot)

print(dic)
operacoesCompra.imprimeProdutos(dic)
operacoesCompra.imprimeQuantidade(dic)
operacoesCompra.calculaTotalCompras(dic)
