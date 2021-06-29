  
import sys
from PIL import Image

if __name__ == "__main__":
    print(f'quanto argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

imagemOriginal = Image.open(sys.argv[1])

matrizB = imagemOriginal.load()

for i in range(imagemOriginal.size[0]):
    for j in range(imagemOriginal.size[1]):
        b = matrizB[i, j][0]
        matrizB[i,j] = (0, 0, b)

imagemOriginal.save(sys.argv[2])