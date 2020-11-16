#Q1
valor = [float(x) for x in input("Digite uma sequência aleatória de números:").split()]
media = float(sum(valor)/len(valor))
n=0
p=0
for num in valor:
    if num < 0:
        n = n+1
    elif num > 0:
        p=p+1
print("média:", media, "positivos:", p, "porcentagem:",((p/len(valor))*100), "negativos:", n, "porcentagem", ((n/len(valor))*100), sep=" ")


#Q2
def aprovacao(total_faltas, nota_1, nota_2, nota_3):
    nome = str(input("nome do aluno:"))
    pct = float((total_faltas/80)*100)
    media = float((nota_1+nota_2+nota_3)/3)
    if pct <=25 and media >= 7.0:
        print("nome: ", nome, "média:", media, "faltas: ", pct, "APROVADO")
    elif pct > 25 and media >= 7.0:
        print("nome: ", nome, "média:", media, "faltas: ", pct, "REPROVADO POR FALTA")
    elif media < 7.0 and pct <= 25:
        print("nome: ", nome, "média:", media, "faltas: ", pct, "REPROVADO POR MÉDIA")
    elif pct > 25 and media <=7.0:
        print("nome: ", nome, "média:", media, "faltas: ", pct, "REPROVADO POR FALTA E MÉDIA")

#Q3
def IMC (alt,peso):
    IMC = peso/(alt**2)
    if IMC < 18.5:
        print(IMC, "Abaixo do Peso")
    elif IMC > 18.5 or IMC < 25:
        print(IMC, "Peso Normal")
    elif IMC > 25 or IMC < 30:
        print(IMC, "Acima do Peso")
    elif IMC > 30:
        print(IMC, "Obeso")




