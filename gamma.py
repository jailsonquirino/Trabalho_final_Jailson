# -*- coding: utf-8 -*-
import sys
from PIL import Image

if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")      

imagemOriginal = Image.open(sys.argv[1])
matrix = imagemOriginal.load()
gamma = int(sys.argv[3])

for y in range(imagemOriginal.size[0]):
    for x in range(imagemOriginal.size[1]):
      r = int ((matrix[y, x][0]/255) ** gamma * 255)
      g = int ((matrix[y, x][1]/255) ** gamma * 255)
      b = int ((matrix[y, x][2]/255) ** gamma * 255)
      matrix[y, x] = (r, g, b)

imagemOriginal.save(sys.argv[2])