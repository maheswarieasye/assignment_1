from re import X
from tkinter import Y


class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        

    def sqsum(self):

        return self.x**2+self.y**2+self.z**2

# point_x=int(input("enter x:"))
# point_y=int(input("enter y:"))
# point_z=int(input("enter z:"))

# x=int(input("enter x:"))
# y=int(input("enter y:"))
# z=int(input("enter z:"))

point_obj=point(1,4,6)
point_obj.sqsum()

print(point_obj.sqsum())
