import sys
import math
#x = input ("nhap canh a :")
#y = input ("nhap canh b :")
#z = input ("nhap canh c :")
def detect_triangle(x,y,z):
    if (x<= 0 or y <=0 or z <=0  or x > sys.float_info.max or
        y > sys.float_info.max or z > sys.float_info.max or
        type(x) not in [float ,int] or type(y) not in [float , int ] or
        type(z) not in [float, int] 
        ):
        return "du lieu khong hop le"
    elif y+x >z and x+z >y and z +y >x :
    
        if x == y and y ==z :
            return "tam giac deu"
        elif ((round(x**2) + round(y**2) == round(z**2) and x==y) or (round(y**2) + round(z**2) == round(x**2)
            and z ==y )or (round(x**2) + round(z**2) == round(y**2) and z==x)):
            return "tam giac vuong can"
        elif  (round(x**2) + round(y**2) == round(z**2) or round(y**2) + round(z**2) == round(x**2) or round(x**2) + round(z**2) == round(y**2)):
            return "tam giac vuong"
        
        elif x==y or y==z or x ==z:
            return "tam giac can"
            
        
        else:
            return "tam giac thuong"
    
    return "khong phai tam giac"
#print tamgiac(math.sqrt(2),math.sqrt(2),math.sqrt(4))
    
