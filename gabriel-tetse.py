import os 

def clear():
  os.system('clear')

def menu():
  while True:
    try:
      banner()
      print("[1] atacar")
      print("[2] sair")
      escolha = int(input("whatsapp@gabriel > "))
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
