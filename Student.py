class Student:
    def __init__(self, **k):
        for key, v in k.items():
            setattr(self, key, v) 

    def __str__(self):
        return str(self.__dict__)  
    
    def view_Detail(self,abc):
        for key,v in self.__dict__.items():
            if(key == abc):
                return v
        
        return "Not have this parameter"
    
    def update_Details(self,k,v):

        if k in self.__dict__.keys():
            self.__dict__[k] = v
        else:
            print("an exception occured")
       
        
        # for key,value in self.__dict__.items():
        #     if(key == k):
        #         self.__dict__[key] = v
        #         print("update Successfully")
        #         return self.__dict__
        
        # return "not have this parameter"

a = Student(name="Rudra", email="Rudrapatel@gmail.com", password="12345", Collage_name="DDU",weight="63",height="5.6",address="abcd")

print(a)

name = a.view_Detail("name")


name = a.update_Details("nam","ABC")

