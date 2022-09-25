str=input("enter the string:")
def reverse(str):
    a=""
    for i in str:
        a=i+a
    
    print("output:",a)

reverse(str)