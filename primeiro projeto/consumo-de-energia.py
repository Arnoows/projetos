#Programa para medir consumo de energia
#Autor: Arnoow
#Entrada
aparelho = input("Digite o tipo de aparelho (geladeira, televisão, computador): ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
tempo_diario = float(input("Digite o tempo diário de uso do aparelho em horas: "))
#Processamento
consumo_mensal = (potencia * tempo_diario * 30) / 1000
#Saída
print(f"\nO consumo mensal de energia do {aparelho} é de {consumo_mensal:.2f} kWh.")