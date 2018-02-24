# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class School1Pipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlDB(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect('127.0.0.1','root','root','hooli_study',charset='utf8')
            # self.conn = pymysql.connect('47.52.78.196', 'admin1', '759ce694b4', 'hooli_study', charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print('连接数据库失败：%s'% str(e))

    def close(self):
        self.cursor.close()
        self.conn.close()




# class HooliPipeline_2(MysqlDB):
#     def process_item(self,item,spider):
#         sql='insert into school_gs_3(url,university,department,programme,bachelor,overview,modules,Evaluation_method,career,IELTS,ALevel,IB,crawltime)'\
#             'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update programme = values(programme),university = values(university),crawltime=VALUES (crawltime)'
#
#         try:
#
#             self.cursor.execute(sql,(
#                 item["url"],item["university"],item["department"],item["programme"],item["bachelor"],item["overview"],item["modules"],item["Evaluation_method"],item["career"],item["IELTS"],item["ALevel"],item["IB"],item["crawltime"]
#             ))
#
#             self.conn.commit()
#         except Exception as e:
#             self.conn.rollback()
#             print(e)
#             print("执行sql语句失败")
#
#         return item




# class HooliPipeline_2(MysqlDB):
#     def process_item(self,item,spider):
#         sql='insert into school_gs_5(url,programme,modules,Evaluation_method)'\
#             'VALUES (%s,%s,%s,%s)on duplicate key update programme = values(programme),modules = values(modules),Evaluation_method=VALUES (Evaluation_method)'
#
#         try:
#
#             self.cursor.execute(sql,(
#                 item["url"],item["programme"],item["modules"],item["Evaluation_method"]
#             ))
#
#             self.conn.commit()
#         except Exception as e:
#             self.conn.rollback()
#             print(e)
#             print("执行sql语句失败")
#
#         return item


# class HooliPipeline_2(MysqlDB):
#     def process_item(self,item,spider):
#         sql='insert into school_gs_6(url,university,department,programme,CourseOverview,startdate,UCAS,Course_length,modules,Evaluation_method,Alevel,IELTS,career,tuition_fee)'\
#             'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update programme = values(programme),modules = values(modules),Evaluation_method=VALUES (Evaluation_method)'
#
#         try:
#
#             self.cursor.execute(sql,(
#                 item["url"],item["university"],item["department"],item["programme"],item["CourseOverview"],item["startdate"],item["UCAS"],item["Course_length"],item["modules"],item["Evaluation_method"],item["Alevel"],item["IELTS"],item["career"],item["tuition_fee"]
#             ))
#
#             self.conn.commit()
#         except Exception as e:
#             self.conn.rollback()
#             print(e)
#             print("执行sql语句失败")
#
#         return item


# class HooliPipeline_2(MysqlDB):
#     def process_item(self,item,spider):
#         sql='insert into school_gs_8(url,department,Course,UcasCode,Duration,Alevel,IB,Location,CourseOverview,Modules,EntryRequirements,Assessment,Career,Other)'\
#             'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update department = values(department),modules = values(modules),Assessment=VALUES(Assessment)'
#
#         try:
#
#             self.cursor.execute(sql,(
#                 item["url"],item["department"],item["Course"],item["UcasCode"],item["Duration"],item["Alevel"],item["IB"],item["Location"],item["CourseOverview"],item["Modules"],item["EntryRequirements"],item["Assessment"],item["Career"],item["Other"]
#             ))
#
#             self.conn.commit()
#         except Exception as e:
#             self.conn.rollback()
#             print(e)
#             print("执行sql语句失败")
#
#         return item


# class HooliPipeline_2(MysqlDB):
#     def process_item(self,item,spider):
#         sql='insert into school_gd_1(url,Department,Programme,Duration,Start_Date,Location,Overview,Modules,Teaching_and_Assessment,Career,EntryRequirements,TOEFL,IELTS,Tuition_Fee,Master,crawltime)'\
#             'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update Department = values(Department),Modules = values(Modules),Master=VALUES(Master)'
#
#         try:
#
#             self.cursor.execute(sql,(
#                 item["url"],item["Department"],item["Programme"],item["Duration"],item["Start_Date"],item["Location"],item["Overview"],item["Modules"],item["Teaching_and_Assessment"],item["Career"],item["EntryRequirements"],item["TOEFL"],item["IELTS"],item["Tuition_Fee"],item["Master"],item["crawltime"]
#             ))
#
#             self.conn.commit()
#         except Exception as e:
#             self.conn.rollback()
#             print(e)
#             print("执行sql语句失败")
#
#         return item



# class HooliPipeline_2(MysqlDB):
#     def process_item(self,item,spider):
#         sql='insert into hooli_x(url,university,department,programme,ucas_code,degree_type,start_date,overview,mode,types,duration,modules,teaching_assessment,career,application_date,deadline,application_fee,tuition_fee,location,Rntry_requirements,GPA,average_score,accredited_university,Alevel,IB,IELTS,TOEFL,GRE,GMAT,working_experience,interview,portfolio,application_documents,how_to_apply,entry_requirements,school_test,description_degree,SATI,SATII,SAT_code,ACT,ACT_code,other)'\
#             'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update programme = values(programme),ucas_code = values(ucas_code),degree_type=VALUES(degree_type),start_date=values(start_date),overview=values(overview),mode=values(mode),types=values(types),duration=values(duration),modules=values(modules),teaching_assessment=values(teaching_assessment),career=values(career),application_date=values(application_date),deadline=values(deadline),application_fee=values(application_fee),tuition_fee=values(tuition_fee),location=values(location),Rntry_requirements=values(Rntry_requirements),GPA=values(GPA),average_score=values(average_score),accredited_university=values(accredited_university),Alevel=values(Alevel),IB=values(IB),IELTS=values(IELTS),TOEFL=values(TOEFL),GRE=values(GRE),GMAT=values(GMAT),working_experience=values(working_experience),interview=values(interview),portfolio=values(portfolio),application_documents=values(application_documents),application_documents=values(application_documents),entry_requirements=values(entry_requirements),school_test=values(school_test),description_degree=values(description_degree),SATI=values(SATI),SATII=values(SATII),SAT_code=values(SAT_code),ACT=values(ACT),ACT_code=values(ACT_code),other=values(other),url=values(url)'
#
#         try:
#             self.cursor.execute(sql,(
#                 item["url"],item["university"],item["department"],item["programme"],item["ucas_code"],item["degree_type"],item["start_date"],item["overview"],item["mode"],item["types"],item["duration"],item["modules"],item["teaching_assessment"],item["career"],item["application_date"],item["deadline"],item["application_fee"],item["tuition_fee"],item["location"],item["Rntry_requirements"],item["GPA"],item["average_score"],item["accredited_university"],item["Alevel"],item["IB"],item["IELTS"],item["TOEFL"],item["GRE"],item["GMAT"],item["working_experience"],item["interview"],item["portfolio"],item["application_documents"],item["how_to_apply"],item["entry_requirements"],item["school_test"],item["description_degree"],item["SATI"],item["SATII"],item["SAT_code"],item["ACT"],item["ACT_code"],item["other"]
#             ))
#
#             self.conn.commit()
#         except Exception as e:
#             self.conn.rollback()
#             print(e)
#             print("执行sql语句失败")
#
#         return item



class HooliPipeline_2(MysqlDB):
    def process_item(self,item,spider):
        sql='insert into tmp_school_majors(url,university,country,city,website,department,programme,ucas_code,degree_type,degree_level,start_date,degree_description,overview,mode,duration,modules,teaching,assessment,career,application_date,deadline,application_fee,tuition_fee,location,ATAS,GPA,average_score,accredited_university,Alevel,IB,IELTS,IELTS_L,IELTS_S,IELTS_R,IELTS_W,TOEFL,TOEFL_L,TOEFL_S,TOEFL_R,TOEFL_W,GRE,GMAT,LSAT,MCAT,working_experience,interview,portfolio,application_documents,how_to_apply,entry_requirements,chinese_requirements,school_test,SATI,SATII,SAT_code,ACT,ACT_code,other,create_time)'\
            'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update university=VALUES(university),department = VALUES(department),country = VALUES(country),city= VALUES(city),website= VALUES(website),programme = values(programme),degree_level=VALUES(degree_level),degree_type=VALUES(degree_type),ucas_code = values(ucas_code),degree_type=VALUES(degree_type),start_date=values(start_date),overview=values(overview),mode=values(mode),duration=values(duration),modules=values(modules),teaching=values(teaching),assessment=values(assessment),career=values(career),application_date=values(application_date),deadline=values(deadline),application_fee=values(application_fee),tuition_fee=values(tuition_fee),location=values(location),GPA=values(GPA),average_score=values(average_score),accredited_university=values(accredited_university),Alevel=values(Alevel),IB=values(IB),IELTS=values(IELTS),IELTS_L=values(IELTS_L),IELTS_S=values(IELTS_S),IELTS_R=values(IELTS_R),IELTS_W=values(IELTS_W),TOEFL=values(TOEFL),TOEFL_L=values(TOEFL_L),TOEFL_S=values(TOEFL_S),TOEFL_R=values(TOEFL_R),TOEFL_W=values(TOEFL_W),GRE=values(GRE),GMAT=values(GMAT),LSAT=VALUES(LSAT),MCAT=VALUES(MCAT),working_experience=values(working_experience),interview=values(interview),portfolio=values(portfolio),application_documents=values(application_documents),application_documents=values(application_documents),how_to_apply=VALUES(how_to_apply),entry_requirements=values(entry_requirements),chinese_requirements=VALUES(chinese_requirements),ATAS=VALUES(ATAS),school_test=values(school_test),degree_description=values(degree_description),SATI=values(SATI),SATII=values(SATII),SAT_code=values(SAT_code),ACT=values(ACT),ACT_code=values(ACT_code),other=values(other),url=values(url)'

        try:
            self.cursor.execute(sql,(
                item["url"],item["university"],item["country"],item["city"],item["website"],item["department"],item["programme"],item["ucas_code"],item["degree_type"],item["degree_level"],item["start_date"],item["degree_description"],item["overview"],item["mode"],item["duration"],item["modules"],item["teaching"],item["assessment"],item["career"],item["application_date"],item["deadline"],item["application_fee"],item["tuition_fee"],item["location"],item["ATAS"],item["GPA"],item["average_score"],item["accredited_university"],item["Alevel"],item["IB"],item["IELTS"],item["IELTS_L"],item["IELTS_S"],item["IELTS_R"],item["IELTS_W"],item["TOEFL"],item["TOEFL_L"],item["TOEFL_S"],item["TOEFL_R"],item["TOEFL_W"],item["GRE"],item["GMAT"],item["LSAT"],item["MCAT"],item["working_experience"],item["interview"],item["portfolio"],item["application_documents"],item["how_to_apply"],item["entry_requirements"],item["chinese_requirements"],item["school_test"],item["SATI"],item["SATII"],item["SAT_code"],item["ACT"],item["ACT_code"],item["other"],item["create_time"]
            ))

            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
            print("执行sql语句失败")

        return item


# class HooliPipeline_2(MysqlDB):
#     def process_item(self,item,spider):
#         sql='insert into tmp_school_majors(url,university,country,city,website,department,programme,ucas_code,degree_type,degree_level,start_date,degree_description,overview,mode,duration,modules,teaching,assessment,career,application_date,deadline,application_fee,tuition_fee,location,ATAS,GPA,average_score,accredited_university,Alevel,IB,IELTS,IELTS_L,IELTS_S,IELTS_R,IELTS_W,TOEFL,TOEFL_L,TOEFL_S,TOEFL_R,TOEFL_W,GRE,GMAT,LSAT,MCAT,working_experience,interview,portfolio,application_documents,how_to_apply,entry_requirements,chinese_requirements,school_test,SATI,SATII,SAT_code,ACT,ACT_code,other,create_time)'\
#             'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#
#         try:
#             self.cursor.execute(sql,(
#                 item["url"],item["university"],item["country"],item["city"],item["website"],item["department"],item["programme"],item["ucas_code"],item["degree_type"],item["degree_level"],item["start_date"],item["degree_description"],item["overview"],item["mode"],item["duration"],item["modules"],item["teaching"],item["assessment"],item["career"],item["application_date"],item["deadline"],item["application_fee"],item["tuition_fee"],item["location"],item["ATAS"],item["GPA"],item["average_score"],item["accredited_university"],item["Alevel"],item["IB"],item["IELTS"],item["IELTS_L"],item["IELTS_S"],item["IELTS_R"],item["IELTS_W"],item["TOEFL"],item["TOEFL_L"],item["TOEFL_S"],item["TOEFL_R"],item["TOEFL_W"],item["GRE"],item["GMAT"],item["LSAT"],item["MCAT"],item["working_experience"],item["interview"],item["portfolio"],item["application_documents"],item["how_to_apply"],item["entry_requirements"],item["chinese_requirements"],item["school_test"],item["SATI"],item["SATII"],item["SAT_code"],item["ACT"],item["ACT_code"],item["other"],item["create_time"]
#             ))
#
#             self.conn.commit()
#         except Exception as e:
#             self.conn.rollback()
#             print(e)
#             print("执行sql语句失败")
#
#         return item