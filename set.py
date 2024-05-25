gamesSet = {"fifa23", "Read Dead 2", "Star Wars", "Mario Odyssey", "The Legend of Zelda"}

print(type(gamesSet))

# 1 - buscar o tamenho do set 
print (len(gamesSet))

# 2 - true e 1 são considerados o mesmo valor 
exampleSet = { "fifa23", True, 1, 90.50}
print(exampleSet)

# 3 - adicionar item de outro set
gamesSet.update(exampleSet)
print(gamesSet)

# 4 - remover um item no set
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)


#não possibilita recuperar valores via fatiamento ou slice