# a=lambda b:b+5
# print(a(5))
# def myfun(n):
#     return lambda a:a*n
# double=myfun(2)
# print(double(5))
# triple=myfun(3)
# print(triple(5))

def even_odd():
    return lambda a:a%2==0
odd=even_odd()
print(odd(7))
