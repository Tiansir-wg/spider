# coding=utf-8
from pymongo import MongoClient


if __name__ == '__main__':

    # 和MongoDB建立连接
    client = MongoClient(host="localhost", port=27017)

    collection = client["movie"]["t1"]

    # 插入一条数据
    # collection.insert_one({"name": 'tiansir',"age": 12})

    # 插入多条数据,返回的结果是游标对象,可迭代,但只能读取一次
    # collection.insert_many([{"name": "tiansir"+str(i), "age": i} for i in range(10000)])

    # 查找数据
    # print collection.find()

    # 删除数据
    collection.delete_one({"name": "tiansir0"})
    print(collection.find({"name": "tiansir0"}).count())