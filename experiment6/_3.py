class Identifier:
    def __init__(self,id:str):
        self.__id=id
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,new_id):
        self.__id=new_id
    
if __name__=="__main__":
    exit()