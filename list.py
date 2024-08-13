# Lista é uma coleção ordenada mutável. Permite membros duplicados.
# index:   0      1     2  3
lista = ["carro", True, 2, 3.5]   
print(lista)
print (type(lista))  
print(lista[1])
print("."*30) 
  
# Tupla é uma colação ordenada imutável. Permite memmbros duplicados.
# index:  0       1     2  3
tupla = ("carro", True, 2, 3.5) 
print(tupla) 
print(type(tupla))  
print(tupla[3])
print("."*30) 
   
# O dicionário é uma coleção ordenada e mutável. Nenhum membro duplicado.
               #chave:  Valor
dicionario = {"nome": "carro", "logica": True, "numero": 2, "outroNumero": 3.5} 
print(dicionario) 
print(type(dicionario))  
print(dicionario["logica"])
print("."*30) 

# Set é uma coleção não ordenada não mutável e não indexada. Nenhum membro duplicado. 
conjunto = {"carro" True, 2, 3.5} 
print(conjunto)  
print(type(conjunto)) 
print(conjunto[1])