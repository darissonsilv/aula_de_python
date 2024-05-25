LoteCarro = {
    "name" : "strada",
    "anoDeLancamento" : 2010,
    "motor" : 1.4,
    "cor" : "preto",
    "carroPreco": 47.000,
    "estilo": ["adventure","urbano"] #lista dentro de um dicionário
    
}

print(LoteCarro)
print(len(LoteCarro))
print(type(LoteCarro))

# 1- apresentar um elemento do dicionário
print(LoteCarro['estilo'])
print(LoteCarro['carroPreco'])

# 2- buscar as chaves do dicionário:
print(LoteCarro.keys()) 

# 3 -buscar os valores do dicionário:
print(LoteCarro.values())

# 4 -buscar itens do dicionário com chave e valor:
print(LoteCarro.items())

# 5 - adicionar itens no dicionário :
LoteCarro["compradores"] = 2
print(LoteCarro)

# 6 - atualizar item no dicionario :
LoteCarro.update({"compradores": 1})
print(LoteCarro)

# 7 - remover item no dicionário :

LoteCarro.pop("compradores")
print(LoteCarro)

