import socket
import time
import struct
import json
import ssl

class Connection:
	_address = None
	_ca_certs = None
	_ssl_version = None
	_ciphers = None

	__context = None
	__sock = None
	__ssl_socket = None

	def __init__(self, address, ca_certs, server_side, ssl_version=ssl.PROTOCOL_TLSv1_2, ciphers='ADH-AES256-SHA'):
		self._address = address
		self._ca_certs = ca_certs
		self._ssl_version = ssl_version
		self._ciphers = ciphers

		self.__context = ssl.SSLContext(ssl_version)
		self.__context.verify_mode = ssl.CERT_REQUIRED
		self.__context.use_privatekey_file('key.pem')
		self.__context.use_certificate_file('cert.pem')

	def receive(self, size, flags=None):
		if flags:
			return self.__ssl_socket.recv(size, flags)
		return self.__ssl_socket.recv(size)

	def connect(self):
		self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.__ssl_socket =
			self.__context.wrap_socket(
				self.__sock,
				cert_reqs=ssl.CERT_REQUIRED,
				ca_certs=self._ca_certs,
				ssl_version=self._ssl_version,
				ciphers=self._ciphers)
		self.__ssl_socket.connect(self._address)

	def close(self):
		self.__ssl_socket.close()

	def __enter__(self):
		self.connect()

	def __exit__(self, *args):
		self.close()


if __name__ == '__main__':
	import argparse
	import discovery

	argparser = argparse.ArgumentParser()
	group = argparser.add_mutually_exclusive_group()
	group.add_argument('-s', '--server', action='store_true', default=False)
	group.add_argument('-c', '--client', action='store_true', default=False)
	args = argparser.parse_args()

	if args.server:
		sender = multicast_listen_to_group(MCAST_GRP, MCAST_PORT)

	elif args.client:
		multicast_send_to_group(MCAST_GRP, MCAST_PORT)
	else:
		print('No arguments given, please define either -l or -m')

