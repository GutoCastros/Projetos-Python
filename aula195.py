# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
# C:\Users\Guto\Documentos\Curso Python - UDEMY - 2026\Projeto\dados
import os

caminho = os.path.join('/Users', 'Guto', 'Documentos', 'Curso Python - UDEMY - 2026', 'Projeto')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    
    if not os.path.isdir(caminho_completo_pasta ):
        continue

    for imagem in os.listdir(caminho_completo_pasta ):
            print('     ', imagem)




