


number=int(input('Enter a number'))
def odd_even():
    return lambda a:a%2==0
check=odd_even()
result=check(number)
if(result):
    print("Even")
else:
    print("odd")