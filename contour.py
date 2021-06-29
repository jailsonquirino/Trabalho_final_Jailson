# -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageFilter

#Checando e imprimindo os argumentos de linha de comando
if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")      

imagemOriginal = Image.open(sys.argv[1])

# O filtro CONTOUR faz um contorno aonde tem diferencia de cor entre os pixel
imagemComFiltro = imagemOriginal.filter(ImageFilter.CONTOUR)

imagemComFiltro.save(sys.argv[2])