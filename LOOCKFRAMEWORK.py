#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import time
import socket
import smtplib
import getpass
import webbrowser
import os
 
print('\n © 2017 Copyright TODOS OS DIREITOS RESERVADOS POR GABRIEL SANTOS')
 
print('''
 
----------------------------------------------------------------------------------------------------------------------------------
 
 ███████╗██████╗  █████╗ ███╗   ███╗███████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗    ██╗      ██████╗  ██████╗  ██████╗██╗  ██╗
 ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝    ██║     ██╔═══██╗██╔═══██╗██╔════╝██║ ██╔╝
 █████╗  ██████╔╝███████║██╔████╔██║█████╗  ██║ █╗ ██║██║   ██║██████╔╝█████╔╝     ██║     ██║   ██║██║   ██║██║     █████╔╝
 ██╔══╝  ██╔══██╗██╔══██║██║╚██╔╝██║██╔══╝  ██║███╗██║██║   ██║██╔══██╗██╔═██╗     ██║     ██║   ██║██║   ██║██║     ██╔═██╗
 ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗    ███████╗╚██████╔╝╚██████╔╝╚██████╗██║  ██╗
 ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝
 
----------------------------------------------------------------------------------------------------------------------------------
 X------------------------------------X
 |    By: Gabriel Santos e Lord13     |
 X------------------------------------X
 
\n [!] ESCOLHA UMA OPTION:
\n [+] 1 - BUSCIP - SITES 6.0
\n [+] 2 - BLOG - VIEW 7.0
\n [+] 3 - SEND - MAIL 7.0 (SPAM)
 
''')
 
opt = input('\n OPTION: ')
 
def blog_view():
    print('''
 ██████╗ ██╗      ██████╗  ██████╗               ██╗   ██╗██╗███████╗██╗    ██╗    
 ██╔══██╗██║     ██╔═══██╗██╔════╝               ██║   ██║██║██╔════╝██║    ██║    
 ██████╔╝██║     ██║   ██║██║  ███╗    █████╗    ██║   ██║██║█████╗  ██║ █╗ ██║    
 ██╔══██╗██║     ██║   ██║██║   ██║    ╚════╝    ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║    
 ██████╔╝███████╗╚██████╔╝╚██████╔╝               ╚████╔╝ ██║███████╗╚███╔███╔╝    
 ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝                 ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝
   X---------------------------------------------------------------------X                                                        
   | By: Gabriel Santos // My Github: https://github.com/LoockUnderwood  |                                                                                                                                                                                            
   X---------------------------------------------------------------------X ''')
 
    url = input("\n [!] -  Coloque a Url do Blog: ")
    refresh = eval(input("\n [!] -  Caso queira, coloque o tempo de refresh em segundos, se não quiser coloque 0: "))
    vezes = int(input("\n [!] -  Coloque o Número de Views que desejas ganhar: "))
    print('\n [!] -   ESPERE 5 SEGUNDOS POR FAVOR.')
    time.sleep(5)
 
    print('\n--------------------------------------')
 
    def openurl():
        print("\n [!] -  !Views Adquiridas!")
        webbrowser.open(url)
        print("\n")
 
    for i in range(vezes):
        openurl()
        time.sleep(refresh)
 
def buscip():
    print('''
 ██████╗ ██╗   ██╗███████╗ ██████╗██╗██████╗               ███████╗██╗████████╗███████╗███████╗
 ██╔══██╗██║   ██║██╔════╝██╔════╝██║██╔══██╗              ██╔════╝██║╚══██╔══╝██╔════╝██╔════╝
 ██████╔╝██║   ██║███████╗██║     ██║██████╔╝    █████╗    ███████╗██║   ██║   █████╗  ███████╗
 ██╔══██╗██║   ██║╚════██║██║     ██║██╔═══╝     ╚════╝    ╚════██║██║   ██║   ██╔══╝  ╚════██║
 ██████╔╝╚██████╔╝███████║╚██████╗██║██║                   ███████║██║   ██║   ███████╗███████║
 ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝╚═╝╚═╝                   ╚══════╝╚═╝   ╚═╝   ╚══════╝╚══════╝
           X---------------------------------------------------------------------X                                                        
           | By: Gabriel Santos // My Github: https://github.com/LoockUnderwood  |                                                                                                                                                                                            
           X---------------------------------------------------------------------X ''')
   
    end = input("\n [+] - Digite o ENDEREÇO do site: ")
    print("\n [+] - IP do mesmo -> "+socket.gethostbyname(end))
    print("\n [!] - OBS: O PROGRAMA FECHARÁ EM 4 SEGUNDOS.")
    time.sleep(4)
    exit()
 
 
def send_mail():
    print('''
 
 ███████╗███████╗███╗   ██╗██████╗               ███╗   ███╗ █████╗ ██╗██╗        ██████╗ ██╗   ██╗
 ██╔════╝██╔════╝████╗  ██║██╔══██╗              ████╗ ████║██╔══██╗██║██║        ██╔══██╗╚██╗ ██╔╝
 ███████╗█████╗  ██╔██╗ ██║██║  ██║    █████╗    ██╔████╔██║███████║██║██║        ██████╔╝ ╚████╔╝
 ╚════██║██╔══╝  ██║╚██╗██║██║  ██║    ╚════╝    ██║╚██╔╝██║██╔══██║██║██║        ██╔═══╝   ╚██╔╝  
 ███████║███████╗██║ ╚████║██████╔╝              ██║ ╚═╝ ██║██║  ██║██║███████╗██╗██║        ██║  
 ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝               ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚═╝        ╚═╝
           X---------------------------------------------------------------------X                                                        
           | By: Gabriel Santos // My Github: https://github.com/LoockUnderwood  |                                                                                                                                                                                            
           X---------------------------------------------------------------------X

           
 \n OBS: - É NECESSÁRIO PERMITIR LOGUINS NO SEU GMAIL SEM SER PELO SITE.
 \n OBS: - CALMA, ISSO NÃO VAI VAZAR OS SEUS DADOS.

 \n [!]  - BASTA ACESSAR ESTE LINK E ATIVAR, DEPOIS DO PROCESSO PODES DESATIVAR.

 \n [!]  - LINK: myaccount.google.com/lesssecureapps ''')
 
    de = input('\n [!]  - Digite o seu Email: ')
    sen = getpass.getpass("\n [!] - Digite a sua Senha: ")
    para = input('\n [!]  - Digite o Email do Alvo: ')
    msg = input('\n [!]  - Digite a Mensagem: ')
    vezes = int(input('\n [!]  - Digite a quantidade de mensagens a serem enviadas: '))
    print('\n [!]  - ESPERE 4 SEGUNDOS POR FAVOR.')
    time.sleep(4)
 
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    x = 1
    smtp.login(de, sen)
    while x <= vezes:
        smtp.sendmail(de, para, msg)
        print("\n [!]  - [%d Enviado Sucefull!]" % x)
        x += 1        
    print('\n [!] - OBS: O PROGRAMA FECHARÁ EM 4 SEGUNDOS.')
    time.sleep(4)
 
 
###################################################################################################################
 
# ÁREA DO BUSCIP - SITES.PY
 
if opt == '2':
    blog_view()
 
###################################################################################################################
 
# ÁREA DO BLOG - VIEW.PY
 
elif opt == '1':
    buscip()
       
###################################################################################################################
 
# ÁREA DO SEND - MAIL.PY
 
elif opt == '3':
    send_mail()
 
else:
    print('\n [!] -  !OPTION INEXISTENTE NESSA VERSÃO!')
    for i in range(4):
        print("\n [!] -  SAINDO DO PROGRAMA EM %s SEG...\r" % str(4-i))

        
        time.sleep(1)
