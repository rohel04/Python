fruits=['apple','mango','grapes','oranges']
print(fruits[:-1])
fruits.append('banana')
print(fruits[-1])
fruits[0]='watermelon'
print(fruits)


x=[5,6,20,8,7]
temp=x[0]
for a in x:
   if temp<a:
        temp=a
   else:
       temp=temp
print(f'The largest number is: {temp}')
        
    