import sys
from PIL import Image

if __name__ == "__main__":
    print(f'quanto argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

imagemOriginal = Image.open(sys.argv[1])

matrizR = imagemOriginal.load()

for i in range(imagemOriginal.size[0]):
    for j in range(imagemOriginal.size[1]):
        r = matrizR[i, j][0]
        matrizR[i,j] = (r, 0, 0)

imagemOriginal.save(sys.argv[2])