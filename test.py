import logging
import os
from webptools import cwebp

def probar():
    # dirección de los archivos de origen
    rawpath = 'C:/Users/Teclovers/projects/wpsender/images/raw/'

    # dirección de los archivos de destino
    outpath = 'C:/Users/Teclovers/projects/wpsender/images/outdir/'

    # listar y eliminar los archivos que existan en la carpeta de destino
    outdir_list = os.listdir(path=outpath)
    for item in outdir_list:
        os.remove(os.path.join(outpath,item))

    # listar y convertir los archivos que se encuentran en la carpeta de origen
    dir_list = os.listdir(path=rawpath)
    for item in dir_list:
        name = item.split('.')[0]
        cwebp(rawpath+item,outpath+name+'.webp',option='-q 80',logging='-v')

if __name__ == '__main__':
    probar()