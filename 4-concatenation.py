name= input("digite o nome do jogo\n")
yearLaunch= int(input("digite o ano do jogo\n"))
gamePrice = float(input("digite o preço do jogo\n"))
planIncluded= input("você quer o plano premium?\n")

# primeira concatenação

print("## DADOS DO JOGO: ##")
print("=====================")

# print("o nome do jogo é", name)
# print("o ano do jogo é", yearLaunch)
# print("o preço do jogo é", gamePrice)
# print("plano do jogo é", planIncluded)

# segunda forma de contatenação

# print("o nome do jogo é?", name, "\n o ano do jogo é?", yearLaunch, "\n o preço do jogo?", gamePrice,
#       "\n quer o plano do jogo?", planIncluded )

# terceira forma de concatenação

print(f"nome do jogo: {name} \nqual o ano do jogo:{yearLaunch} \nqual o preço do jogo: {gamePrice} \nquer o plano premium: {planIncluded}")
