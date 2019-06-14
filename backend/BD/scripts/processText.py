#!/usr/local/bin/python3.7

import sys, re

file = sys.argv[1]

f = open('../turtle/out.ttl', 'w')
sys.stdout = f

#abrir o ficheiro e ler o conteudo
text = open(file).read()

#Captar os números ordinais e traduzir dando cast para inteiro
text = re.sub(r"\"(\")", r"\1", text)

print(text)
