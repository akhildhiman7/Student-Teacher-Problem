# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:30:50 2019

@author: Akhil
"""
class StudentQueue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item, AT, BT):
        self.lst = []
        self.lst.append(item)
        self.lst.append(AT)
        self.lst.append(BT)
        self.items.insert(0,self.lst)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def head(self):
        return self.items[-1][1]
    def burst_time(self):
        return self.items.burst_time[-1][2]
    def id_no(self):
        return self.items[-1][0]
    

class TeacherQueue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item, AT, BT):
        self.lst = []
        self.lst.append(item)
        self.lst.append(AT)
        self.lst.append(BT)
        self.items.insert(0,self.lst)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def head(self):
        return self.items[-1][1]
    def burst_time(self):
        return self.items[-1][2]
    def id_no(self):
        return self.items[-1][0]

teachers = int(input("Eneter the number of Teachers in the queue: ", ))
t_data = []
last_time = 0
if teachers != 0:
    for i in range(teachers):
        print("Enter Arrival Time for Teacher ",i+1, end = "")
        AT = int(input())
        if (AT < last_time):
            while True:
                print("AT can't be less then previous arrival time")
                print("Enter Arrival Time for Teacher ",i+1, end = "")
                AT = int(input())            
                if last_time <= AT:
                    break
        last_time = AT
        print("Enter Burst Time for Teacher ",i+1, end = "")
        BT = int(input())
        temp_list = []
        temp_list.append(AT)
        temp_list.append(BT)
        t_data.append(temp_list)
    
students = int(input("Enter the nubers of Students in the queue: ", ))
s_data = []
last_time = 0
if students != 0:
    for i in range(students):
        print("Enter Arrival Time for Student ",i+1, end = "")
        AT = int(input())
        if (AT < last_time):
            while True:
                print("AT can't be less then previous arrival time")
                print("Enter Arrival Time for Student ",i+1, end = "")
                AT = int(input())            
                if last_time <= AT:
                    break
        last_time = AT
        print("Enter Burst Time for Student ",i+1, end = "")
        BT = int(input())
        temp_list = []
        temp_list.append(AT)
        temp_list.append(BT)
        s_data.append(temp_list)
    
TQ =  TeacherQueue()
for i in range (teachers):
    TQ.enqueue(i+1, t_data[i][0], t_data[i][1])
SQ = StudentQueue()
for i in range(students):
    SQ.enqueue(i+1, s_data[i][0], s_data[i][1])
    
maxlen =teachers+students
teacher_count = 0
student_count = 0
curr_time = 0
t = teachers
s = students
j = 0
k = 0

'''
print("No of teachers: ", t)
print("No of students: ", s)
print("AT of first student is ", SQ.items[s-1][1])
print("AT of first teacher is ", TQ.items[t-1][1])

'''

for i in range(maxlen):
    if (SQ.isEmpty()):
        for i in range (teachers):
            print("Teacher ",TQ.id_no()," issued book")
            TQ.dequeue()
        break
    elif TQ.isEmpty():
        for i in range (students):
            print("Student ",SQ.id_no()," issued book")
            SQ.dequeue()
        break
    else:
        tchr = TQ.head()
        stdnt = SQ.head()
        if tchr <= stdnt:
            if teacher_count <= 2:
                print("Teacher ", TQ.id_no()," issued book")
                ++teacher_count
                curr_time += TQ.burst_time()
                TQ.dequeue()
                teachers -= 1
            else:
                print("Student ", SQ.id_no()," issued book")
                SQ.dequeue()
                teacher_count = 0
                students -= 1
        elif tchr > stdnt:
            print("Student ", SQ.id_no()," issued book")
            SQ.dequeue()
            students -= 1
