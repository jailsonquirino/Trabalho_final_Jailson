import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QMainWindow, QMessageBox, QPushButton, QLabel, QToolTip, QGridLayout, QWidget, QMessageBox
from PyQt5.QtCore import QSize
from PIL import Image
import subprocess

class Janela(QMainWindow): #MainWindow
    def __init__(self):
        super(Janela, self).__init__()        
        self.setup_main_window()
        self.carregarJanela() #initUI

    def setup_main_window(self):
        self.x = 800
        self.y = 600
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Processamento Digital de Imagens")
        self.wid = QWidget(self) #Cria o widget
        self.setCentralWidget(self.wid) #Fica no centro da janela
        self.layout = QGridLayout() #Cria o layout em grid
        self.wid.setLayout(self.layout) #Aplica o layout grid no widget

    def carregarJanela(self): #initUI
        #Criar os componentes (Label, Button, Text, Image)

        # Criando a barra menu
        self.barraMenu = self.menuBar() 

        # Criando os botões na barra de menu
        self.menuArquivo = self.barraMenu.addMenu("&Arquivo") 
        self.menuTransformacao = self.barraMenu.addMenu("&Transformação") 
        self.menuSobre = self.barraMenu.addMenu("&Sobre")

        # Criando as opções nos botões
        self.acaoAbrir = self.menuArquivo.addAction("Abrir") 
        self.acaoAbrir.triggered.connect(self.botaoAbrir)
        self.acaoSalvar = self.menuArquivo.addAction("Salvar como...") 
        self.acaoSalvar.triggered.connect(self.botaoSalvar)
        self.acaoFechar = self.menuArquivo.addAction("Fechar") 
        self.acaoFechar.triggered.connect(self.close) 

        self.acaoTransformar10 = self.menuTransformacao.addAction("Negativo")
        self.acaoTransformar10.triggered.connect(self.botaoTransformar10) 
        self.menuTransformacao.addSeparator()

        self.acaoTransformar11 = self.menuTransformacao.addAction("Correção gamma") 
        self.acaoTransformar11.triggered.connect(self.botaoTransformar11) 
        self.menuTransformacao.addSeparator()

        self.acaoTransformar25 = self.menuTransformacao.addAction("Escala de Cinza")
        self.acaoTransformar25.triggered.connect(self.botaoTransformar25)
        self.menuTransformacao.addSeparator()

        self.subMenu1 = self.menuTransformacao.addMenu("Filtros")
        self.acaoTransformar12 = self.subMenu1.addAction("Blur")
        self.acaoTransformar12.triggered.connect(self.botaoTransformar12)
        self.acaoTransformar13 = self.subMenu1.addAction("Contour")
        self.acaoTransformar13.triggered.connect(self.botaoTransformar13)
        self.acaoTransformar14 = self.subMenu1.addAction("Detail")
        self.acaoTransformar14.triggered.connect(self.botaoTransformar14)
        self.acaoTransformar15 = self.subMenu1.addAction("Edge Enhance")
        self.acaoTransformar15.triggered.connect(self.botaoTransformar15)
        self.acaoTransformar16 = self.subMenu1.addAction("Edge Enhance More")
        self.acaoTransformar16.triggered.connect(self.botaoTransformar16)
        self.acaoTransformar17 = self.subMenu1.addAction("Emboss")
        self.acaoTransformar17.triggered.connect(self.botaoTransformar17)
        self.acaoTransformar18 = self.subMenu1.addAction("Find Edges")
        self.acaoTransformar18.triggered.connect(self.botaoTransformar18)
        self.acaoTransformar19 = self.subMenu1.addAction("Sharpen")
        self.acaoTransformar19.triggered.connect(self.botaoTransformar19)
        self.acaoTransformar20 = self.subMenu1.addAction("Smooth")
        self.acaoTransformar20.triggered.connect(self.botaoTransformar20)
        self.acaoTransformar21 = self.subMenu1.addAction("Smooth More")
        self.acaoTransformar21.triggered.connect(self.botaoTransformar21)
        self.acaoTransformar22 = self.subMenu1.addAction("Kernel 1")
        self.acaoTransformar22.triggered.connect(self.botaoTransformar22)
        self.acaoTransformar23 = self.subMenu1.addAction("Kernel 2")
        self.acaoTransformar23.triggered.connect(self.botaoTransformar23)
        self.acaoTransformar24 = self.subMenu1.addAction("Kernel 3")
        self.acaoTransformar24.triggered.connect(self.botaoTransformar24)
        self.menuTransformacao.addSeparator()

        self.subMenu2 = self.menuTransformacao.addMenu("Camadas (R, G, B)")
        self.acaoTransformar26 = self.subMenu2.addAction("Camada R - Red")
        self.acaoTransformar26.triggered.connect(self.botaoTransformar26)
        self.acaoTransformar27 = self.subMenu2.addAction("Camada G - Green")
        self.acaoTransformar27.triggered.connect(self.botaoTransformar27)
        self.acaoTransformar28 = self.subMenu2.addAction("Camada B - Blue")
        self.acaoTransformar28.triggered.connect(self.botaoTransformar28)
        self.menuTransformacao.addSeparator()

        self.subMenu3 = self.menuTransformacao.addMenu("Girar")
        self.acaoTransformar4 = self.subMenu3.addAction("Rotacionar 90º") 
        self.acaoTransformar4.triggered.connect(self.botaoTransformar4)
        self.acaoTransformar5 = self.subMenu3.addAction("Ratocionar 180º") 
        self.acaoTransformar5.triggered.connect(self.botaoTransformar5)        
        self.acaoTransformar6 = self.subMenu3.addAction("Rotacionar 270º") 
        self.acaoTransformar6.triggered.connect(self.botaoTransformar6) 
        self.menuTransformacao.addSeparator()

        self.subMenu4 = self.menuTransformacao.addMenu("Esplelhar")
        self.acaoTransformar7 = self.subMenu4.addAction("Espelhar horizontal") 
        self.acaoTransformar7.triggered.connect(self.botaoTransformar7)
        self.acaoTransformar8 = self.subMenu4.addAction("Espelhar vetical") 
        self.acaoTransformar8.triggered.connect(self.botaoTransformar8)
        self.menuTransformacao.addSeparator()

        self.acaoTransformar9 = self.menuTransformacao.addAction("Transparencia") 
        self.acaoTransformar9.triggered.connect(self.botaoTransformar9)

        # Criando o sobre
        self.acaoSobre = self.menuSobre.addAction("Sobre o aplicativo")  
        self.acaoSobre.triggered.connect(self.botaoSobreapp)
        self.acaoSobre2 = self.menuSobre.addAction("Sobre a imagem")  
        self.acaoSobre2.triggered.connect(self.botaoSobreimg)

        #Criando um imagem
        self.imagem1 = QLabel(self) 
        self.endereco1 = 'imagens/arara.jpg'
        self.pixmap1 = QtGui.QPixmap(self.endereco1) 
        self.pixmap1 = self.pixmap1.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem1.setPixmap(self.pixmap1)
        self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

        #Imagem 2
        self.imagem2 = QLabel(self) 
        self.endereco2 = 'imagens/arara.jpg'
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

        #Organizando os componentes Widgets dentro do GridLayout
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)

    #OpenFileDialog
    def botaoAbrir(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption='Abrir arquivo', 
                                                            directory=QtCore.QDir.currentPath(), 
                                                            filter='All files (*.*);; Imagens (*.jpg; *.png)',
                                                            initialFilter='Imagens (*.jpg; *.png)')
        self.endereco1 = fileName
        self.pixmap1 = QtGui.QPixmap(self.endereco1) 
        self.pixmap1 = self.pixmap1.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)

    def botaoTransformar4(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_rotacionar_90.jpg'
        self.script = '.\grau_90.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar5(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_rotacioanr_180.jpg'
        self.script = '.\grau_180.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar6(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_rotacioanr_270.jpg'
        self.script = '.\grau_270.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar7(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_espelho_horizontal.jpg'
        self.script = '.\espelhar_horizontal.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar8(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_espelho_vertical.jpg'
        self.script = '.\espelhar_vertical.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar9(self):
        trans, okPressed = QInputDialog.getInt(self, "Inserir a porcentagem","Percentagem:", 10, 0, 100, 1)
        if okPressed:
            valor = str(trans)
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_transparencia.png'
        self.script = '.\Transparencia.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro + ' ' + valor
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar10(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_negativo.jpg'
        self.script = '.\egativo.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    
    def botaoTransformar11(self):
        trans, okPressed = QInputDialog.getInt(self, "Valor gamma","Valor:", 10, 0, 100, 1)
        if okPressed:
            valor = str(trans)
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_gama.png'
        self.script = '.\gamma.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro + ' ' + valor
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar12(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_blur.jpg'
        self.script = '.\Blur.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)
    
    def botaoTransformar13(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_contour.jpg'
        self.script = '.\contour.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)
        
    def botaoTransformar14(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_detail.jpg'
        self.script = '.\detail.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar15(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_edge_enhance.jpg'
        self.script = '.\edge.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar16(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_edge_enhance_more.jpg'
        self.script = '.\edge_more.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar17(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_emboss.jpg'
        self.script = '.\emboss.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar18(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_find_edges.jpg'
        self.script = '.\Find_edges.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar19(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_sharpen.jpg'
        self.script = '.\sharpen.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar20(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_smooth.jpg'
        self.script = '.\smooth.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar21(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_smooth_more.jpg'
        self.script = '.\smooth_more.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar22(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_kernel.jpg'
        self.script = '.\kernel1.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar23(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_kernel2.jpg'
        self.script = '.\kernel2.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar24(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_kernel3.jpg'
        self.script = '.\kernel3.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar25(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_cinza.jpg'
        self.script = '.\cinza.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar26(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_camadar.jpg'
        self.script = '.\camadar.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar27(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_camadag.jpg'
        self.script = '.\camadag.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar28(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_camadab.jpg'
        self.script = '.\camadab.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoSobreapp(self):
        self.menssagem = QMessageBox()
        self.menssagem.setIcon(QMessageBox.Information)
        self.menssagem.setWindowTitle("Sobre o aplicativo")
        self.menssagem.setText("Desenvolvido por Carlos Eduardo Casteliano de Paula e \nJailson Quirino de Paula\nlink: https://youtu.be/QRuHiBuEf4Q \nAplicativo de transformação de imagens.\nItuiutaba, 25 de junho de 2021.")
        self.menssagem.exec_()

    def botaoSobreimg(self):
        self.menssagem = QMessageBox()
        self.menssagem.setIcon(QMessageBox.Information)
        self.menssagem.setWindowTitle("Sobre a imagem")
        self.menssagem.setText("Informações sobre a imagem")
        formato = self.endereco1            
        partition1 = formato.rpartition('.')       
        nome = self.endereco1            
        partition2 = nome.rpartition('/')
        self.menssagem.setInformativeText("Nome do arquivo: " + partition2[2] + "\nFormato: " + partition1[2] + "\nAltura: 342\nLargura: 533")
        self.menssagem.exec_()

    def botaoSalvar(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(self, caption='Salvar como...', 
                                                            directory=QtCore.QDir.currentPath(), 
                                                            filter='Imagens (*.jpg)',
                                                            initialFilter='Imagens (*.jpg)')
        
        print(fileName) 

aplicacao = QApplication(sys.argv)        
j = Janela() #MainWindow
j.show()
sys.exit(aplicacao.exec_())