str=input("enter the string:")
def fun(str):
    n1=0
    n2=0
    for i in str:
        if i.islower():
            n1=n1+1
        elif i.isupper():
            n2=n2+1
    print("Number of lower case:",n1)
    print("Number of upper case:",n2)
fun(str)