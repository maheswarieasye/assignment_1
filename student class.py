class student:
    def set_name(self,name):
        self.name=name
        
    
    def get_name(self):
        return self.name

    def set_rno(self,rno):
        self.rno=rno

    def get_rno(self):
        return self.rno
    
    def __str__(self):
        return f"NAME:{self.name} \n ROLLNO:{self.rno}" 

obj=student()
obj.set_name("mahesh")
obj.set_rno(40)

print(obj.get_name())
print(obj.get_rno())
