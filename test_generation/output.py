#Name : Tran Van Trinh
#MSV: 10020378

import math
import unittest
import itertools
import re
import input


list_var=[]                                #luu cac bien cua mang
ret=[]                                #luu cac string tra ve vao list

vareflag=False
reflag=False
check=0



#Kiem tra cac khoang co bi trung nhau khong cua 1 bien


def checkdup(a):
    i=0
    while 1:
        for j in range(len(a)-1):
            if(a[i]<a[j]<a[i+1]):
                return False
        i=i+2
        if(i==len(a)):
            break
    return True


#Kiem tra cac khoang trong moi bien co bi trung nhau khong

def checklist_var(a):
    check=0
    for arrchild in a:
        if(checkdup(arrchild)):
            check+=1
        else:
            return False
    if(check==len(a)):
        return True

#Doc file input.py
#Doc mang cac bien  va cac gia tri tra ve


with open('input.py','r') as f:
    for line in f:
        if 'main' in line:
            reflag=True
        if (reflag==True) & ('return' in line):
            ret.append(line.strip().lstrip("return '").rstrip("'"))
        if line.strip().startswith("'''"):
            vareflag=True
            check=check+1
            if(check==1):
                continue
            else:
                vareflag=False
        if vareflag:
            list_var.append(map(int,re.findall(r'[0-9]+',line.strip())))


#Tim cac khoang tuong duong cua mot bien


def findAvg(lst):
    tmplst=[]
    i=0
    while 1:
        if(i>len(lst)-1):
            break
        tmplst.append( int(round((lst[i]+lst[i+1])/2)) )
        i=i+2
    print tmplst
    return tmplst


#Tim tat ca cac khoang tuong duong cua cac bien


def findAll(lst):
    tmpst=[]
    
    for child in lst:
        print child
        print findAvg(child)
        tmpst.append(findAvg(child))
        continue
    return tmpst

#Unittest
try:
            
    class output(unittest.TestCase):
        pass

    def test_generator(*args):
        def test(self):
            self.assertEqual(input.main(*args),1)
        return test

    if __name__=="__main__":
        if checklist_var(list_var)==False:
            raise Exception("wrong input")
        else :
            for arr in itertools.product(*findAll(list_var)):
                test_name='test_'+str(arr)
                test=test_generator(*arr)
                setattr(output,test_name,test)
        unittest.main()
except Exception as e:
    print "wrong input"
