#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 08:29:16 2021

@author: marunga
"""

"""
A caso seja interessante configurar o conjunto de pesos manualmente
esse deve ser o formato

# Pesos da camada de entrada
w1 = np.array([[-0.424,-0.740,-0.961],
               [0.358, -0.577, -0.469]])
# Pesos da camada intermediária
w2 = np.array([[-0.017],[-0.893],[0.148]])
"""

import numpy as np
import matplotlib.pyplot as plt

#Função de Ativação
def sigmoid(valor):
    return 1/(1+ np.exp(-valor))

# Derivada da função ativação
def sigmoidDerivate(sig):
    return sig*(1-sig)


# Entradas para o operador lógico XOR
x = np.array([[0,0],
             [0,1],
             [1,0],
             [1,1]])

# Saidas para o operador lógico XOR
y = np.array([[0],[1],[1],[0]])

# Quantidade de Neurônios na camada de entrada
neuro_input = 2

# Quantidade de Neurônios na camada intermediária
neuro_hiden = 3

# Quantidade de Neurônios na camada de saída
neuro_output = 1

# Inicializando aleatóriamente um conjunto de pesos, camada de entrada
w1 = 2*np.random.random((neuro_input,neuro_hiden))-1

# Inicializando aleatóriamente um conjunto de pesos, camada intermediaria
w2 = 2*np.random.random((neuro_hiden,neuro_output))-1

# Épocas/ Quantidade de treinos
time_training = 1000000

# Momento
momentum =1 

# Taxa de aprendizado
learning_rate = 0.3

# Criando lista com histórico de erro para plotagem
list_mse = []

# Criando uma lista elementos com as épocas para plotagem
list_time_training = np.arange(0,time_training,1)

for i in range(time_training):
    input_layer = x
    
    # Produto escalar entre camada entrada e os seus respectivos pesos
    input_synapse = np.dot(input_layer, w1)
    hiden_layer = sigmoid(input_synapse)
    
    # Produto escalar entre camada intermediaria e os seus respectivos pesos
    hiden_synapse = np.dot(hiden_layer,w2)
    output_layer = sigmoid(hiden_synapse)
    
    # Calculando erros da camada de saída
    erro_output_layer = y - output_layer
    
    # Erro médio quadrático
    mse = np.mean(erro_output_layer**2)
    
    # Salvando o MSE em uma lista para plotagem
    list_mse.append(mse)
    
    # Calculando pesos da camada de saída
    output_derivate = sigmoidDerivate(output_layer)
    output_delta = erro_output_layer*output_derivate
    
    # Calculando pesos da camada intermediaria
    w2_transposed = w2.T 
    delta_output_w2 = output_delta.dot(w2_transposed)
    hiden_delta = delta_output_w2*sigmoidDerivate(hiden_layer)
    
    # Atualizando os pesos da camada intermediaria
    hiden_layer_transposed = hiden_layer.T
    w2_new = hiden_layer_transposed.dot(output_delta)
    w2 = (w2*momentum)+(w2_new*learning_rate)
    
    # Atualizando os pesos da camada de entrada
    input_layer_tranposed = input_layer.T
    w1_new = input_layer_tranposed.dot(hiden_delta)
    w1 = (w1*momentum)+(w1_new*learning_rate)
    
# Plotando grafico de linha
fig, ax = plt.subplots()
ax.plot(list_time_training, list_mse)  
ax.set(xlabel='Época', ylabel='Taxa de erro',
       title='Relação de Época e Taxa de erro')
ax.grid()
fig.savefig("test.png")
plt.show()



