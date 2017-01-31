#!/usr/bin/python3

fich=open("/etc/passwd","r")
usuarios=fich.readlines()

mydic={}
for usuario in usuarios:
    token=usuario.split(':')
    mydic[token[0]]=token[-1][:-1]

print("usuario root: ", mydic["root"])
try:
    print("usuario imaginario: ", mydic["imaginario"])
except KeyError:
    print("El usuario imaginari no existe")
