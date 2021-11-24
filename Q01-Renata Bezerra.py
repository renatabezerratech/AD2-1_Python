# -*- coding: utf-8 -*-
"""
@author: Renata Silva Bezerra
"""
def tamanho_lin(mat):
    aux = [0]*len(mat)
    for i in range(len(mat)):
        aux[i] = len(mat[i])
    return aux

def maior(vet):
    maior = vet[0]
    for i in range(len(vet)):
        if vet[i] > maior:
            maior = vet[i]
    return maior

def mat_max_elent(mat, maior):
    quant = 0
    tan_linha = tamanho_lin(matriz)
    maior = maior(tan_linha)
    
    for i in range(len(mat)):
        if len(mat[i]) == maior:
            print(mat[i])
            quant += len(mat[i]) 
            
    print('Quantidade de elementos:', quant)
    return None

def transposta(mat):
    mat_t=[[j[0] for j in mat],[j[1] for j in mat]]
    for i in mat_t:
        print(i)
    return None
    
matriz = []
arq = open(input('Entre com o nome do arquivo: '), 'r')

linha = arq.readline()

if linha == '':
    print('Nenhuma matriz foi encontrada no arquivo!!!')
else:
    while linha != '':
        matriz.append(linha.split())
        linha = arq.readline()
        
    print('Matriz com mais elementos:')
    mat_max_elent(matriz, maior)
    
    print('Transposta da Matriz com mais elementos:')
    # transposta(matriz) 

arq.close()