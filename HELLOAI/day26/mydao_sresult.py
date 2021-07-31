import cx_Oracle
import mybatis_mapper2sql
from day26.mylog import Mylog


class MyDaoSresult:

    def __init__(self):
        self.conn = cx_Oracle.connect("python/python@localhost:1521/xe")
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_sresult.xml')[0]

    def myselect(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        Mylog().getLogger().debug(sql)
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            list.append({'survey_id':record[0], 's_seq':record[1], 'st_mobile':record[2], 'answer':record[3], 'in_date':record[4], 'in_user_id':record[5], 'update_id':record[6], 'up_user_id':record[7]})
        return list
    
    def myinsert(self, survey_id, s_seq, st_mobile, answer, in_date, in_user_id, update_id, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        Mylog().getLogger().debug(sql)
        self.cs.execute(sql, (survey_id, s_seq, st_mobile, answer, in_date, in_user_id, update_id, up_user_id))
        cnt = self.cs.rowcount
        return cnt

    def myupdate(self, survey_id, s_seq, st_mobile, answer, in_date, in_user_id, update_id, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")
        Mylog().getLogger().debug(sql)
        self.cs.execute(sql, (s_seq, st_mobile, answer, update_id, up_user_id, survey_id))
        cnt = self.cs.rowcount
        return cnt

    def mydelete(self, survey_id, s_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")
        Mylog().getLogger().debug(sql)
        self.cs.execute(sql, (survey_id, s_seq,))
        cnt = self.cs.rowcount
        return cnt   

    def __del__(self):
        self.conn.commit() 
        self.cs.close()
        self.conn.close()
        
