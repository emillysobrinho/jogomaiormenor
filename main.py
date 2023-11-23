import random
numero_atual = random.randint(1, 100)
print(f"O número atual é {numero_atual}.")
proximo_numero = random.randint(1,100)
escolha = input("O proximo número será maior ou menor? " )
print(f"O proximo numero é {proximo_numero}.")
if escolha == "maior" and proximo_numero > numero_atual:
  print('você acertou!')
elif escolha == "menor" and proximo_numero < numero_atual:
  print('Você acertou!')
if escolha != "menor" and proximo_numero < numero_atual:
  print('você errou!')
elif escolha != "maior" and proximo_numero > numero_atual:
  print('Você errou!')
