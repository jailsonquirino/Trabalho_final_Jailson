# -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageFilter

#Checando e imprimindo os argumentos de linha de comando
if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")      

imagemOriginal = Image.open(sys.argv[1])
matrix = imagemOriginal.load()
for y in range(imagemOriginal.size[0]): # Coluna y
    for x in range(imagemOriginal.size[1]): # Linha x
        r = 255 - matrix[y, x][0]
        g = 255 - matrix[y, x][1]
        b = 255 - matrix[y, x][2]
        matrix[y,x] = (r, g, b)

imagemOriginal.save(sys.argv[2])