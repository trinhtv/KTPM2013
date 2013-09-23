import triangle
import math
import unittest
import sys

class test_triangle(unittest.TestCase):
    
    def test_tamgiacthuong(self):
        self.assertEqual(triangle.detect_triangle(2,3,4) ,"tam giac thuong")
        
    def test_tamgiacvuong(self):
        self.assertEqual(triangle.detect_triangle(6,8,10) ,"tam giac vuong")
        
    def test_tamgiacvuong1(self):
        self.assertEqual(triangle.detect_triangle(5,4,3) ,"tam giac vuong")
        
    def test_tamgiacvuong2(self):
        self.assertEqual(triangle.detect_triangle(4,5,3) ,"tam giac vuong")
        
    def test_tamgiacvuongcan(self):
        self.assertEqual(triangle.detect_triangle(2,2,math.sqrt(8)) ,"tam giac vuong can")
        
    def test_tamgiacvuongcan1(self):
        self.assertEqual(triangle.detect_triangle(math.sqrt(8),2,2) ,"tam giac vuong can")
        
    def test_tamgiacvuongcan2(self):
        self.assertEqual(triangle.detect_triangle(2,math.sqrt(8),2) ,"tam giac vuong can")
        
    def test_tamgiaccan(self):
        self.assertEqual(triangle.detect_triangle(4,4,7) ,"tam giac can")

    def test_tamgiaccan1(self):
        self.assertEqual(triangle.detect_triangle(4,7,4) ,"tam giac can")

    def test_tamgiaccan2(self):
        self.assertEqual(triangle.detect_triangle(7,4,4) ,"tam giac can")
        
    def test_tamgiacdeu(self):
        self.assertEqual(triangle.detect_triangle(3,3,3) ,"tam giac deu")
    def test_tamgiacdeu(self):
        self.assertEqual(triangle.detect_triangle(2,3,6) ,"khong phai tam giac")
        
    def test_loidulieu9(self):
        self.assertEqual(triangle.detect_triangle(-3,4,5) ,"du lieu khong hop le")
        
    def test_loidulieu0(self):
        self.assertEqual(triangle.detect_triangle(3,-4,7) ,"du lieu khong hop le")
        
    def test_loidulieu1(self):
        self.assertEqual(triangle.detect_triangle(3,4,-7) ,"du lieu khong hop le")
        
    def test_loidulieu2(self):
        self.assertEqual(triangle.detect_triangle(-3,-4,7) ,"du lieu khong hop le")
        
    def test_loidulieu3(self):
        self.assertEqual(triangle.detect_triangle(-3,4,-7) ,"du lieu khong hop le")
        
    def test_loidulieu4(self):
        self.assertEqual(triangle.detect_triangle(3,-4,-7) ,"du lieu khong hop le")
        
    def test_loidulieu5(self):
        self.assertEqual(triangle.detect_triangle(-3,-4,-7) ,"du lieu khong hop le")
        
    def test_loidulieu6(self):
        self.assertEqual(triangle.detect_triangle(2**60,4,7) ,"du lieu khong hop le")
        
    def test_loidulieu7(self):
        self.assertEqual(triangle.detect_triangle(3,2**60,7) ,"du lieu khong hop le")
        
    def test_loidulieu8(self):
        self.assertEqual(triangle.detect_triangle(3,7,2**60) ,"du lieu khong hop le")
        
    def test_loidulieu10(self):
        self.assertEqual(triangle.detect_triangle(2**60,2**60,7) ,"du lieu khong hop le")
        
    def test_loidulieu11(self):
        self.assertEqual(triangle.detect_triangle(2**60,4,2**60) ,"du lieu khong hop le")
        
    def test_loidulieu13(self):
        self.assertEqual(triangle.detect_triangle(4,2**60,2**60) ,"du lieu khong hop le")
        
    def test_loidulieu12(self):
        self.assertEqual(triangle.detect_triangle(2**60,2**60,2**60) ,"du lieu khong hop le")
        
        
if __name__ == '__main__':
    unittest.main()

