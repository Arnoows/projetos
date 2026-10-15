# 1. Funcao para calcular as medias das disciplinas
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

# 2. Funcao para identificar alunos aprovados ou reprovados
def verificar_situacao(media):
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"

# 3. Funcao para gerar um relatorio simples de desempenho
def gerar_relatorio(nome_aluno, nota1, nota2, nota3):
    # Processamento coordenado
    media_final = calcular_media(nota1, nota2, nota3)
    situacao_final = verificar_situacao(media_final)
    
    # Saida de dados 
    print("--- Relatorio de Desempenho ---")
    print(f"Aluno: {nome_aluno}")
    print(f"Notas registradas: {nota1}, {nota2}, {nota3}")
    print(f"Media Alcancada: {media_final:.2f}")
    print(f"Situacao: {situacao_final}")
    print("-------------------------------")

# Programa Principal 
nome = "Carlos"
n1 = 7.5
n2 = 5.0
n3 = 8.0

gerar_relatorio(nome, n1, n2, n3)