#REPRESENTAÇÃO EXPLICITA DA LISTA DE ADJACÊNCIAS

lista_adj = { "A" : ["B"],
	      "B" : ["C", "D"],
	      "C" : ["B", "E"],
    	      "D" : ["A"],
	      "E" : ["B"]
	    }



#REPRESENTAÇÃO EXPLICITA DA MATRIZ DE ADJACÊNCIAS
#		 		 A B C D E
matriz_adj =   [[0,1,0,0,0], #A
		[0,0,1,1,0], #B
		[0,1,0,0,1], #C
		[1,0,0,0,0], #D
		[0,1,0,0,0]] #E



"""
Questão 15 -  Faça uma função para obter todos os 
nós adjacentes (vizinho) a um nó do grafo, 
dado que o grafo é representado por uma matriz de adjacências.

"""

def mostra_vizinho_matriz(vertice):

	if vertice == "A":
		print(matriz_adj[0])
	if vertice == "B":
		print(matriz_adj[1])
	if vertice == "C":
		print(matriz_adj[2])
	if vertice == "D":
		print(matriz_adj[3])
	if vertice == "E":
		print(matriz_adj[4])

"""
Questão 16 - Faça uma função para obter todos os nós adjacentes
(vizinho) a um nó do grafo, dado que o grafo é representado 
por uma lista de adjacências.

"""
def mostra_vizinho_lista(vertice):
	print(lista_adj[vertice])


mostra_vizinho_lista("B")
