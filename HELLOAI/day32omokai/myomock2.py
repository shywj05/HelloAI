import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.Qt import QIcon
from PyQt5.QtCore import *
from notebook.services.contents.handlers import _checkpoint_id_regex
import cx_Oracle
import random

form_class = uic.loadUiType("myomock2.ui")[0]


class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mystate = 0
        self.pb.clicked.connect(self.myclick)
        self.flag_wb = True
        self.flag_ing = True
        self.history2 = []
        self.pb2d = []
        self.arr2d = [
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0,  0, 0, 0, 0, 0]
                ]
        
        for i in range(10):
            line = []
            for j in range(10):
                temp = QPushButton("", self)
                temp.clicked.connect(self.myclick)
                temp.setIcon(QIcon("0.png"))
                temp.setIconSize(QSize(50, 50))
                temp.setGeometry(j * 40, i * 40, 40, 40)
                temp.setToolTip(str(i) + "," + str(j))
                line.append(temp)
            self.pb2d.append(line)
        
        self.pb.clicked.connect(self.myreset)    
        self.myrender()
        
    def myinsertDB(self,history,win):
        conn=cx_Oracle.connect("python/python@localhost:1521/xe")
        cs = conn.cursor()
        cs.execute("SELECT NVL(MAX(PAN)+1,1) FROM OMOK")
        pan = 0
        for record in cs :
            pan = record
        sql = "insert into omok(pan, pseq, history, win) values (:1,:2,:3,:4)"
        for n,i in enumerate(history): 
            cs.execute(sql,(pan[0],n+1,i,win))
        
        conn.commit()    
        cs.close()
        conn.close()
    
    def myreset(self):
        print("클릭")
        self.flag_wb = True
        self.flag_ing = True
        for i in range(10):
            for j in range(10):
                self.arr2d[i][j] = 0
        self.myrender()
        
    def myrender(self):
        for i in range(9):
            for j in range(9):
                if self.arr2d[i][j] == 0:
                    self.pb2d[i][j].setIcon(QIcon("0.png")) 
                if self.arr2d[i][j] == 1:
                    self.pb2d[i][j].setIcon(QIcon("1.png"))
                if self.arr2d[i][j] == 2:
                    self.pb2d[i][j].setIcon(QIcon("2.png"))
    
    def myclick(self):
        self.history = ""
        
        if self.flag_ing == False:
            return 

        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        int_i = int(arr_ij[0])
        int_j = int(arr_ij[1])

        
        if self.arr2d[int_i][int_j] > 0:
            return
        
        int_stone = 0
        
        if self.flag_wb:
            self.arr2d[int_i][int_j] = 1
            int_stone = 1
            
            if self.flag_wb==True:# 내가 놓아야지만 컴퓨터가 놓는다. 
            while True :#계속돌아가야되는게
                x = random.randrange(0,10)
                y = random.randrange(0,10)
                if self.arr2d[x][y]==0 :
                   self.arr2d[x][y]=1
                   self.flag_wb = not self.flag_wb
                   break
                else :
                  continue
            
            
        else:
            self.arr2d[int_i][int_j] = 2
            int_stone = 2
            
        up = self.getUP(int_i, int_j, int_stone)
        dw = self.getDW(int_i, int_j, int_stone)
        
        le = self.getLE(int_i, int_j, int_stone)
        ri = self.getRI(int_i, int_j, int_stone)
        
        ul = self.getUL(int_i, int_j, int_stone)
        ur = self.getUR(int_i, int_j, int_stone)
        
        dl = self.getDL(int_i, int_j, int_stone)
        dr = self.getDR(int_i, int_j, int_stone)
        
        d1 = up + dw + 1
        d2 = dl + ur + 1
        d3 = le + ri + 1
        d4 = ul + dr + 1
        
        if self.flag_wb == True:
            int_i = random.randrange(0,10)
            int_j = random.randrange(0,10)
            self.arr2d[int_i][int_j]
        
        self.myrender()
        
        for i in range(10):
            for j in range(10):
                self.history += str(self.arr2d[i][j])
        self.history2.append(self.history)
        print(self.history2)
        
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            if self.flag_wb:
                QMessageBox.about(self, "오목게임", "백돌이 이겼습니다.")
                self.myinsertDB(self.history2, self.flag_wb)
                self.flag_ing = False
            else:
                QMessageBox.about(self, "오목게임", "흑돌이 이겼습니다.")
                self.myinsertDB(self.history2, self.flag_wb)
                self.flag_ing = False
           
        self.flag_wb = not self.flag_wb
        
        
    def getUP(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_i += -1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else:
                    return count
        except:
            return count
        
    def getDW(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_i += 1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else:
                    return count
        except:
            return count
        
    def getLE(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_j += -1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else:
                    return count
        except:
            return count
        
    def getRI(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_j += 1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else:
                    return count
        except:
            return count
        
    def getUL(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_i += -1
                int_j += -1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else:
                    return count
        except:
            return count
        
    def getUR(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_i += -1
                int_j += 1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else:
                    return count
        except:
            return count
        
    def getDL(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_i += 1
                int_j += -1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else:
                    return count
        except:
            return count
        
    def getDR(self, int_i, int_j, int_stone):
        
        count = 0
        try:
            while True:
                int_i += 1
                int_j += 1
                if int_i < 0:
                    return count
                if self.arr2d[int_i][int_j] == int_stone:
                    count += 1
                else:
                    return count
        except:
            return count
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
