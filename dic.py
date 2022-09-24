


import string
N=26
def user(**c):
    for c in range(97, 123):
        print(chr(c), end = " ")
        
    res = string.ascii_lowercase[:N]
user()