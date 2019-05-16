#!/usr/bin/python
#coding: utf-8
# Criado por b4l0x
#

import requests
import argparse as arg

print '''
    ___       __          _          _____           __         
   /   | ____/ /___ ___  (_)___     / __(_)___  ____/ /__  _____
  / /| |/ __  / __ `__ \/ / __ \   / /_/ / __ \/ __  / _ \/ ___/
 / ___ / /_/ / / / / / / / / / /  / __/ / / / / /_/ /  __/ /    
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/  /_/ /_/_/ /_/\__,_/\___/_/     
                                                                
'''

parser = arg.ArgumentParser(description="Admin finder criado por b4l0x..")
parser.add_argument("--url", help="Url do site..", required=True, action="store")
parser.add_argument("--wordlist", help="Use uma wordlist de pagina personalizadas, ou deixe em branco para padrao", 
default="lista.txt", action="store")
x = parser.parse_args()

try:
	print("[!] Iniciando procura...")
	ler = open(x.wordlist, "r")
	for pag in ler:
		page = pag.replace("\n", "")
		r = requests.get(x.url+page)
		rq = (r.status_code)
		if rq == 200:
			print("[!] Painel encontrado: {}").format(x.url+page)
			break
		elif rq != 200:
			print("[!] Nada em: {}").format(x.url+page)
except:
	print("[X] ERRO!")