class Product:
    def __init__(self,number:int,pclass:str,name:str,price:float):
        self.__number=number
        self.__pclass=pclass
        self.__name=name
        self.__price=price
    def get_property(self):
        print(f"Name:{self.__name}\nClass:{self.__pclass}\nPrice:{self.__price}\nNumber:{self.__number}\n")
    @property
    def number(self):
        return self.__number
   
    @number.setter
    def number(self,new_number):
        self.__number=new_number
    @property
    def pclass(self):
        return self.__pclass
    
    @pclass.setter
    def pclass(self,new_pclass:str):
        self.__pclass=new_pclass

    @property    
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name:str):
        self.__name=new_name
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,new_price:float):
        self.__price=new_price

if __name__=="__main__":
    product=Product(1000,"P","product",100)
    product.get_property()
    