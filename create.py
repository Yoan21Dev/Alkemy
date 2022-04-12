import os, sys,zlib, doctest, pprint
import textwrap
from pathlib import Path
import time, os.path
from string import Template
# os.makedirs(os.path.join('dataset','Scripts'))

# text = "holap"

# for linea in text.split():
#         print(linea)

# time = os.getcwd()
# print (time)
# print ( sys.argv)
# a = bytes('aaaa')
# t = zlib.compress(a)
# print (len(t))
# text = "skgjskjgksjgkskgskjdkgdkdkgdjgdjkgjksjgkshgkbsjvbsjgjsjgkjskgjskmgs.nskgjskjglslsgklskglksqslkglsglsgslg,ls, jsfkajfkajkfaf ,a fkafjam,m,naf,nf242355,"
# print (textwrap.fill(text, width=20))

# photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

# class BatchRename(Template):
#     delimiter = '%'

# fmt = input('Enter rename style (%d-dat e %n-seqnum %f-format): ')

# t = BatchRename(fmt)
# date = time.strftime('%d%b%y')
# for i, filename in enumerate(photofiles):
#  base, ext = os.path.splitext(filename)
#  newname = t.substitute(d=date, n=i, f=ext)
#  print ('{0} --> {1}'.format(filename, newname))
# import logging
# logging.debug(u'Información de depuración')
# logging.info(u'Mensaje informativo')
# logging.warning(u'Atención: archivo de configuración %s no se encuentra',
# 'server.conf')
# logging.error(u'Ocurrió un error')
# logging.critical(u'Error crítico -- cerrando')