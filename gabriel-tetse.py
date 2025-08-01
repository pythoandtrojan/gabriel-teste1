import os 

def clear():
  os.system('clear')

def banner():
  print("""
    ██╗    ██╗██╗  ██╗ █████╗ ████████╗███████╗ █████╗ ██████╗ 
    ██║    ██║██║  ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
    ██║ █╗ ██║███████║███████║   ██║   ███████╗███████║██████╔╝
    ██║███╗██║██╔══██║██╔══██║   ██║   ╚════██║██╔══██║██╔═══╝ 
    ╚███╔███╔╝██║  ██║██║  ██║   ██║   ███████║██║  ██║██║     
     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝ 
     AUTHOR: Gabriel | INSTA: gabriel_ynn | 31/7/2008
                     whatsappTookit """)

def menu():
  while True:
    try:
      banner()
      print("[1] atacar")
      print("[2] sair")
      escolha = int(input("whatsapp@root > "))
      if escolha == 1:
        try:
          numero = int(input("numero alvo(ex 94051041): "))
        except ValueError:
          print("somente numeros")
          input("precione enter pra continuar")
          clear()
          continue
        for i in range(1, 100000):
          print(f"atacando o {numero} > ({i}/100000)")
          input("precione enter pra continuar")
          os.system('python main.py')
          clear()
          continue
      elif escolha == 2:
        print("==== EXIT ====")
        exit()
      else:
        print("escolha invalida")
        os.syystem('python main.py')
    except ValueError:
      print("somente numeros!!")
      input("precione enter pra continuar")
      clear()
      continue
      
          
menu()
