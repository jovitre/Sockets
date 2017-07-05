from sockets import Sock
import sys

IP = '127.0.0.1'
PORT = 6006
BUFFER_SIZE = 1024

if __name__ == '__main__':
    
    if not len(sys.argv) >= 2:
        print ("[SERVIDOR][ERRO]: O valor do saldo deve ser informado.")
        sys.exit(-1)

    saldo = int(sys.argv[1])

    print("[SERVIDOR]: Saldo inicial: {}".format(saldo))
    
    s = Sock(IP, PORT, saldo)

    while True:
        try:
            s.recv_msg(BUFFER_SIZE)
        except ConnectionError:
            print("[SERVIDOR][ERRO]: Cliente desconectado!")
            s.sock.close()
            break
