from math import pi

def func(yaricap,yukseklik):
    def daireAlan(yaricap):
        return (yaricap*yaricap)*pi
        
    
    return round((2*daireAlan(yaricap)) + 2*yaricap*pi*yukseklik,2)

print(func(5,10))


# import math

# def func(yaricap,yukseklik,pi=math.pi):
#     def daireAlan(yaricap):
#         alan = (yaricap*yaricap)*pi
#         return alan
    
#     return (2*daireAlan(yaricap)) + 2*yaricap*pi*yukseklik

# print(func(5,10))