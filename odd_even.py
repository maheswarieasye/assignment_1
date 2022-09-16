set=(1,3,4,5,6,8,7,9,0)
print("numbers=",set)
even=0
odd=0
for i in set:
    if (i%2)==0:
        even=even+1
    else:
        odd=odd+1
print("number of even numbers:",even)
print("number of odd numbers:",odd)