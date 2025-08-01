import os
import requests
from colorama import Fore, Style, init
init(autoreset=True)

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(Fore.GREEN + """
   _____ _             _    _____       _        
  / ____| |           | |  |  __ \     | |       
 | (___ | |_ __ _ _ __| | _| |__) |___ | | _____ 
  \___ \| __/ _` | '__| |/ /  _  // _ \| |/ / __|
  ____) | || (_| | |  |   <| | \ \ (_) |   <\__ \\
 |_____/ \__\__,_|_|  |_|\_\_|  \_\___/|_|\_\___/
    """ + Style.RESET_ALL)

def obter_ip():
    try:
        resposta = requests.get('https://api.ipify.org?format=json', timeout=5)
        if resposta.status_code == 200:
            return resposta.json()['ip']
        return "Não foi possível obter o IP"
    except:
        return "Erro ao conectar"
def menu():
    while True:
        try:
            clear()
            banner()
            ip = obter_ip()
            print(Fore.YELLOW + f" Seu IP público: {ip}" + Style.RESET_ALL)
            print("\n" + Fore.CYAN + " [1] Atacar")
            print(" [2] Sair" + Style.RESET_ALL)
            
            escolha = int(input(Fore.MAGENTA + "\n whatsapp@gabriel > " + Style.RESET_ALL))
            
            if escolha == 1:
                try:
                    numero = int(input(" Número alvo (ex 94051041): "))
                except ValueError:
                    print(Fore.RED + " Somente números!" + Style.RESET_ALL)
                    input(" Pressione ENTER para continuar")
                    continue
                
                for i in range(1, 100000):
                    clear()
                    print(Fore.RED + f" Atacando o {numero} > ({i}/100000)" + Style.RESET_ALL)
                    input(" Pressione ENTER para continuar")
                    os.system('python main.py')
                    
            elif escolha == 2:
                print(Fore.RED + "\n ==== EXIT ====" + Style.RESET_ALL)
                exit()
            else:
                print(Fore.RED + " Escolha inválida!" + Style.RESET_ALL)
                input(" Pressione ENTER para continuar")
                
        except ValueError:
            print(Fore.RED + " Somente números!" + Style.RESET_ALL)
            input(" Pressione ENTER para continuar")

if __name__ == "__main__":
    menu()
