# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import re, pymysql

client = MongoClient()
collection = client['xs']['xyp']

class BiquduoPipeline:
    def process_item(self, item, spider):
        # for x in range(len(item["chapter"])):
        #     d = re.sub('\s', ' ', item["chapter"][x])
        #     print(d)

        # with open("./data/" + item["bookname"][0] + ".txt", 'a') as f:
        #     f.write(item["chaptername"] + "\n")
        #     for x in range(len(item["chapter"])):  # 循环取出String
        #         d = re.sub('\s', ' ', item["chapter"][x])
        #         d = re.sub(u'\u2022', ' ', d)
        #         f.write(d + "\n")
        collection.insert(item)
        return item
