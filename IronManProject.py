# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:30:50 2019

@author: Akhil
"""
import random

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
        return self.items[-1][2]
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
    

SQ = StudentQueue()
TQ =  TeacherQueue()
    
print("STUDENT TEACHER PROBLEM")
print()
print("Select Mode")
print("0. Pre defined mode")
print("1. Automatic Mode")
print("2. Mannual Mode")
print("Any other key to exit ONLY NUMERICS")
while True:
    try:
        ip_var = int(input("--> "))
        break
    except ValueError:
        pass
#ip_var = 1
if ip_var == 0:
    print("Predefined Mode Selected")
    print()
    Tat1, Tbt1 = 1, 2
    Tat2, Tbt2 = 2, 2
    Tat3, Tbt3 = 3, 2
    Tat4, Tbt4 = 14, 3
    TQ.enqueue(1, Tat1, Tbt1)
    TQ.enqueue(2, Tat2, Tbt2)
    TQ.enqueue(3, Tat3, Tbt3)
    TQ.enqueue(4, Tat4, Tbt4)
    Sat1, Sbt1 = 1, 2
    Sat2, Sbt2 = 2, 2
    SQ.enqueue(1, Sat1, Sbt1)
    SQ.enqueue(2, Sat2, Sbt2)
    teachers = TQ.size()
    students = SQ.size()
elif ip_var == 1:
    print("Automatic Mode Selected")
    auto = 1
    if auto == 1:
        tchr = random.randint(1, 51)
        lston = 0
        for xx in range (tchr):
            arrival_time = random.randint(1, 51)
            if arrival_time < lston:
                while True:
                    arrival_time = random.randint(1, 51)
                    if arrival_time >= lston:
                        break
            lston = arrival_time
            burst_time = random.randint(1, 51)
            idno = xx+1
            TQ.enqueue(idno, arrival_time, burst_time)
            print("Teacher",idno, "  AT:",arrival_time, " BT:",burst_time)
            
        stdnt = random.randint(1, 51)
        lston = 0
        for xx in range (stdnt):
            arrival_time = random.randint(1, 51)
            if arrival_time < lston:
                while True:
                    arrival_time = random.randint(1, 51)
                    if arrival_time >= lston:
                        break
            lston = arrival_time
            burst_time = random.randint(1, 51)
            idno = xx+1
            SQ.enqueue(idno, arrival_time, burst_time)
            print("Student",idno, "  AT:",arrival_time, " BT:",burst_time)
        teachers = TQ.size()
        students = SQ.size()
        print("Teachers: ", teachers)
        print("Students: ", students)
            
elif ip_var == 2:
    print("User Mode Selected")
    print()
    while True:
        try:
            teachers = int(input("Enter the number of Teachers in the queue: ", ))
            break
        except ValueError:
            pass
    t_data = []
    last_time = 0
    if teachers >= 0:
        for i in range(teachers):
            print("Enter Arrival Time for Teacher ",i+1, end = "")
            while True:
                try:
                    AT = int(input())
                    break
                except ValueError:
                    pass
            if (AT < last_time):
                while True:
                    print("AT can't be less then previous arrival time")
                    print("Enter Arrival Time for Teacher ",i+1, end = "")
                    while True:
                        try:
                            AT = int(input())
                            break
                        except ValueError:
                            pass
                    if last_time <= AT:
                        break
            last_time = AT
            print("Enter Burst Time for Teacher ",i+1, end = "")
            while True:
                try:
                    BT = int(input())
                    break
                except ValueError:
                    pass
            if BT <= 0:
                while True:
                    print("Error: BT can't be less than 1 ##Min BT req: 1")
                    print("Enter Burst Time for Teacher ",i+1, end = "")
                    while True:
                        try:
                            BT = int(input())
                            break
                        except ValueError:
                            pass
                    if BT > 0:
                        break                           
            temp_list = []
            temp_list.append(AT)
            temp_list.append(BT)
            t_data.append(temp_list)
    else:
        while True:
            print("Number of Teachers can't be less than 0")
            while True:
                try:
                    teachers = int(input("Pleas re-enter the number of Teachers: "))
                    break
                except ValueError:
                    pass
            if teachers >= 0:
                for i in range(teachers):
                    print("Enter Arrival Time for Teacher ",i+1, end = "")
                    while True:
                        try:
                            AT = int(input())
                            break
                        except ValueError:
                            pass
                    if (AT < last_time):
                        while True:
                            print("AT can't be less then previous arrival time")
                            print("Enter Arrival Time for Teacher ",i+1, end = "")
                            while True:
                                try:
                                    AT = int(input())   
                                    break
                                except ValueError:
                                    pass
                            if last_time <= AT:
                                break
                    last_time = AT
                    print("Enter Burst Time for Teacher ",i+1, end = "")
                    while True:
                        try:
                            BT = int(input())
                            break
                        except ValueError:
                            pass
                    if BT <= 0:
                        while True:
                            print("Error: BT can't be less than 1 ##Min BT req: 1")
                            print("Enter Burst Time for Teacher ",i+1, end = "")
                            while True:
                                try:
                                    BT = int(input())
                                    break
                                except ValueError:
                                    pass
                            if BT > 0:
                                break                           
                    temp_list = []
                    temp_list.append(AT)
                    temp_list.append(BT)
                    t_data.append(temp_list)
                break
                
    while True:
        try:
            students = int(input("Enter the nubers of Students in the queue: ", ))
            break
        except ValueError:
            pass
    s_data = []
    last_time = 0
    if students >= 0:
        for i in range(students):
            print("Enter Arrival Time for Student ",i+1, end = "")
            while True:
                try:
                    AT = int(input())
                    break
                except ValueError:
                    pass
            if (AT < last_time):
                while True:
                    print("AT can't be less then previous arrival time")
                    print("Enter Arrival Time for Student ",i+1, end = "")
                    while True:
                        try:
                            AT = int(input())  
                            break
                        except ValueError:
                            pass
                    if last_time <= AT:
                        break
            last_time = AT
            print("Enter Burst Time for Student ",i+1, end = "")
            while True:
                try:
                    BT = int(input())
                    break
                except ValueError:
                    pass
            if BT <= 0:
                while True:
                    print("Error: BT can't be less than 1 ##Min BT req: 1")
                    print("Enter Burst Time for Student ",i+1, end = "")
                    while True:
                        try:
                            BT = int(input())
                            break
                        except ValueError:
                            pass
                    if BT > 0:
                        break     
            temp_list = []
            temp_list.append(AT)
            temp_list.append(BT)
            s_data.append(temp_list)
    else:
        while True:
            print("Number of Students can't be less than 0")
            while True:
                try:
                    students = int(input("Pleas re-enter the number of Students: "))
                    break
                except ValueError:
                    pass
            if students >= 0:
                for i in range(students):
                    print("Enter Arrival Time for Student ",i+1, end = "")
                    while True:
                        try:
                            AT = int(input())
                            break
                        except ValueError:
                            pass
                    if (AT < last_time):
                        while True:
                            print("AT can't be less then previous arrival time")
                            print("Enter Arrival Time for Student ",i+1, end = "")
                            while True:
                                try:
                                    AT = int(input())
                                    break
                                except ValueError:
                                    pass
                            if last_time <= AT:
                                break
                    last_time = AT
                    print("Enter Burst Time for Student ",i+1, end = "")
                    while True:
                        try:
                            BT = int(input())
                            break
                        except ValueError:
                            pass
                    if BT <= 0:
                        while True:
                            print("Error: BT can't be less than 1 ##Min BT req: 1")
                            print("Enter Burst Time for Student ",i+1, end = "")
                            while True:
                                try:
                                    BT = int(input())
                                    break
                                except ValueError:
                                    pass
                            if BT > 0:
                                break     
                    temp_list = []
                    temp_list.append(AT)
                    temp_list.append(BT)
                    s_data.append(temp_list)
                break
        
    for i in range (teachers):
        TQ.enqueue(i+1, t_data[i][0], t_data[i][1])
    for i in range(students):
        SQ.enqueue(i+1, s_data[i][0], s_data[i][1])
else:
    exit()
    
maxlen =teachers+students
student_priority = 0
if SQ.isEmpty() or TQ.isEmpty():
    if SQ.isEmpty() and TQ.isEmpty():
        print("Teacher and Student Queues are EMPTY")
    elif SQ.isEmpty():
        if TQ.isEmpty() != True:
            curr_time = TQ.head()
        else:
            print("Both the Queues are EMPTY")
    elif TQ.isEmpty():
        curr_time = SQ.head()
else:
    curr_time = min(SQ.head(), TQ.head())
    
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
            if TQ.isEmpty() == False:
                print("Teacher ",TQ.id_no()," issued book")
                curr_time += TQ.burst_time()
                TQ.dequeue()
                break
    elif TQ.isEmpty():
        for i in range (students):
            if SQ.isEmpty() == False:
                print("Student ",SQ.id_no()," issued book")
                curr_time += SQ.burst_time()
                SQ.dequeue()
                break
    elif student_priority == 2:
            print("Student ",SQ.id_no()," issued book")
            curr_time += SQ.burst_time()
            student_priority = 0
            SQ.dequeue()
    else:
        tchr = TQ.head()
        stdnt = SQ.head()
        if tchr <= stdnt:
            if curr_time >= stdnt:
                student_priority += 1
            print("Teacher ", TQ.id_no()," issued book. Student Priority: ", student_priority)
            curr_time += TQ.burst_time()
            TQ.dequeue()
        elif tchr > stdnt:
            if curr_time >= tchr:
                student_priority += 1
                curr_time += TQ.burst_time()
                print("Teacher ", TQ.id_no()," issued book. Student Priority: ", student_priority)
                TQ.dequeue()
            else:
                curr_time += SQ.burst_time()
                print("Student ", SQ.id_no()," issued book")
                student_priority = 0
                SQ.dequeue()
   
