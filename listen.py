import socket
import struct

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 50001
IS_ALL_GROUPS = False

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if IS_ALL_GROUPS:
    sock.bind(('', MCAST_PORT))
else:
    sock.bind((MCAST_GRP, MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

b = b'-'
while b != b'':
    b = sock.recv(65536)
    print(b.decode('latin-1'), end='')