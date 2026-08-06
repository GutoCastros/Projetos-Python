# os.walk
# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('/Users', 'Guto', 'Documentos', 'Curso Python - UDEMY - 2026', 'Projeto')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print(' ', the_counter, 'dir_', dir_)


    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print(' ', the_counter, 'FILE:', caminho_completo_arquivo)
      
      
      
       # ESSE COMANDO DELETA TUDO QUE ESTEJA NA PASTA
       # os.unlink(caminho_completo_arquivo) 

