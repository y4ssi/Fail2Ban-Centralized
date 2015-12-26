import datetime
from pymongo import MongoClient
import os
import config
# conexion con mongo
dbm = config.dbm
now = datetime.datetime.now()
delta = now - datetime.timedelta(hours=1)
bans = dbm.logs.find({"datetime": {"$gt": delta}})
for ban in bans:
    command = "fail2ban-client set jaula " + "bainip " + ban['IP']
    os.system(command)
