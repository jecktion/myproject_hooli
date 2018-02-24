# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class School2Pipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlDB(object):
    def __init__(self):
        try:
            # self.conn = pymysql.connect('127.0.0.1','root','root','hooli_study',charset='utf8')
            self.conn = pymysql.connect('47.52.78.196', 'admin1', '759ce694b4', 'hooli_study', charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print('连接数据库失败：%s'% str(e))

    def close(self):
        self.cursor.close()
        self.conn.close()


class HooliPipeline(MysqlDB):
    def process_item(self,item,spider):
        sql='insert into hooli_school_university(url,university,country,city,overview,history,education,rank_W,rank_A,masters,research,career,student_services,housing_services,library_services,ICT_services,medical_services,campus_life,sports_facilities,student_clubs,students_number,other,create_time)'\
            'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update university=VALUES(university),country = VALUES(country),city= VALUES(city),overview= VALUES(overview),history = values(history),education=VALUES(education),rank_W=VALUES(rank_W),rank_A = values(rank_A),masters=VALUES(masters),research=values(research),career=values(career),student_services=values(student_services),housing_services=values(housing_services),library_services=values(library_services),ICT_services=values(ICT_services),medical_services=values(medical_services),campus_life=values(campus_life),sports_facilities=values(sports_facilities),student_clubs=values(student_clubs),students_number=values(students_number),other=values(other),create_time=values(create_time)'

        try:
            self.cursor.execute(sql,(
                item["url"],item["university"],item["country"],item["city"],item["overview"],item["history"],item["education"],item["rank_W"],item["rank_A"],item["masters"],item["research"],item["career"],item["student_services"],item["housing_services"],item["library_services"],item["ICT_services"],item["medical_services"],item["campus_life"],item["sports_facilities"],item["student_clubs"],item["students_number"],item["other"],item["create_time"]
            ))

            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
            print("执行sql语句失败")

        return item
