import socket
import threading

class Sock:

    def __init__(self, IP, PORT, saldo):
        'Inicializa a classe sock'
        
        print("[SERVIDOR]: Inicializando o socket")
        self.create_socket(IP, PORT)
        self.saldo = saldo

    def create_socket(self, IP, PORT):
        'Inicializa, de fato, o socket, conectando ao IP e a porta'
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((IP, PORT))
        self.sock.setblocking(0)

    def recv_msg(self, BUFFER_SIZE):
        'Recebe mensagem do cliente'

        self.sock.listen(5)
        while True:
            print("[SERVIDOR]: Aguardando cliente")
            try:
                self.sock.settimeout(60)
                self.conn, self.addr = self.sock.accept()
                threading.Thread(target = self.handle_op, args = (BUFFER_SIZE, )).start()
            except socket.timeout:
                print("[SERVIDOR][ERRO]: Tempo limite esgotado!")
                raise ConnectionError()

    def handle_op(self, BUFFER_SIZE):
        'Lida com a execucao da operacao'
        
        while True:
            op = self.conn.recv(BUFFER_SIZE).decode('utf-8') 
            if not op:
                raise error("[SERVIDOR]: Cliente desconectado")
                return
            
            op = op.strip('\n')
            op = op.lower().split()
        
            operacao = op[0]
            resposta = 'Seu saldo eh: '
            
            print("[SERVIDOR]: Operacao de {}".format(operacao.capitalize()))
            
            if operacao == 'saldo':
                print("[SERVIDOR]: Enviando o saldo para o cliente")
                resposta += str(self.saldo) 
                self.conn.send(resposta.encode())
                return self.saldo

            if operacao == 'debito':
                val = int(op[1])
                self.saldo -= val
                resposta += str(self.saldo)
                self.conn.send(resposta.encode())
                return self.saldo

            if operacao == 'credito':
                val = int(op[1])
                self.saldo += val
                resposta += str(self.saldo) 
                self.conn.send(resposta.encode())
                return self.saldo













        
