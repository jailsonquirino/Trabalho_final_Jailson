# -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageFilter

#Checando e imprimindo os argumentos de linha de comando
if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")      

imagemOriginal = Image.open(sys.argv[1])

kernel1 = ImageFilter.Kernel((3,3), (1, 0, -1, 0, 0, 0, -1, 0, 1), 1, 0)
imagemComFiltro = imagemOriginal.filter(kernel1)

imagemComFiltro.save(sys.argv[2])