import socket
import sys
import psutil
import json

ip = '192.168.1.39'
port = 6666

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def getNetworkInfo():
    networkInfo = {}
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            networkInfo["interface Name"] = interface_name
            if str(address.family) == 'AddressFamily.AF_INET':
                networkInfo["IP Address"] = address.address
                networkInfo["Netmask"] = address.netmask
                networkInfo["Broadcast IP"] = address.broadcast
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                networkInfo["MAC Address"] = address.address
                networkInfo["Netmask"] = address.netmask
                networkInfo["Broadcast MAC"] = address.broadcast
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    networkInfo["Total Bytes Sent"] = get_size(net_io.bytes_sent)
    networkInfo["Total Bytes Received"] = get_size(net_io.bytes_recv)
    return networkInfo

def getTargetInfo():
    targetInfo = {}
    targetInfo["OS"] = sys.platform
    targetInfo["Network"] = getNetworkInfo()
    return json.dumps(targetInfo)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip, port)
    sock.connect(address)

    msg = sock.recv(1024)
    sendMsgToServer = getTargetInfo()
    sock.send(sendMsgToServer.encode())
    print(msg.decode())

    sock.close()

if __name__ == "__main__":
        main()
        
