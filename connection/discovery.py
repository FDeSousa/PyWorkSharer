# Clients broadcast their existence to register with servers
# Servers then start a connection to a client to establish a key via Diffie-Hellman key exchange
# Once a shared key has been set up, client and server can communicate via encrypted means
import socket
import time
import struct
import json
import ssl

MCAST_GRP = '224.224.1.1' # This has to match between client/server
MCAST_PORT = 5007 # So does this, or client/server won't see the message

TIME_STRUCT = struct.Struct('!d')

def multicast_send_to_group(group, port, max_hops=2):
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sock:
		sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, max_hops)

		print('Preparing to send multicast')

		t = time.time()
		data = TIME_STRUCT.pack(t)

		print('Sending time:', str(t))
		print('Sending time packed as data:', data)

		sock.sendto(data, (group, port))

		print('Finished multicast')

def multicast_listen_to_group(group, port):
	data = sender = None

	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sock:
		# Options to support re-use of address and port
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

		# We want to listen for broadcasts on this group and port
		sock.bind((group, port))
		mreq = struct.pack('4sl', socket.inet_aton(group), socket.INADDR_ANY)
		sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

		print('Waiting for multicast')
		data, sender = sock.recvfrom(10240, 0)

	print('Received time packed as data:', data)
	print('Time unpacked:', TIME_STRUCT.unpack(data))
	print('From sender:', sender)
	print('Finished listening')

	return sender


if __name__ == '__main__':
	import argparse
	argparser = argparse.ArgumentParser()
	group = argparser.add_mutually_exclusive_group()
	group.add_argument('-l', '--listen', action='store_true', default=False)
	group.add_argument('-m', '--multicast', action='store_true', default=False)
	args = argparser.parse_args()

	if args.listen:
		multicast_listen_to_group(MCAST_GRP, MCAST_PORT)
	elif args.multicast:
		multicast_send_to_group(MCAST_GRP, MCAST_PORT)
	else:
		print('No arguments given, please define either -l or -m')
