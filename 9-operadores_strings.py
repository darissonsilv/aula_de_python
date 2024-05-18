gameName = "GTA"
gameDescript = """
    GTA V, É UM DOS MELHORES JOGOS DA ATUALIDADE, 
    OS JOGADORES TEM UMA BOA AVALIAÇÃO,
    VERSÃO MOBILE E EM PC

"""

print(gameDescript.lower()) #deixar a string com letra minúscula 
print(gameDescript.upper()) #deixar a string com letra maiúscula 
print(gameDescript.title()) #deixar a string com a letra inicial maiúscula
print(gameDescript.capitalize()) #deixar a string com a letra inicial maiúscula
print(gameName.center(24,'=')) #centralizar a string e preencher os espaços 
print(gameName.find("A")) # retorna a posição do caractere
print(gameDescript.count("A")) # diz a quantidade de caracteres indicado
print(gameDescript.replace("GTA V","FREE-FIRE")) # altera a string por outra nova 
print(gameDescript.split(","))