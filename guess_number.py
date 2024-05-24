import random

print("Seja bem vindo ao Guess Number da Lane!")
choice_number = input("Digite o número teto do desafio: ")

if choice_number.isdigit():
  choice_number = int(choice_number)
else:
  print("Erro valor informado não é numérico. Execute novamente e informe um número!")
  quit()

random_number = random.randint(0, choice_number)

n_choices = 0
  
while True:
  answer_user = input("Advinhe o número: ")

  if answer_user.isdigit():
    answer_user = int(answer_user)
  else:
    print("Erro: valor informado não é numérico.Informe um número!")
    continue

  n_choices = n_choices + 1

  if answer_user == random_number:
    print("Acertou!")
    break
  elif answer_user > random_number:
    print("Tente um número menor!")
  else:
    print("Tente um número maior!")

print("N° de tentativas: " + str(n_choices))