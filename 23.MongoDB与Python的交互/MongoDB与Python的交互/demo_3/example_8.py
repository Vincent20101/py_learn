from mongo_db import client
from gridfs import GridFS
from bson.objectid import ObjectId

db=client.school
gfs=GridFS(db,collection="book")
document=gfs.get(ObjectId("5c1f2d50db1df31788fed5f3"))
file=open("D:/data/Linux手册.pdf","wb")
file.write(document.read())
file.close()