#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 6006
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
resposta = None

print ("[SERVIDOR] Abrindo a porta " + str(TCP_PORT) + " e ouvindo")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

while 1:
    s.listen(1)
    print ("[SERVIDOR] Aguardando conexao")
    conn, addr = s.accept()
    print ('[SERVIDOR] Conexao com o cliente realizada. Endereco da conexao:', addr)
    print ("[SERVIDOR] Aguardando dados do cliente")
    data = conn.recv(BUFFER_SIZE).decode("utf-8")
    if not data: break
    print ("[SERVIDOR] Dados recebidos do cliente com sucesso: " + data)
    print ("[SERVIDOR] Enviando resposta para o cliente")
    conn.send(data.encode())  # echo
    print ("[SERVIDOR] Resposta enviada: " + data)
    
print ("[SERVIDOR] Fechando a porta " + str(TCP_PORT))
conn.close()
print ("[SERVIDOR] Fim")
