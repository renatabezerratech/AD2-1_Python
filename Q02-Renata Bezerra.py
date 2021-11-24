# -*- coding: utf-8 -*-
# coding: utf-8
"""
@author: Renata Silva Bezerra
"""
def remover(mat, p):
    for i in range(len(p)):
        plv = p[i]
        for j in range(len(mat)):
            x = mat[j].count(plv)
            if x > 0:
                mat[j].remove(plv)
    return None

def escrever(mat, arquivo):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            arquivo.write(mat[i][j] + ' ')
        arquivo.write('\n')

palavras = input('Entre com as palavras que deseja remover: ').split()

a = input('Entre com o nome do arquivo: ')

arq = open(a, 'r', encoding='utf-8')

matriz = []
linha = arq.readline()

if linha == '':
    print('Nenhuma texto foi encontrada no arquivo!!!')
else:
    while linha != '':
        matriz.append(linha.split())
        linha = arq.readline()
        
    remover(matriz, palavras)
    
    arq.close()
    
    arq = open(a, 'w', encoding='utf-8')
    
    escrever(matriz, arq)
        
arq.close()
    
