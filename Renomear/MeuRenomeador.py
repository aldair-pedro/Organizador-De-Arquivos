# -*- coding: utf-8 -*-
import os

"""
Created on Wed Mar  4 01:20:50 2026

@author: AP
"""

pasta=r"C:\Users\AP\Desktop\Arquivos\.png"
i=1
historico=[]
for file in os.listdir(pasta):
    name,ext=os.path.splitext(file)
    nome_antigo=os.path.join(pasta,file)
    nome_novo="file_"+str(i).zfill(2)+".png"
    caminho_novo_nome=os.path.join(pasta,nome_novo)
    os.rename(nome_antigo,caminho_novo_nome)
    i+=1
    historico.append(f"Renomed:{name} -> {nome_novo}")
for i in historico:
    with open("Renomeados.txt","w") as arquivo:
        arquivo.write(f"{historico}")
    
   

        
        