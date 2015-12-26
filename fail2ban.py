import sys
import datetime
from pymongo import MongoClient
import socket
import config
# conexion con mongo
dbm = config.dbm
try:
    int(sys.argv[2])
    port = sys.argv[2]
except:
    port = socket.getservbyname(sys.argv[2])
dbm.logs.insert({"IP": sys.argv[3], "name": sys.argv[1], "port": sys.argv[2],
                 "datetime": datetime.datetime.now()})
