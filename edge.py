# -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageFilter

#Checando e imprimindo os argumentos de linha de comando
if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")      

imagemOriginal = Image.open(sys.argv[1])

# O filtro EDGE_ENHANCE realça um pouco os pixels
imagemComFiltro = imagemOriginal.filter(ImageFilter.EDGE_ENHANCE)

imagemComFiltro.save(sys.argv[2])