import cx_Oracle
import mybatis_mapper2sql
from day25.mylog import Mylog

class Stargetdao:
    def __init__(self):
#         self.mylog = Mylog()
        self.conn=cx_Oracle.connect("python/python@localhost:1521/xe")
        self.cs = self.conn.cursor()
        self.mapper= mybatis_mapper2sql.create_mapper(xml='mybatis_starget.xml')[0]
    def myselect(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        Mylog().getLogger().debug(sql)
#         self.mylog.logger.debug(sql)
        rs = self.cs.execute(sql)
        list = []
        for record in rs :
            list.append({'survey_id':record[0],'st_tel':record[1],'complete_yn':record[2],'in_date':record[3],'in_user_id':record[4],'up_date':record[5],'up_user_id':record[6]})
        return list
        
    def myinsert(self,survey_id, st_tel, complete_yn, in_date, in_user_id, up_date, up_user_id):
        sql  = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        Mylog().getLogger().debug(sql)
#         self.mylog.logger.debug(sql)
        self.cs.execute(sql,(survey_id, st_tel, complete_yn, up_date, up_user_id))
        cnt = self.cs.rowcount
        return cnt
    def myupdate(self,survey_id, st_tel, complete_yn, in_date, in_user_id, up_date, up_user_id):
        sql  = mybatis_mapper2sql.get_child_statement(self.mapper, "update")
        Mylog().getLogger().debug(sql)
#         self.mylog.logger.debug(sql)
        self.cs.execute(sql,(st_tel, complete_yn, up_user_id, survey_id))
        cnt = self.cs.rowcount
        return cnt
    def mydelete(self,survey_id,st_tel):
        sql  = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")
        Mylog().getLogger().debug(sql)
#         self.mylog.logger.debug(sql)
        self.cs.execute(sql,(survey_id,st_tel,))
        cnt = self.cs.rowcount
        return cnt   
    def __del__(self):
#         print("파괴자")
        self.conn.commit() 
        self.cs.close()
        self.conn.close()
        
# if __name__ == '__main__':
#     
#     dao= Sdetaildao()
#     list = dao.myselect()
#     print(list)
    
#     dao= MyDao()
#     list = dao.myinsert(9,9,9)
#     print(list)
    
#     dao= Sdetaildao()
#     list = dao.myupdate(1,2,3,4,5,6,7,8,9,10,11)
#     print(list)
        
#     dao= MyDao()
#     list = dao.mydelete(1)
#     print(list)