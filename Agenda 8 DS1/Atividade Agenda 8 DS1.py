opiniao_excelente = 0
opiniao_ruim = 0
for i in range(10):
    print("Bem vindo a pesquisa da empresa. Responda o que você pensa sobre o curso!")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opiniao = int(input("Digite sua opinião sobre o curso 1- Excelente, 2 - Bom, 3 - Ruim: "))
    if opiniao == 1:
        print("Obrigado pelo feedback positivo!")
        opiniao_excelente += 1
    elif opiniao == 2:
        print("Agradecemos sua opinião e vamos trabalhar para melhorar.")
    elif opiniao == 3:
        print("Lamentamos que sua experiência não tenha sido satisfatória. Vamos buscar melhorias.")
        opiniao_ruim += 1
print("RESULTADO DA PESQUISA")
print(f"a) Quantidade de respostas 'EXCELENTE': {opiniao_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {opiniao_ruim}")