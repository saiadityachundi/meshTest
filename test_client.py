#!/usr/bin/python

import os
import sys
import socket

if len(sys.argv) >= 2:
    ip = sys.argv[1]
else:
    ip = "192.168.1.100"

# obtain env variables
namespace = os.environ["HOSTNAME"]
namespace_word = os.environ["NAMESPACE_WORD"]
port = 1230 + int(namespace.strip(namespace_word))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    sock.sendto("Hello GCS, I am " + namespace + "\n", (ip, port))
