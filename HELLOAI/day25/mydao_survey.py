import cx_Oracle
import mybatis_mapper2sql
from day25.mylog import Mylog

class Sdao:
    def __init__(self):
#         self.mylog = Mylog()
        self.conn=cx_Oracle.connect("python/python@localhost:1521/xe")
        self.cs = self.conn.cursor()
        self.mapper= mybatis_mapper2sql.create_mapper(xml='mybatis_survey.xml')[0]
    def myselect(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        Mylog().getLogger().debug(sql)
#         self.mylog.logger.debug(sql)
        rs = self.cs.execute(sql)
        list = []
        for record in rs :
            list.append({'survey_id':record[0],'title':record[1],'content':record[2],'interview_cnt':record[3],'deadline':record[4],'in_date':record[5],'in_user_id':record[6],'up_date':record[7],'up_user_id':record[8]})
        return list
        
    def myinsert(self,survey_id, title, content, interview_cnt, deadline, in_date, in_user_id, up_date, up_user_id):
        sql  = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        Mylog().getLogger().debug(sql)
#         self.mylog.logger.debug(sql)
        self.cs.execute(sql,(survey_id, title, content, interview_cnt, deadline, in_user_id, up_user_id))
        cnt = self.cs.rowcount
        return cnt
    def myupdate(self,survey_id, title, content, interview_cnt, deadline, in_date, in_user_id, up_date, up_user_id):
        sql  = mybatis_mapper2sql.get_child_statement(self.mapper, "update")
        Mylog().getLogger().debug(sql)
#         self.mylog.logger.debug(sql)
        self.cs.execute(sql,(title, content, interview_cnt, deadline, up_user_id, survey_id))
        cnt = self.cs.rowcount
        return cnt
    def mydelete(self,survey_id):
        sql  = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")
        Mylog().getLogger().debug(sql)
#         self.mylog.logger.debug(sql)
        self.cs.execute(sql,(survey_id,))
        cnt = self.cs.rowcount
        return cnt   
    def __del__(self):
#         print("파괴자")
        self.conn.commit() 
        self.cs.close()
        self.conn.close()
        
# if __name__ == '__main__':
    
#     dao= MyDao()
#     list = dao.myselect()
#     print(list)
    
#     dao= MyDao()
#     list = dao.myinsert(9,9,9)
#     print(list)
    
#     dao= MyDao()
#     list = dao.myupdate(4,1,1)
#     print(list)
        
#     dao= MyDao()
#     list = dao.mydelete(1)
#     print(list)