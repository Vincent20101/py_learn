from mongo_db import client
from gridfs import GridFS
from bson.objectid import ObjectId
import math
import datetime

db=client.school
gfs=GridFS(db,collection="book")
book=gfs.find_one({"filename":"Linux就该这么学.pdf"})
print(book.filename)
print(book.type)
print(book.keyword)
print("%dM"%math.ceil(book.length/1024/1024))
print("---------------------")
books=gfs.find({"type":"PDF"})
for one in books:
    uploadDate=one.uploadDate+datetime.timedelta(hours=8)
    uploadDate=uploadDate.strftime("%Y-%m-%d %H:%M:%S")
    print(one._id,one.filename,uploadDate)
print("---------------------")
rs=gfs.exists(ObjectId("5c1f2d50db1df31788fed5f3"))
print(rs)
rs=gfs.exists(**{"type":"PDF"})
print(rs)