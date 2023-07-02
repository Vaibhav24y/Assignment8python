class A:
    def __init__(self,a,b,c):
        self.__a=a
        self._b=b
        self.c=c
    def display(self):
        print("Inside class a ")
        print(self.__a)
        print(self._b)
        print(self.c)
class B(A):
    def display(self):
        print("Inside calss b")
        try:
            print(self.__a)
        except AttributeError :
         print("private member Inaccessible")
        print("b",self._b)
        print("c",self.c)
        super().display()
f=B(30,20,10)
f.display()