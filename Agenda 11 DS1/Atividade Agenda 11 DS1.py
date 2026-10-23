from colorama import Fore, Style

#Lista armazenando as mensagens dos níveis do reservatório 
mensagens_niveis = [
    "Muito baixo (crítico)", # Nível 1
    "Baixo",                 # Nível 2
    "Médio",                 # Nível 3
    "Alto",                  # Nível 4
    "Muito alto (alerta)"    # Nível 5
]
# Função para definir a cor e exibir a mensagem de alerta
def Alerta_nivel_reservatório(nivel):
    if nivel == 1:
        print(Fore.RED + mensagens_niveis[nivel - 1] + Style.RESET_ALL)
    elif nivel == 2:
        print(Fore.YELLOW + mensagens_niveis[nivel - 1] + Style.RESET_ALL)   
    elif nivel == 3:
        print(Fore.GREEN + mensagens_niveis[nivel - 1] + Style.RESET_ALL)  
    elif nivel == 4:
        print(Fore.CYAN + mensagens_niveis[nivel - 1] + Style.RESET_ALL) 
    elif nivel == 5:
        print(Fore.BLUE + mensagens_niveis[nivel - 1] + Style.RESET_ALL)
    else:
        print("Nível inválido. Por favor, insira um nível entre 1 e 5." + Style.RESET_ALL)
for numero in range(1, 6):
    Alerta_nivel_reservatório(numero)