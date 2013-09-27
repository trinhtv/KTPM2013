import sys
import math
#x = input ("nhap canh a :")
#y = input ("nhap canh b :")
#z = input ("nhap canh c :")
def tamgiac(x,y,z):
    if x<= 0 or y <=0 or z <=0  or x >=sys.float_info.max or y >=sys.float_info.max or z >=sys.float_info.max:
        return "du lieu khong hop le!"
    else:
        if x == y and y ==z :
            return "tam giac deu !"
        elif (x**x + y**y == round(z**z) and x==y) or (y**y + z**z == round(x**x) and z ==y )or (x**x + z**z == round(y**z) and z==x):
            return "tam giac vuong can"
        elif y+x >z and x+z >y and z +y >x :
            if x==y or y==z or x ==z:
                return "tam giac can !"
            
        
        else:
            return "tam giac thuong !"
    
        return "khong phai tam giac!"
print tamgiac(1,1,math.sqrt(2))
    
