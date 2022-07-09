#Operator Overloading

class Insan:
    def __init__(self,yas):
        self.yas = yas

    def __lt__(self,obj):
        return self.yas < obj.yas
    
    def __eq__(self,obj):
        return self.yas == obj.yas

    def __gt__(self,obj):
        return self.yas > obj.yas

    def __add__(self,obj):
        return self.yas + obj.yas

a = Insan(15)
b = Insan(15)

print(a+b)