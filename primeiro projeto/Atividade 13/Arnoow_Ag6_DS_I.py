#Sistema de Desconto
valor = float(input("Digite o valor da compra: "))
if valor < 200:
    desconto = valor * 0.05 
    print (f"O desconto aplicado é de R$ {desconto:.2f}")
elif valor >= 200 and valor < 300: 
    desconto = valor * 0.10
    print (f"O desconto aplicado é de R$ {desconto:.2f}")
elif valor >= 300:
    desconto = valor * 0.15
    print (f"O desconto aplicado é de R$ {desconto:.2f}")

