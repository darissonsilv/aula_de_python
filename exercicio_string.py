gameName = "Fifa 23"
gameDescript = """
fifa 2023 
um dos melhores jogos da atualidade
jogo desenvolvido por EA Sports 
"""

char = gameName[0].lower()
# crie uma variavel chamada char dentro dela coloquei a 
# gameName na posição 0 e coloquei o comando menúsculo
new_name = gameName.replace(char,'$')
# criei outra variavel com o nome new_name e dentro dela chamei a gameName
# substituindo o comendo " char" pelo $
new_name = char + new_name[1:] 
# usei a mesma variavel new_name , trago o char e aplico o new_name na posição [1] em diante
print(new_name)