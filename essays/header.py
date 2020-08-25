from PIL import Image
import numpy as np
import glob
import os
import xlrd

types = ('*.png', '*.jpg', '*.jpeg', '*.tif')
images = []

thresh = 0.1
crop_lenght = 250 # from aspect.py
#Fuvest: 120
#Enem: 250

test_ration = 1.4 # from aspect.py
#Fuvest: 1.4
#Enem: 1.4

# Parte inicial do titulo da imagem depois do algoritmo
#Fuvest
title = ('./cropped/Nota-{0}-Red{1}.png', './processed/Nota-{0}-Red{1}.png', './not-cropped/Nota-{0}-Red{1}.png')
#Enem -->> NAO USA PLANILHA
#     -->> Modificar .format() linhas 46, 52, 56
#title = ('./cropped/{0}-Red{1}', './processed/{0}-Red{1}', './not-cropped/{0}-Red{1}')

# Adiciona todas as imagens dos tipos types()
for tp in types:
    images.extend(glob.glob(tp))

images.sort(key=os.path.getmtime)

# Abre a planilha de notas
#   Notas devem estar ordenadas por data de
# envio da redacao, na 1o coluna da 1o pagina
wb = xlrd.open_workbook('./notas.xlsx')
sheet = wb.sheet_by_index(0)

for i in range( len(images) ):
    im = Image.open( images[i] )
    imarr = np.array(im)
    aspectratio = float(imarr.shape[0]) / float(imarr.shape[1])

    #   Se a imagem for menor do que o parametro,
    # ela ja esta cortada
    if aspectratio < test_ration - thresh :
        im.save(title[0].format( sheet.cell_value(i, 0), i ) )
    #   Se estiver no intervalo desejado, e so a redacao,
    # entao corte
    elif  test_ration - thresh < aspectratio < test_ration + thresh :
        cropped = imarr[ crop_lenght:imarr.shape[0], :imarr.shape[1] ]
        nimg = Image.fromarray(cropped)
        nimg.save(title[1].format( sheet.cell_value(i, 0), i ) )
    #   Se for maior, deve ser um print, que deve ser
    # cortado manualmente
    elif aspectratio > test_ration + thresh :
        im.save(title[2].format( sheet.cell_value(i, 0), i ) )