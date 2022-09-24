
#write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

def last(n):
    return n[-1]
    
lst=[(2,3),(1,4),(5,2),(3,1),(4,6)]
lst2=sorted(lst, key=last)
print("original=",lst)
print("sorted=",lst2)