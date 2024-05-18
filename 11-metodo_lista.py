entrega_list = ["SSD" , "Memoria RAM" , "PLACA DE VIDEO" ,
"PROCESSADOR" , "MOUSEPAD" ,"GABINETE"]

# Saber o tamanho de uma lista
print(len(entrega_list)) 

# retorna um objeto pelo o número do índice
print(entrega_list.index("PLACA DE VIDEO"))

# aDICIONAR UM OBJETO/ELEMENTO NO FINAL DA LISTA
entrega_list.append("PLACA MAE")
print(entrega_list)

# ORDENAR A LISTA
entrega_list.sort()
print(entrega_list)


# COPIAR OS OBJETOS DE UMA LISTA PARA OUTRA
entregue_list = entrega_list.copy()
entregue_list.remove("SSD")
print(entregue_list)


# REMOVER TODOS OS ELEMENTOS DA LISTA
entrega_list.clear()
print(entrega_list)