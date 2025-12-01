# round(target,digits)
# digits means the number after point (5,--0.00001)
import math
class QuadraticEquation:
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
    def getDiscriminant(self)->float:
        return self.__b**2-4*self.__a*self.__c 
    def getRoot1(self):
        dct=self.getDiscriminant()
        if dct<0:
            return 0
        return round((math.sqrt(dct)-self.__b)/(2*self.__a),5)
    def getRoot2(self):
        dct=self.getDiscriminant()
        if dct<0:
            return 0
        return round((-math.sqrt(dct)-self.__b)/(2*self.__a),5)
    def printRoot(self):
        if self.getDiscriminant()==0:
            print(f"{self.getRoot1()}")
        elif self.getDiscriminant()>=0:
            print(f"Root1{self.getRoot1()}\nRoot2{self.getRoot2()}")
        else:
            print("Not real root!")
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self,new_a):
        self.__a=new_a
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self,new_b):
        self.__b=new_b
    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self,new_c):
        self.__c=new_c
if __name__=="__main__":
    target=QuadraticEquation(1,10,3)
    target.printRoot();
